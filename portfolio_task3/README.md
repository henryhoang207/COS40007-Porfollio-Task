# Portfolio 3 - Electrical grid stability classification

Hoang Huu Hoan, 105732188. COS40007 Artificial Intelligence Engineering.

The analysis compares Random Forest, scikit-learn MLP, ANN-1 (batch 32) and ANN-2
(batch 64) using the same 11 original predictors and final 7,000/3,000 split.
Batch 16 is also evaluated during ANN development. All modelling code is in
`Portfolio_Assessment_3_HoangHuuHoan.ipynb`.

Repository: [henryhoang207/COS40007-Porfollio-Task](https://github.com/henryhoang207/COS40007-Porfollio-Task).
Earlier portfolio files at repository root are preserved.

## Reproduce

Use Python 3.12 on a CPU. From the repository root on Windows PowerShell:

```powershell
py -3.12 -m venv .venv
$env:PYTHONUTF8 = '1'
$env:PYTHONIOENCODING = 'utf-8'
& .\.venv\Scripts\python.exe -m pip install -r portfolio_task3/requirements-lock.txt
& .\.venv\Scripts\python.exe -m ipykernel install --user --name cos40007-task3 --display-name 'Python 3.12 (Portfolio 3)'
Set-Location portfolio_task3
```

Open the notebook with a Jupyter-compatible editor, choose that kernel, then
Restart Kernel and Run All. Run from `portfolio_task3/`; all paths are relative.
The notebook regenerates results, figures and trained model artifacts. It requires
no internet access after dependencies are installed. Run `python run_notebook.py` to execute every cell in a fresh kernel, or
`python verify_artifacts.py` for an independent inference-only audit.

`requirements.txt` lists direct dependencies. `requirements-lock.txt` records the
exact working package set. Training uses deterministic TensorFlow operations,
seed 42, CPU threads limited to two and oneDNN disabled. Different operating
systems or numerical libraries can still produce small numerical differences.

## Evaluation

The stratified split reproduces Portfolio 2 and is a previously inspected
benchmark, not untouched external validation. Traditional models use five-fold
stratified development CV with fold-local scaling. ANN trials use a fixed 20%
development validation reserve with a fit-only scaler. Configuration and epoch
choices are frozen before final test inference. All final models train on the
same common-scaled 7,000 rows. Trial curves and final-refit results are labelled
separately. See the notebook and `IMPLEMENTATION_PLAN.md` for the full protocol.

## Assistance and submission status

This working implementation was generated and executed with OpenAI Codex.
`ASSISTANCE_LOG.md` describes the actual scope; no student-authorship or personal
learning claims are invented. The brief limits GenAI code use; this generated
implementation must not be described as meeting that restriction without the
instructor's guidance. The student-requested deferred learning reflection,
Canvas deadline and accepted submission fields are recorded as TBD in
`SUBMISSION_TODO.md`. No Canvas submission is claimed.

Dataset attribution and licence: [data/README.md](data/README.md).
