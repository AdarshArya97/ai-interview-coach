---
topic: machine_learning
subtopic: regularization
difficulty: medium
source_name: Claude-assisted study notes
source_url: n/a
license: own work
---
Regularization is any technique that discourages a model from becoming too complex,
so it generalizes better to unseen data. The most common form adds a penalty on the
size of the model's weights to the loss function. L2 regularization (ridge) penalizes
the squared weights, shrinking them toward zero without usually making them exactly
zero. L1 regularization (lasso) penalizes the absolute weights and can drive some
to exactly zero, which acts as automatic feature selection. Elastic net combines
both. The strength of the penalty is a hyperparameter, often called lambda or alpha;
a larger value means a simpler model and more risk of underfitting. In scikit-learn,
some models use C instead, which is the inverse of the regularization strength. In
neural networks, other forms include dropout, which randomly turns off units during
training, weight decay, and early stopping. Typical interview points: the
difference between L1 and L2 and when to choose each, why features should be scaled
before regularizing, how regularization trades a little bias for lower variance, and
how to choose the strength using cross-validation. A common pitfall is applying
regularization to unscaled features, which penalizes them unevenly.