---
topic: machine_learning
subtopic: bias_variance
difficulty: medium
source_name: Claude-assisted study notes
source_url: n/a
license: own work
---
The bias-variance tradeoff describes two sources of error that pull in opposite
directions as model complexity changes. Bias is error from overly simple
assumptions: a high-bias model misses real patterns and underfits, scoring poorly on
both training and validation data. Variance is error from sensitivity to the
particular training sample: a high-variance model fits noise and overfits, scoring
well on training data but poorly on new data. For squared error, the expected
prediction error splits into bias squared, variance and irreducible noise, which no
model can remove. Making a model more complex usually lowers bias but raises
variance, so the goal is a balance that minimizes total error on unseen data.
Typical interview points: how to diagnose each case (high bias shows a high error
on both sets, high variance shows a large gap between them), how learning curves
reveal which problem you have, and the fixes. For high bias, use a more flexible
model or better features. For high variance, add data, use regularization, or use
ensembling such as bagging. Examples: linear regression on curved data has high
bias, while a deep unpruned decision tree has high variance. A common pitfall is
adding more data to a high-bias model, which does not help.