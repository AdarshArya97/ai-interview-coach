---
topic: machine_learning
subtopic: class_imbalance
difficulty: medium
source_name: Claude-assisted study notes
source_url: n/a
license: own work
---
Class imbalance occurs when one class has far more examples than another, such as
fraud detection where only 1 percent of transactions are fraudulent. A model can
reach 99 percent accuracy by always predicting the majority class while being
useless for the rare class that matters. The first fix is to use better metrics:
precision, recall, F1, and PR-AUC instead of accuracy. Common techniques fall into
three groups. Data-level methods resample the training set: random oversampling
duplicates minority examples, undersampling removes majority examples, and SMOTE
creates synthetic minority examples by interpolating between neighbors. Algorithm-level
methods change the loss, for example with class weights (class_weight="balanced" in
scikit-learn) that make mistakes on the minority class cost more. Threshold tuning
moves the decision threshold away from 0.5 to trade precision against recall.
Typical interview points: why accuracy is misleading, when to choose oversampling
versus class weights, and what the risks of SMOTE are. A common pitfall is applying
resampling before splitting the data, or inside the validation folds, which leaks
information and inflates scores. Resample only the training portion, keep the
validation and test sets at their natural class distribution, and use stratified
splits so each fold contains minority examples.