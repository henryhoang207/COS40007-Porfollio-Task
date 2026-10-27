# Portfolio 3 task and rubric review

Reviewed 27 October 2026 against the user's supplied A-D task text and two rubric
images. The user requested an audit and a Word explanation with screenshot
placeholders. Assessment documents supply criteria; their generic CNN, LSTM and
regression alternatives are not instructions to change this tabular
classification task.

## Conclusion

All applicable A-D technical steps are present. The existing evidence supports
the **Excellent band for all seven scored criteria**, with **68 points
available**. This is an evidence review, not an awarded or guaranteed 68/68.
The architecture row overlaps across the two images and is counted once.

The original PDF lacks an Acknowledgement of Country and actual submission
date. The new Word explanation adds the acknowledgement and a complete cover
structure; actual submission date remains TBD. Both criteria carry zero points
in the supplied rubric, so no numerical deduction is invented for them.

The earlier brief prohibits whole-code generation; actual AI-generated
implementation is disclosed. This authorship issue remains unresolved and is
separate from the seven technical rubric criteria. Honest disclosure alone is
not compliance. Personal GenAI learning reflections and Canvas details remain
TBD in `../SUBMISSION_TODO.md`, following the user's explicit instruction.

## Scored criteria

| Criterion | Maximum | Current evidence |
|---|---:|---|
| Traditional ML models | 10 | RF and MLP; appropriate configurations; test accuracy and weighted F1; 5-fold accuracy/F1; comparison; clear best traditional model |
| Traditional ML visualisation | 6 | Four-model accuracy bars with labels, values and 63.8% majority baseline; report interprets the three-case leading gap |
| Deep learning data preparation | 12 | 11 features; scaled tabular data; stratified training/validation/test; fit-only scaling; documented dimensions |
| Deep learning architecture and training | 16 | 64/32/16 dense, two dropout 0.2 layers, two Softmax outputs; Adam and sparse crossentropy; callbacks; pilot/trials; saved H5 |
| Deep learning evaluation | 12 | Test accuracy/loss, weighted/per-class F1, classification reports, confusion matrices, accuracy/loss curves; comparison with MLP |
| Final summary and reflection | 8 | Four-row master table; primary-metric winner and caveats; deployment discussion; all three technical model reflections |
| GitHub repository | 4 | Models/results/comments and eight actual phased implementation commits; repository links in reports |
| **Total** | **68** | Technical evidence fits Excellent; marker determines awarded points |

## Every requested step

Physical notebook cell numbers count Markdown and code cells. Execution labels
In [n] count code cells only. The notebook is
`../Portfolio_Assessment_3_HoangHuuHoan.ipynb`.

| Step | Evidence |
|---|---|
| A1 load and analyse | Cells 5/6; 10,000 rows; target stabf; stable 0 and unstable 1 |
| A2 preprocess | Cell 6; 7,000/3,000 split; shapes; fit-only StandardScaler |
| A3 train RF and MLP | Cell 8 cross-validation; cell 12 final fits |
| A4 evaluate and compare | Cells 8/14; accuracy, weighted F1, 5-fold CV; MLP best traditional |
| A5 visualise | Cell 14; figures/final_accuracy_comparison.png; all four core models |
| B1 tabular input | Cell 6; fit 5600x11, validation 1400x11, test 3000x11; common final training 7000x11 |
| B2 architecture and compile | Cells 3/10; 3410 parameters; 64/32/16/dropout/Softmax; Adam/crossentropy/accuracy |
| B3 train | Cell 10; 10-epoch pilot; batches 16/32/64; up to 50 epochs; 20% validation reserve; patience 10 and 5 callbacks |
| B4 classification evaluation | Cell 14; classification reports, accuracy/loss/F1, confusion matrices and curves |
| B5 persistence | Cell 16; two whole H5 models; development and final pickle histories; reload audit |
| C1 master results | Cell 14; results/master_results.csv; two traditional and two core ANN configurations |
| C2 winner and production | Cells 14/18; ANN-2 accuracy leader by 3/3000; metric-dependent choice; deployment limits |
| C3 model reflection | Cell 18; architecture effects/limits, traditional comparison and future improvements |
| D GitHub | Eight phased implementation commits through 4768cce; published notebook, models, results and reports |

Classification is the applicable branch. R squared, RMSE, MAE and continuous
actual-versus-predicted scatter are not required. The generic master-table
CNN/LSTM labels are alternatives; ANN-1 and ANN-2 satisfy this dataset's branch.
The extra batch-16 development trial is retained without inventing a test score.

## Important interpretation limits

- The test split was used in earlier portfolios. It is a previously inspected
  benchmark, not untouched external validation.
- ANN trial curves use 5600/1400 fit/validation rows and callbacks. Final saved
  ANNs are fresh 7000-row fixed-rate refits for the selected 39/46 epochs. Their
  histories are separate and must not be conflated.
- ANN-2 accuracy is 96.57%, versus MLP 96.47%: three cases, 0.10 percentage
  points. MLP leads balanced accuracy; ANN-1 has the fewest unstable-as-stable
  errors. No statistical superiority or production-readiness claim is made.
- Widths and dropout were not ablated. Batch comparisons also differ in update
  budget, selected epochs and learning-rate reductions; causal claims are limited.
- No five-fold ANN CV was performed. Validation results are not labelled CV.

## Screenshot guide

The Word explanation has matching placeholders and complete capture instructions.
Paths below are relative to `portfolio_task3`.

| Slot | What and where to capture |
|---|---|
| S01 | Dataset audit and printed shapes; notebook cells 5/6, In [2]/[3]; two crops if needed |
| S02 | Traditional CV summaries; cell 8, In [4], plus RF/MLP master rows in cell 14, In [7] |
| S03 | Full ANN summary and 3410 trainable parameters; cell 10, In [5] |
| S04 | Callback definitions in train_trial; cell 10 code; patience, restore weights, factor and minimum LR |
| S05 | Pilot and all three batch trial rows; cell 10, In [5] |
| S06 | figures/ann_core_development_loss.png; both core batches, axes, legends and best epochs |
| S07 | figures/ann_core_development_accuracy.png; both core batches and legends |
| S08 | figures/ann_development_learning_rate.png; all three batches and LR steps |
| S09 | Both ANN class reports; cell 14, In [7]; precision, recall, F1 and support |
| S10 | figures/final_confusion_matrices.png; all four model panels and labelled axes |
| S11 | models folder plus passed reload output in cell 16, In [8]; two crops |
| S12 | Four-row master table; cell 14, In [7] |
| S13 | figures/final_accuracy_comparison.png; four bars, values and baseline |
| S14 | report/supporting_figures/classification_probability_scatter.png; all four panels |
| S15 | GitHub portfolio_task3 files and Commits on main; two crops showing identity/history |

The new probability scatter reads only `results/test_predictions.csv`. It plots
each saved unstable probability against the true class, with fixed-seed 42
horizontal jitter uniformly between -0.14 and 0.14 for readability, shared across
models. All 3000 rows appear in each panel; correctness comes from the saved
class predictions; probability 0.5 is marked. It changes no predictions and is
not a calibration test. No fitting or selection is performed.

## Verification

The independent model-reload audit passed again on all 3000 rows per model,
with exact classes and probabilities within absolute/relative tolerance 1e-6.
Existing records prove the clean-environment ten-cell full execution and the
earlier fresh remote-clone check. New document render, content, hash and remote
publication evidence is recorded in `../results/word_report_verification.json`.
QA page images and preview PDF stay outside the repository.

The Word document is a requested screenshot draft. Replace S01-S15 and supply
the submission date; deferred personal/Canvas fields remain TBD. No Canvas
submission is claimed.
