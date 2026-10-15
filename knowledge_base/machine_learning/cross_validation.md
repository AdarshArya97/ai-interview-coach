---
topic: machine_learning
subtopic: cross_validation
difficulty: medium
source_name: Claude-assisted study notes
source_url: n/a
license: own work
---
Cross-validation estimates how well a model will perform on unseen data by training
and testing it on several different splits of the dataset. In k-fold
cross-validation, the data is divided into k equal folds. The model is trained on
k minus 1 folds and validated on the remaining one, repeating until every fold has
been used for validation once, and the scores are averaged. This gives a more
reliable estimate than a single train-validation split, especially on small
datasets. Stratified k-fold keeps the class proportions the same in each fold, which
matters for imbalanced data. For time series, use a time-based split so the model
never trains on the future, because shuffling would leak information. Cross-validation
is also used to tune hyperparameters, and nested cross-validation separates tuning
from final evaluation. Typical interview points: why k is commonly 5 or 10, the cost
of training k models, how leave-one-out differs, and why a final held-out test set
is still useful. A common pitfall is data leakage, such as fitting a scaler or
imputer on the full dataset before splitting. Preprocessing should be fitted inside
each training fold only, for example with a scikit-learn Pipeline.