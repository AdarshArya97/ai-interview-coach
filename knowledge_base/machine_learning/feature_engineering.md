---
topic: machine_learning
subtopic: feature_engineering
difficulty: medium
source_name: Claude-assisted study notes
source_url: n/a
license: own work
---
Feature engineering is the process of turning raw data into inputs that help a model
learn better, and it often improves results more than changing the algorithm. Common
steps include handling missing values by imputing the mean, median or a constant,
encoding categorical variables with one-hot or ordinal encoding, and scaling numeric
features with standardization or min-max scaling. Skewed features can be reduced
with a log transform. New features can be created from existing ones, such as
interaction terms, ratios, counts, or date parts like day of week and month. Feature
selection removes irrelevant or redundant columns to cut noise and training time.
Typical interview points: which models need scaling (distance-based models, linear
models with regularization, and neural networks do; tree-based models mostly do
not), why one-hot encoding a high-cardinality column creates too many features,
what target encoding is and its leakage risk, and how to handle outliers. A common
pitfall is data leakage: fitting imputers, scalers or encoders on the full dataset
before splitting means information from the test data influences training. Fit
every transformation on the training data only, then apply it to validation and
test data, ideally inside a pipeline.