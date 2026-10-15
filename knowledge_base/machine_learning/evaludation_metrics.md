---
topic: machine_learning
subtopic: evaluation_metrics
difficulty: medium
source_name: Claude-assisted study notes
source_url: n/a
license: own work
---
Evaluation metrics measure how well a model performs, and the right one depends on
the problem. For classification, accuracy is the share of correct predictions, but
it is misleading when classes are imbalanced. Precision is the fraction of predicted
positives that are truly positive, TP / (TP + FP). Recall is the fraction of actual
positives the model finds, TP / (TP + FN). The F1 score is the harmonic mean of
precision and recall. ROC-AUC measures how well the model ranks positives above
negatives across all thresholds, while PR-AUC is often more informative when
positives are rare. For regression, common metrics are MAE, which is easy to
interpret and robust to outliers, RMSE, which penalizes large errors more, and R
squared, which shows the share of variance explained. Typical interview points: when
to favor precision (false alarms are costly, such as spam filtering) and when to
favor recall (misses are costly, such as disease screening), how changing the
decision threshold trades one for the other, why accuracy fails on a dataset with
99 percent negatives, and how to read a confusion matrix. A common pitfall is
reporting a single metric without considering the cost of each error type.