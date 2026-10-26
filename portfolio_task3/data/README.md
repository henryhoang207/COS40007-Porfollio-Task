# Dataset provenance

Arzamasov, V. (2018). *Electrical Grid Stability Simulated Data* [Dataset].
UCI Machine Learning Repository. [DOI: 10.24432/C5PG66](https://doi.org/10.24432/C5PG66).

[Dataset description and download](https://archive.ics.uci.edu/dataset/471/electrical+grid+stability+simulated+data).
Licensed under [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/).

`Data_for_UCI_named.csv` is copied unchanged from the existing Portfolio 2 dataset.
Its SHA-256 is recorded in `source_manifest.json` and rechecked in the notebook.
The file contains 10,000 configurations and 14 columns. Eleven original
predictors are used; `p1` is redundant, `stab` leaks the target, and `stabf` is
the target only. No rows or values in the included source CSV were changed.
