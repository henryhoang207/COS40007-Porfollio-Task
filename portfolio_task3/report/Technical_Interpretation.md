### Which tested model performed best?

ANN-2 had the highest observed test accuracy (96.57%), weighted F1 0.9655, balanced accuracy 95.80%, macro-F1 0.9625, and unstable recall 98.59%. It misclassified 27 unstable cases as stable. This is an observed benchmark ranking, separate from development-only epoch selection.

### How did architecture choices affect performance?

The required 64/32/16 dense layers and ReLU can represent nonlinear interactions; the two 0.2 dropout layers regularise training, while Softmax and sparse crossentropy match the two integer-coded classes. Early stopping restricts validation deterioration, and LR reduction permits smaller updates when validation loss stalls. All core widths were held fixed, so these experiments do not establish optimal widths or isolate a causal dropout effect. The controlled batch comparison gave best validation losses of 0.1055 (16), 0.1070 (32) and 0.1080 (64). The curves show the observed fit/validation trajectories; dropout is active only during fit. Changing batch size also changes the number of updates per epoch, so equal epoch caps are not equal update budgets. Final refits use fixed LR and selected epoch counts, rather than replaying the development callbacks.

### Did deep learning outperform the traditional models, and why?

The higher-scoring core ANN (ANN-2, 96.57%) outperformed the higher-scoring traditional classifier (MLP, 96.47%) by +0.10 percentage points. Their weighted F1 scores were 0.9655 and 0.9646; unstable-as-stable counts were 27 and 50. Smooth nonlinear boundaries may favour neural networks over axis-aligned tree splits, but that is a possible explanation, not a tested mechanism. MLP is itself a neural network; its comparison with Keras also changes regularisation, training implementation, batch size and stopping. A single split and seed cannot attribute the difference to one factor.

### What would more time improve?

Repeat development trials over several seeds; use bounded inner-CV tuning for widths, regularisation and learning rate; compare calibrated probabilities and development-chosen cost-sensitive thresholds; and investigate errors near the simulated stability boundary. Any feature-engineering extension should remain development-only and separately labelled. Keep an independent external dataset for a final check. Neither test-based tuning nor additional unreported searches would be a defensible improvement.

### Would this be deployed in production?

No. These are simulated configurations from one fixed grid setting, with a previously inspected benchmark test split. Real measurement noise, network topologies and operating distributions can shift. Calling an unstable case stable can be costly; deployment needs external field validation, engineering review of error costs, calibration, monitoring, conservative fallback behaviour and comparison with physical safety analyses. High assignment accuracy does not demonstrate production readiness.

### Metric trade-offs

MLP has the highest balanced accuracy (96.12%), while ANN-1 has the fewest unstable-as-stable errors (23). ANN-2 exceeds MLP by only 3 correct test cases. Different error costs can therefore favour different configurations.