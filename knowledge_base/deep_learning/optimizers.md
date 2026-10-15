---
topic: deep_learning
subtopic: optimizers
difficulty: medium
source_name: Own study notes
source_url: n/a
license: own work
---
An optimizer updates a neural network's trainable parameters using gradients computed during backpropagation. Its goal is to reduce the loss function over training. Stochastic Gradient Descent (SGD) updates parameters using gradients from individual examples or mini-batches. A learning rate controls the size of each update: if it is too large, training may become unstable; if too small, learning can be slow. Momentum accumulates a moving direction from past gradients, helping updates move more consistently. Adam combines momentum-like estimates of the gradient with adaptive estimates of squared gradients, giving each parameter an adjusted step size. Adam is a common default for many deep-learning tasks, while SGD with momentum can work very well in some computer-vision settings. AdamW separates weight decay from Adam's gradient update and is widely used for transformer training. An optimizer does not replace a loss function or backpropagation: the loss measures error, backpropagation calculates gradients, and the optimizer uses those gradients to update parameters. Learning-rate schedules and warm-up can further improve training.
