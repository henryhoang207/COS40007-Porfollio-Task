# GenAI assistance record

## 1. GenAI Tools Used

OpenAI Codex desktop assistant (GPT-6-based runtime; exact model version not
exposed). Used to inspect prior notebooks and the plan, prepare the Python
environment, generate this working notebook and supporting verification code,
run experiments, debug failures, interpret measured outputs, prepare the report,
and perform incremental Git commits and pushes.

This describes code generation and execution, beyond debugging-only assistance.
The work is not represented as independently written or personally verified by
the student. The source brief's narrower GenAI allowance is recorded in
`SUBMISSION_TODO.md` for student/instructor resolution.

## 2. Specific Tasks & Prompts

Task 1 - Plan execution. Exact user prompt:

> "C:\Users\hoanh\OneDrive\Tài liệu\CS material\COS40007\Portfollio_Task3\Portfolio_Task3_End_to_End_Plan.md"
>
> Follow this plan end to end, with verification between each phase and push to github.

Task 2 - Defer student-only information. Exact user reply:

> Record this part in .md files as TBD

That reply addressed a request for the current Canvas deadline, accepted
submission files and the student's own learning reflection.

Earlier portfolios and the supplied plan predate this execution request. Their
assistance histories are not reconstructed or attributed to this session.

Task 3 - Audit and Word explanation. The user supplied the Part A-D task text
and two rubric images, asked to verify current coverage and the maximum rubric
band, and requested a DOCX with a brief Part A, in-depth Part B, comparison
visualisations and screenshot placeholders with exact capture instructions.
The user subsequently instructed: "continue".

Codex used the Documents skill to create the explanation and rubric review,
analysed saved predictions for a supplementary classification probability
scatter, and updated the audit and submission notes. The code, model settings,
notebook and existing measured outputs were not changed. This documentation
work was AI-drafted; no student learning experience was invented.

Task 4 - Insert figures and editable notebook content. Exact user request:

> Insert existing figures directly into word. Reproduce the notebooks table and model summary as editable word content as needed

Codex edited the current Word document in place, preserving the original report
and its local formatting in a temporary backup. Six original result PNGs were
embedded without image generation. Dataset audit, split shapes, traditional CV
and test metrics, ANN layer summary, pilot/trials and class-level/aggregate
classification reports were reproduced or expanded as editable Word tables.
The existing editable master results were retained. Only S04, S11 and S15 remain
as manual evidence screenshot placeholders. Personal fields remain TBD.

## 3. Code Attribution only for debugging and helping find errors

The mandatory template heading is retained verbatim. Actual assistance was broader:

- Notebook setup, data audit, splits, traditional CV, ANN development, final refits,
  evaluation, export and reload: AI-generated implementation and execution.
- Notebook interpretations and report: AI-drafted using actual experiment outputs.
- Dependency setup: diagnosed Windows console Unicode logging errors; subsequent
  verification uses UTF-8 environment settings.
- Verification and packaging helpers: AI-generated and executed.

Additional actual debugging findings are appended when they occur.

## 4. Learning Reflection

Personal responses are intentionally deferred by the user. The three required
questions and their TBD entries are in `SUBMISSION_TODO.md`. No personal learning
statement has been written on the student's behalf.

- Notebook pre-execution review: corrected nested-string quoting and a Windows-path escape in the report cell; compiled all ten analysis cells successfully.
- Environment setup: moved the active clean environment outside OneDrive after slow installation; no model results were produced before setup verification.

- Execution harness: an orchestration timeout interrupted the initial setup kernel before any model training; setup was restarted. Long-running jobs are now launched asynchronously with durable logs.

- Phase coordination: propagated child-process UTF-8 settings after a Windows path could not be printed. The notebook had been saved successfully; data checks then ran once and passed.
- Report verification: rendered and visually inspected all four pages, including tables, curves, confusion matrices, headings and footers; verified clickable repository URI annotations.

- Independent verification startup: restarted during initial imports with bytecode cache writes disabled; no model settings or notebook analysis code changed.

- Packaging audit: found Git line-ending conversion changed the bytes of three SHA-256-checked files. Added targeted .gitattributes rules and verified staged blobs match the original dataset, frozen settings and model metadata byte for byte. Model settings and numeric data values were unchanged.

- Final staged-file check identified that the ASCII-encoded PDF was being treated as text. Declared PDF, model, history and figure exports as binary in .gitattributes so their byte offsets and hashes are preserved. No exported artifact bytes were edited.

- Final verification: a clean-environment full run executed all ten code cells without error outputs and reproduced CV, ANN development, final metrics and predictions. A fresh GitHub clone also passed hashes, PDF-byte comparison and independent inference checks on all 3,000 test rows for every exported model.

- Word audit: the independent saved-model reload check passed again. The supplied
  rubric has seven scored criteria totalling 68; the overlapping architecture
  row was counted once. Classification/MLP alternatives were applied correctly,
  and the outstanding authorship issue was retained separately from technical
  rubric coverage.
- Document preparation: output files were saved successfully, but an initial
  console print could not encode the decomposed Unicode workspace path. UTF-8
  logging corrected this; no experiment or artifact content changed because of
  that logging error.
- Document preview: the canonical renderer could not find its LibreOffice
  runtime. A hidden Word instance exported the document for QA; a cleanup-call
  argument was corrected. The preview PDF and page images are temporary QA
  files outside the repository, not additional submission deliverables.
- Final Word QA: inspected all 13 rendered pages at 150 dpi. Removed an inherited
  title rule and rechecked the final first page; pages 2-13 were pixel-identical
  to the inspected render. Checked all 15 screenshot slots, 11 repeated-header
  tables, repository links, figure sources and notebook cell references. The
  original notebook, recipes and measured results remain unchanged.
- Publication QA: a fresh filtered GitHub clone verified the documentation
  commit and exact published Word and supporting PNG bytes, plus the audit and
  local-verification records. The publication evidence is appended to
  `results/word_report_verification.json` in a separate verification commit.
- Figure-insertion QA: rendered and visually inspected all 17 pages at 150 dpi.
  Verified six embedded image byte streams match their original PNGs exactly,
  all 12 tables are native Word tables, the ANN summary retains 3410 parameters,
  and only three manual evidence placeholders remain. The existing executable
  notebook, model artifacts and numerical results were not edited or retrained.
