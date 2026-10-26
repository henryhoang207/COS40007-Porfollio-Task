"""Independent inference-only audit. No model training or model selection occurs here."""
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'
import json
import hashlib
import pickle
from pathlib import Path
import joblib
import numpy as np
import pandas as pd
import h5py
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score, balanced_accuracy_score, recall_score, log_loss, confusion_matrix

tf.config.threading.set_intra_op_parallelism_threads(2)
tf.config.threading.set_inter_op_parallelism_threads(2)
ROOT = Path(__file__).resolve().parent
ATOL, RTOL = 1e-6, 1e-6

def main():
    metadata = json.loads((ROOT / 'models/model_metadata.json').read_text())
    features = metadata['ordered_features']
    expected = ['tau1','tau2','tau3','tau4','p2','p3','p4','g1','g2','g3','g4']
    assert features == expected and set(features).isdisjoint({'p1','stab','stabf'})
    assert metadata['class_map'] == {'stable':0,'unstable':1}
    data_path = ROOT / 'data/Data_for_UCI_named.csv'
    assert hashlib.sha256(data_path.read_bytes()).hexdigest() == metadata['data_sha256']
    df = pd.read_csv(data_path)
    y = df.stabf.map(metadata['class_map']).astype('int64')
    dev_idx, test_idx = train_test_split(np.arange(len(df)),test_size=.3,stratify=y,random_state=42)
    fit_idx, val_idx = train_test_split(dev_idx,test_size=.2,stratify=y.iloc[dev_idx],random_state=43)
    splits = pd.read_csv(ROOT / 'results/split_indices.csv')
    assert splits.row_index.is_unique and set(splits.row_index) == set(range(10000))
    for role, indices in [('fit',fit_idx),('validation',val_idx),('test',test_idx)]:
        got = splits[splits.role==role].sort_values('split_position')
        np.testing.assert_array_equal(got.row_index.to_numpy(),indices)
        np.testing.assert_array_equal(got.target.to_numpy(),y.iloc[indices].to_numpy())
    assert not (set(dev_idx) & set(test_idx))
    folds = pd.read_csv(ROOT / 'results/cv_fold_indices.csv')
    assert folds.row_index.is_unique and set(folds.row_index) == set(dev_idx)
    assert folds.groupby('validation_fold').size().tolist() == [1400]*5
    saved = pd.read_csv(ROOT / 'results/test_predictions.csv')
    np.testing.assert_array_equal(saved.row_index.to_numpy(),test_idx)
    np.testing.assert_array_equal(saved.truth.to_numpy(),y.iloc[test_idx].to_numpy())
    table = pd.read_csv(ROOT / 'results/master_results.csv').set_index('model')
    assert set(table.index) == {'RF','MLP','ANN-1','ANN-2'} and len(table)==4
    cv = pd.read_csv(ROOT / 'results/traditional_cv_results.csv')
    for name in ['RF','MLP']:
        rows=cv[cv.model==name]
        assert len(rows)==5 and set(rows.fold)=={1,2,3,4,5}
        for score in ['accuracy','weighted_f1']:
            assert abs(float(table.loc[name,f'cv_{score}_mean'])-rows[score].mean()) < 1e-12
            assert abs(float(table.loc[name,f'cv_{score}_sd'])-rows[score].std(ddof=1)) < 1e-12
    scaler=joblib.load(ROOT / 'models/standard_scaler.pkl')
    assert scaler.n_samples_seen_==7000
    assert list(scaler.feature_names_in_)==features
    np.testing.assert_allclose(scaler.mean_,df.iloc[dev_idx][features].mean().to_numpy(),atol=1e-12)
    np.testing.assert_allclose(scaler.var_,df.iloc[dev_idx][features].var(ddof=0).to_numpy(),atol=1e-12)
    X_test=df.iloc[test_idx].loc[:,features]
    truth=y.iloc[test_idx]
    frozen_path=ROOT / 'results/frozen_configurations.json'
    frozen=json.loads(frozen_path.read_text())
    assert hashlib.sha256(frozen_path.read_bytes()).hexdigest()==metadata['frozen_configuration_sha256']
    assert frozen['frozen_before_task3_test_predictions'] is True
    evidence={}
    for name,filename in [('RF','random_forest.pkl'),('MLP','mlp_classifier.pkl'),
                          ('ANN-1','ann_batch32.h5'),('ANN-2','ann_batch64.h5')]:
        if name in ['RF','MLP']:
            model=joblib.load(ROOT / 'models' / filename)
            for attr in ['mean_','scale_','var_']:
                np.testing.assert_array_equal(getattr(model['scale'],attr),getattr(scaler,attr))
            assert list(model['scale'].feature_names_in_)==features
            assert model['scale'].n_samples_seen_==7000
            probs=model.predict_proba(X_test)
            pred=model.predict(X_test)
        else:
            path=ROOT / 'models' / filename
            assert h5py.is_hdf5(path)
            with h5py.File(path) as h:
                assert 'model_config' in h.attrs and 'training_config' in h.attrs
                assert 'model_weights' in h and 'optimizer_weights' in h
            model=tf.keras.models.load_model(path)
            assert model.input_shape==(None,11) and model.output_shape==(None,2)
            dense=[l for l in model.layers if isinstance(l,tf.keras.layers.Dense)]
            drops=[l for l in model.layers if isinstance(l,tf.keras.layers.Dropout)]
            assert [l.units for l in dense]==[64,32,16,2]
            assert [l.activation.__name__ for l in dense]==['relu','relu','relu','softmax']
            assert [l.rate for l in drops]==[.2,.2] and model.count_params()==3410
            probs=model(scaler.transform(X_test).astype('float32'),training=False).numpy()
            pred=probs.argmax(axis=1)
            assert abs(float(table.loc[name,'test_crossentropy_loss'])-log_loss(truth,probs,labels=[0,1]))<1e-5
            batch=frozen['ann'][name]['batch_size']
            for kind in ['development','final']:
                with (ROOT / f'results/ann_batch{batch}_{kind}_history.pkl').open('rb') as f:
                    history=pickle.load(f)
                assert all(np.isfinite(v).all() for v in history.values())
                if kind=='development':
                    assert len(history['loss'])==len(history['val_loss'])<=50
                    assert np.argmin(history['val_loss'])+1==frozen['ann'][name]['epochs']
                else:
                    assert len(history['loss'])==frozen['ann'][name]['epochs']
                    assert 'val_loss' not in history
        expected_probs=saved[[name+'_p_stable',name+'_p_unstable']].to_numpy()
        np.testing.assert_allclose(probs,expected_probs,atol=ATOL,rtol=RTOL)
        np.testing.assert_array_equal(pred,saved[name+'_prediction'].to_numpy())
        metrics={'test_accuracy':accuracy_score(truth,pred),
                 'test_weighted_f1':f1_score(truth,pred,average='weighted'),
                 'balanced_accuracy':balanced_accuracy_score(truth,pred),
                 'macro_f1':f1_score(truth,pred,average='macro'),
                 'unstable_recall':recall_score(truth,pred,pos_label=1),
                 'unstable_as_stable':int(confusion_matrix(truth,pred,labels=[0,1])[1,0])}
        for key,value in metrics.items():
            assert abs(float(table.loc[name,key])-value)<1e-12,(name,key,value,table.loc[name,key])
        evidence[name]={'class_predictions_identical':True,
                        'maximum_probability_difference':float(np.max(np.abs(probs-expected_probs))),
                        'metrics_recomputed_and_equal':True,'raw_rows_checked':len(X_test)}
    result={'passed':True,'fresh_process':True,'atol':ATOL,'rtol':RTOL,
            'data_hash_verified':True,'split_reconstruction_verified':True,
            'common_scaler_development_only_verified':True,'cv_summary_recomputed':True,
            'whole_model_hdf5_verified':True,'metadata_feature_order_verified':True,
            'models':evidence}
    (ROOT / 'results/artifact_verification.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps(result,indent=2))

if __name__=='__main__':
    main()
