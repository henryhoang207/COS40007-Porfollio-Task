# Portfolio Task 3d: end-to-end assignment plan

Prepared: 26 October 2026. Status: planning complete; implementation and measured results are future work.

## 1. Scope and sources

Read all six pages of `Portfolio Task 3d - Advanced ML Models and Deep Learning - MLP for Classification.pdf` and the Portfolio 1 and 2 notebooks. Use the existing Electrical Grid Stability Simulated Data dataset and the classification pathway.

Confirmed GitHub Classroom destination: [henryhoang207/COS40007-Porfollio-Task](https://github.com/henryhoang207/COS40007-Porfollio-Task) (the Portfolio 2 repository, confirmed by the student).

The PDF prints a due date of 10/05/2026 at 23:59. Confirm the current deadline and submission fields on Canvas; the printed date is earlier than the planning date.

## 2. Decisions from the brief

| Requirement | Planned implementation | Brief location |
|---|---|---|
| Two named traditional classifiers | RandomForestClassifier and scikit-learn MLPClassifier | A.3, pp. 1-2 |
| Scaling and displayed split shapes | StandardScaler; print development, validation, and test dimensions | A.2; B.1 |
| Traditional evaluation | Accuracy, weighted F1, and five-fold stratified CV | A.4, p. 2 |
| ANN architecture | 64-ReLU, dropout 0.2, 32-ReLU, dropout 0.2, 16-ReLU, two-unit Softmax | B.2, pp. 3-4 |
| ANN compilation | Adam, sparse categorical crossentropy, accuracy; print model summary | B.2, p. 4 |
| ANN experiments | Compare batch sizes 16, 32, and 64; begin with a 10-epoch pilot and allow at most 50 epochs per subsequent run | B.3, p. 4 |
| Validation and callbacks | Reserve 20% of development data; early stopping patience 10 with restored best weights; halve learning rate after 5 stagnant validation-loss epochs | B.3, p. 4 |
| ANN evaluation | Test loss and accuracy, class report, confusion matrix, train/validation loss and accuracy curves | B.4, p. 4 |
| At least two deep-learning configurations | ANN-1 batch 32 and ANN-2 batch 64; record the batch-16 experiment as well | C.1, p. 5 |
| Model exports | Whole ANN models as .h5, ANN training histories as .pkl; traditional model files as .pkl as requested | B.5 and requested deliverables |
| Final interpretation | Master table, best observed model, deployment discussion, and the three model reflection questions | C.1-C.3, p. 5 |
| GitHub evidence | Genuine incremental commits and pushes; repository link in report | D, p. 5 |
| GenAI reflection | Complete the supplied template honestly in the report | E, pp. 5-6 |

Interpret two template inconsistencies conservatively. A.5 mentions a chart across three models, while C.1 shows two traditional and two deep-learning rows: show all four core configurations in the final chart and table. C.1 labels its deep-learning examples CNN/LSTM, but Part B explicitly specifies ANN for tabular data: label the two deep-learning rows ANN-1 and ANN-2. Do not add a CNN or LSTM.

The requested notebook is the main analysis deliverable. The PDF also explicitly requires a short report containing the GenAI reflection and GitHub link, so plan that as an additional submission item unless the instructor has provided a later replacement instruction.

## 3. Dataset and continuity

- Source: the existing `Portfollio_Task2/data/Data_for_UCI_named.csv`; copy the unchanged CSV into the Task 3 repository working directory and record its SHA-256.
- Size: 10,000 independent simulated configurations, 14 original columns.
- Target: `stabf`, with stable = 0 and unstable = 1.
- Class counts: 3,620 stable and 6,380 unstable; a majority-only classifier has 63.8% accuracy.
- Ordered predictors: `tau1`, `tau2`, `tau3`, `tau4`, `p2`, `p3`, `p4`, `g1`, `g2`, `g3`, `g4`.
- Exclude `stab`: its sign determines the target and would leak the answer.
- Exclude `p1`: it is redundant with the consumer powers, consistently with prior portfolios.
- Retain all valid rows. Recheck missing values, duplicates, label values, and column order. Prior work found no missing or duplicate rows; do not add unnecessary imputation or resampling.
- Use the same 11 original predictors for all four core models. Feature engineering from Task 2 is an optional later extension, rather than part of the required comparison.

Task 2 used a stratified 70/30 split with seed 42. Its test results were already examined, and Task 1 EDA used the full dataset. Reuse the split for continuity, describe it as a previously inspected benchmark, and make all Task 3 modelling choices from development evidence. Do not claim a new, untouched external validation set.

Task 2 contains executed notebook outputs but its generated result folders and saved traditional models are absent. Treat its SVM/DT results as historical context. They cannot replace the newly required RF and MLP experiments or be presented as new Task 3 measurements.

## 4. Evaluation protocol to declare before training

1. Reconstruct the stratified 70/30 split with seed 42: 7,000 development rows and 3,000 test rows. Save original row indices, feature order, target map, and the data hash.
2. Evaluate each fixed traditional configuration with five shuffled stratified folds on the 7,000 development rows, seed 42. Put StandardScaler inside each pipeline so scaling is fitted on the training portion of each fold. Report accuracy and weighted-F1 means plus sample fold SD; SD is not a confidence interval.
3. Create a fixed stratified internal ANN split from the 7,000 development rows, seed 43: 5,600 fit rows and 1,400 validation rows. This is the brief's 20% validation reserve. Pass these subsets explicitly to keep validation stratified.
4. Fit the ANN trial scaler only on the 5,600 fit rows. Transform validation with that scaler. Use the identical fit/validation subsets for every batch-size experiment. Test data is not used in training, callbacks, or selection.
5. Select settings and record the best epoch for each of the two predeclared ANN configurations using validation loss. Do not assume ANN will win. Freeze all configurations and the final refit recipe before viewing Task 3 test results.
6. For a final comparison with identical training inputs, fit a fresh common StandardScaler on all 7,000 development rows. Refit both traditional models and both ANNs on those same scaled development arrays. Each ANN starts fresh and trains for its validation-selected epoch count, capped at 50, with its fixed initial Adam learning rate. No validation-dependent callbacks run in this final refit because no validation subset remains.
7. Evaluate all frozen final models on the same 3,000 test rows. Produce all metrics from these predictions. Do not revise the models after comparing test results.

The final ANN refits are separate from the trial models that used early stopping and learning-rate reduction. Their learning-rate schedules can therefore differ. Label the required learning curves as development trial histories, and label the table's test scores and saved .h5 files as final refit results. Save both development histories and final fit histories so that the distinction is auditable.

Five-fold CV is explicitly required for the traditional classifiers. ANN five-fold CV is an optional extension; mark its CV cells as not performed rather than treating its internal validation accuracy as a CV estimate.

Keep the default class decision rule: argmax of the two Softmax probabilities. Any future decision-threshold experiment must use development data only and be labelled as an extension.

## 5. Models and bounded experiments

| Model | Initial configuration | Purpose |
|---|---|---|
| Random Forest | 300 trees, standard classifier defaults otherwise, fixed seed | Required tree-ensemble comparator |
| scikit-learn MLP | Hidden layers (64, 32, 16), ReLU, Adam, StandardScaler, fixed seed, max_iter initially 500 | Required traditional-library neural-network comparator |
| ANN-1 | Required 64/32/16 architecture, dropout 0.2 twice, Softmax(2), Adam initial learning rate 0.001, batch 32 | Required deep-learning baseline |
| ANN-2 | Same required architecture and initial learning rate, batch 64 | Controlled parameter comparison |

Also run batch 16 during the ANN development experiment and retain its validation results. The two named core ANN configurations remain visible even if batch 16 performs best; if useful, add batch 16 as an extra clearly labelled result rather than silently dropping a required core row.

Start with a 10-epoch pilot, then run fresh, seeded development trials with a maximum of 50 epochs. Use validation-loss early stopping with patience 10 and restore_best_weights enabled. Use validation-loss learning-rate reduction with factor 0.5 and patience 5. State the pilot, maximum epoch limit, actual epochs, best epoch, and learning-rate choices.

The sklearn MLP and Keras ANN are both neural networks. Explain that the comparison follows the brief's tool groupings and examines training implementation, dropout, batch size, and stopping behaviour; do not describe them as fundamentally unrelated model families.

Inspect sklearn convergence warnings. Increase its iteration limit only when training diagnostics justify it, document the change before final test evaluation, and avoid an open-ended search. If extra tuning is necessary, use development-only inner selection; report selected CV scores honestly and do not call them an unbiased nested-CV estimate.

## 6. Single-notebook structure

1. Title, student details, engineering question, scope, and brief GenAI-use disclosure pointing to the report.
2. Setup: dependency versions, random seeds, relative paths, and output folders.
3. Data loading and checks: source, shape, target counts, exclusions, and ordered predictors.
4. Reproducible split and scaling: all dimensions, saved indices, and leakage explanation.
5. Part A: RF and sklearn MLP definitions, five-fold CV, fold-level results, and concise interpretation.
6. Part B: ANN architecture explanation and summary; development trials, callbacks, batch comparison, and learning curves.
7. Frozen configurations and shared final refits.
8. Final test evaluation: required metrics, reports, confusion matrices, master comparison, and saved charts.
9. Model persistence and reload verification using the exported files.
10. Part C reflections: architecture effects, whether ANN outperformed the traditional models, improvements with more time, and deployment discussion.
11. Reproduction and submission checklist, repository link, and references.

Keep all modelling and analysis code in this one notebook. Use notebook Markdown for the interpretation and actual outputs for evidence. Avoid placeholder results or copied conclusions from earlier assessments.

## 7. Metrics, charts, and conclusions

Master results table: model type, configuration name, test accuracy, test weighted F1, balanced accuracy, macro-F1, unstable recall, test crossentropy loss for Keras ANNs, traditional CV accuracy/weighted-F1 mean and SD, and relevant training settings. Use explicit not-applicable/not-performed cells instead of invented scores.

Required figures: one final accuracy comparison chart with all four core configurations; ANN training/validation loss curves; ANN training/validation accuracy curves; and labelled ANN confusion matrices. Save the figures separately for the report. Include per-class classification reports, with stable/unstable labels and support counts. Additional traditional confusion matrices are useful for a consistent error comparison.

Use the actual final metrics to state which tested configuration had the highest test accuracy, while distinguishing this observed ranking from development-based selection. Discuss weighted F1 and unstable-as-stable errors as well. Small differences on one split do not establish a universal winner.

The architecture reflection should explain why the required widths, ReLU, dropout, Softmax, and stopping settings were chosen. Since core layer widths are held fixed, do not claim to have experimentally established which width is best. Use the controlled batch comparison and learning curves as the evidence actually collected.

The deployment answer must address simulation-only data, previously inspected test data, domain shift, error costs, and the need for external validation. Do not claim production readiness from this assignment benchmark.

## 8. Saved files and repository layout

Suggested layout inside the confirmed Classroom repository:

```text
portfolio_task3/
  Portfolio_Assessment_3_HoangHuuHoan.ipynb
  README.md
  requirements.txt
  .gitignore
  data/
    Data_for_UCI_named.csv
  models/
    random_forest.pkl
    mlp_classifier.pkl
    ann_batch32.h5
    ann_batch64.h5
    standard_scaler.pkl
    model_metadata.json
  results/
    split_indices.csv
    frozen_configurations.json
    traditional_cv_results.csv
    ann_development_results.csv
    master_results.csv
    test_predictions.csv
    ann_batch32_development_history.pkl
    ann_batch64_development_history.pkl
    ann_batch32_final_history.pkl
    ann_batch64_final_history.pkl
    artifact_verification.json
  figures/
  report/
    Portfolio_Assessment_3_Report.pdf
```

Save the traditional files as complete fitted preprocessing/model pipelines so they accept raw predictor rows. Their final scalers should match the separately exported common scaler used with the ANN files. The metadata records the ordered 11 features, class map, argmax decision rule, seed, versions, data hash, architecture/settings, and which scaler accompanies the ANNs.

The required .h5 files must contain whole ANN models, rather than only weights or renamed .keras files. An optional additional .keras copy can be useful, but does not replace the brief's .h5 deliverable. Verify the chosen runtime's save/load behaviour during setup.

Use a clean Python 3.12 environment and verify TensorFlow/Keras, scikit-learn, NumPy, pandas, matplotlib/seaborn, h5py, and Jupyter compatibility before selecting exact package versions. Python 3.12 is already installed; the shell currently defaults to Python 3.14. Pin the working package set after the compatibility check. CPU training is the initial plan.

Do not commit the environment, caches, credentials, or temporary files. Preserve dataset attribution/licensing. Check repository file sizes and use the repository's appropriate large-file workflow if an artifact exceeds its normal upload limit.

## 9. Work stages and real Git history

| Stage | Work and completion evidence | Example commit |
|---|---|---|
| 1. Prepare | Use the confirmed repository's existing history; add Task 3 paths, README, dependency setup, student-written notebook outline, and honest assistance log | Set up Portfolio 3 analysis |
| 2. Data | Reproduce target/exclusions, verify CSV hash, save split indices, and display shapes | Prepare grid classification data and splits |
| 3. Traditional ML | Complete RF and MLP CV, diagnostics, and interpretations | Compare Random Forest and MLP classifiers |
| 4. ANN development | Complete required architecture, batch trials, callbacks, and saved histories | Evaluate ANN batch configurations |
| 5. Final evaluation | Freeze configurations, run final refits/test evaluation, create tables/figures | Complete final model comparison |
| 6. Persistence | Export required models, scaler, metadata, and verify reloaded predictions | Save and verify trained models |
| 7. Submission | Restart/run notebook, finish report/reflections, verify remote contents and links | Finalise Portfolio 3 submission |

Commit and push as each actual stage is completed, as required by the brief. Do not create artificial milestones retrospectively or put the entire assignment into one final commit. Preserve earlier portfolio work when establishing the Task 3 checkout. No repository is being published or changed as part of this planning document.

## 10. Acceptance checks

- Restart the notebook kernel and Run All successfully in the documented environment, using relative paths and the included CSV.
- All four core configurations, required metrics, summaries, learning curves, reports, and confusion matrices are present, with accurate labels.
- No predictor contains `stab`, `stabf`, or `p1`; no fit, selection, callback, or scaler training uses the test rows.
- There are two traditional .pkl files, at least two whole-model ANN .h5 files, the common scaler, metadata, and pickled ANN histories.
- In a fresh kernel or process, reload each saved artifact. Traditional predictions must match; ANN probabilities must agree within a declared numerical tolerance and class predictions must match. Check raw-row inference with the saved scaler and feature order.
- Recomputed metrics agree with saved predictions and the final table. Every split index has the intended role, with no train/test overlap.
- Check the repository from a fresh checkout/environment using the README, and verify the notebook, models, and report exist remotely.
- The concise report contains selected figures, a short results explanation, the confirmed GitHub URL, and the exact mandatory GenAI reflection headings: tools used, specific tasks and exact prompts, debugging/code attribution, and learning reflection.
- The student writes the personal learning reflection and verifies that every assistance claim is true. Resolve any notebook placeholders before submission.
- Confirm the current Canvas deadline and accepted file fields; then submit the notebook, model artifacts, report, and repository URL in the required locations.

## Technical references for implementation

- [TensorFlow installation and platform support](https://www.tensorflow.org/install/pip)
- [Keras whole-model saving/loading](https://keras.io/api/models/model_saving_apis/model_saving_and_loading/)
- [Keras legacy HDF5 saving documentation](https://keras.io/2/api/models/model_saving_apis/model_saving_and_loading/)

Use the assignment PDF as the controlling source for required architecture, metrics, file extensions, reflections, and GitHub evidence. Technical library documentation guides implementation compatibility; it does not replace the assignment instructions.
