# Acceptance evidence

| Requirement | Evidence |
|---|---|
| Four core configurations | Executed notebook; results/master_results.csv |
| Traditional five-fold CV and weighted F1 | results/traditional_cv_results.csv; results/traditional_cv_summary.csv |
| No leaked or redundant predictors | results/data_audit.json; models/model_metadata.json |
| Fixed disjoint splits and fit-only trial scaling | results/split_indices.csv; results/split_verification.json |
| ANN architecture, pilot, batches 16/32/64 and callbacks | Notebook model summary; results/ann_development_verification.json; saved histories |
| Frozen recipe before Task 3 test predictions | results/frozen_configurations.json; results/final_evaluation_verification.json |
| Common final development scaler | models/standard_scaler.pkl; independent artifact audit |
| Reports, confusion matrices and learning curves | results/classification_reports.json; figures/; report/ |
| Whole-model .h5 exports and traditional .pkl pipelines | models/ and results/model_artifact_manifest.json |
| Fresh-process raw-row reload and metric agreement | results/artifact_verification.json |
| Clean pinned verification environment | results/fresh_environment_verification.json |
| Fresh-kernel full execution in separate checkout | results/fresh_reproduction_verification.json; results/notebook_execution_verification.json |
| Exact hashed-file bytes in Git | .gitattributes; results/git_byte_preservation_verification.json |
| Incremental commits and pushes | Repository Git history; PHASE_VERIFICATION.md |
| Student-deferred reflection, Canvas details and submission | SUBMISSION_TODO.md - TBD by user instruction |

These checks establish reproducibility of this assisted benchmark analysis. They
do not establish real-grid deployment readiness or compliance with the brief's
restriction on whole-code generation. Actual assistance is disclosed in
ASSISTANCE_LOG.md and the report.
