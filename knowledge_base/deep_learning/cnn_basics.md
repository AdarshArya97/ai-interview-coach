---
topic: deep_learning
subtopic: cnn_basics
difficulty: medium
source_name: Own study notes
source_url: n/a
license: own work
---
A Convolutional Neural Network (CNN) is a neural architecture designed to learn spatial patterns, especially in images. A convolutional layer applies learnable filters, also called kernels, across local regions of an input to create feature maps. Early layers may detect edges and textures, while deeper layers can learn more complex shapes and object parts. Weight sharing means the same filter is reused across positions, reducing the number of parameters compared with a fully connected layer over the whole image. Stride controls how far a filter moves at each step, while padding controls how borders are handled and influences output dimensions. Activation functions such as ReLU add non-linearity. Pooling layers, such as max pooling, can reduce spatial dimensions, although some modern CNNs use strided convolutions instead. Later layers combine learned features to perform tasks such as image classification, object detection, and segmentation. CNNs are effective for visual data because their local connectivity and shared filters exploit spatial structure.
