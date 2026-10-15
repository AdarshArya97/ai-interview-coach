---
topic: machine_learning
subtopic: overfitting
difficulty: medium
source_name: Own study notes
source_url: n/a
license: own work
---
Overfitting happens when a model learns the noise and quirks of its training data
instead of the underlying pattern. It scores very well on the training set but
noticeably worse on data it has not seen. Typical signs are a large gap between
training and validation accuracy, and a validation loss that starts rising while
training loss keeps falling. Common remedies include collecting more data, using a
simpler model, adding regularization such as L2 penalties or dropout, stopping
training early, and using cross-validation to get a more honest estimate of
performance. Typical interview points: how to detect overfitting (compare training
and validation metrics, plot learning curves), why a very complex model on a small
dataset overfits, how data augmentation and feature selection help, and how
overfitting differs from underfitting, where the model is too simple and scores
poorly on both training and validation data. A common pitfall is tuning
hyperparameters repeatedly against the test set, which leaks information and makes
the final score look better than real-world performance.