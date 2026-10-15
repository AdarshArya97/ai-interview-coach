---
topic: deep_learning
subtopic: activation_functions
difficulty: easy
source_name: Own study notes
source_url: n/a
license: own work
---
An activation function transforms a neuron's weighted input, usually after the weighted sum and bias have been calculated. It introduces non-linearity, allowing a neural network to learn complex patterns; without nonlinear activations, stacking ordinary linear layers is still equivalent to a single linear transformation. ReLU (Rectified Linear Unit) returns zero for negative inputs and the input itself for positive inputs, making it efficient and widely used in hidden layers. Sigmoid maps values to the range 0 to 1 and is often used for binary-classification output probabilities, although it can cause vanishing gradients in deep networks. Tanh maps values to -1 to 1 and is zero-centered, but can also saturate. Softmax converts a vector of scores into values that sum to 1 and is commonly used for mutually exclusive multi-class classification. GELU and SiLU are smooth activations often used in modern deep-learning architectures. The appropriate activation depends on the task, architecture, and output interpretation.
