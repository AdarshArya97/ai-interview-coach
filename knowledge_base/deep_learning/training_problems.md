---
topic: deep_learning
subtopic: training_problems
difficulty: medium
source_name: Own study notes
source_url: n/a
license: own work
---
Neural-network training can fail or generalize poorly for several reasons. Overfitting occurs when a model fits training examples too closely and performs worse on unseen data; it can be reduced with more representative data, data augmentation, regularization, dropout, early stopping, or a smaller model. Underfitting occurs when a model cannot learn the training patterns well, often because it is too simple, insufficiently trained, or poorly configured. Vanishing gradients make updates to early layers very small, while exploding gradients create excessively large updates and unstable loss. ReLU-like activations, suitable initialization, normalization, residual connections, and gradient clipping can help with gradient problems. Data leakage occurs when information unavailable at prediction time, or information from validation or test data, accidentally enters training; it produces misleadingly strong evaluation results. Class imbalance can make accuracy deceptive when a model mostly predicts the majority class, so metrics such as precision, recall, F1-score, and PR-AUC may be more informative. A sound workflow uses separate training, validation, and test sets, checks learning curves, and evaluates on data representative of real use.
