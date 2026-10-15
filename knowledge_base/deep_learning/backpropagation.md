---
topic: deep_learning
subtopic: backpropagation
difficulty: medium
source_name: Own study notes
source_url: n/a
license: own work
---
Backpropagation is the process neural networks use to calculate how much each parameter contributes to the prediction error. First, a forward pass sends input data through the network to produce a prediction. A loss function compares that prediction with the target. During the backward pass, the chain rule of calculus is applied from the output layer toward earlier layers to compute gradients of the loss with respect to weights and biases. An optimizer then uses these gradients to update the parameters and reduce the loss. Backpropagation calculates gradients; it does not itself choose the parameter updates. Common problems include vanishing gradients, where gradients become extremely small in early layers, and exploding gradients, where they become excessively large. Suitable activation functions, careful initialization, normalization, residual connections, and gradient clipping can help address these issues. Backpropagation is used in training many neural architectures, including multilayer perceptrons, convolutional neural networks, and transformers.
