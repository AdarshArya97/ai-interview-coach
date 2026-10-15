---
topic: deep_learning
subtopic: transformers_and_attention
difficulty: medium
source_name: Own study notes
source_url: n/a
license: own work
---
Transformers are neural network architectures that use attention to model relationships between elements in a sequence. Unlike recurrent networks, transformers can process sequence positions in parallel during training, with positional information added because attention alone does not inherently encode token order. In self-attention, each token is projected into a query, key, and value vector. Query-key similarity scores determine how strongly a token attends to other tokens; these scores are scaled, normalized with softmax, and used to combine value vectors. Multi-head attention performs several attention operations in parallel so the model can learn different types of relationships. Feed-forward layers, residual connections, and normalization are also important transformer components. Encoder-style transformers are often used for understanding tasks, decoder-style models commonly generate text autoregressively, and encoder-decoder models support sequence-to-sequence tasks. In language models, token embeddings represent token identities as vectors, while positional information helps distinguish order. Transformers power many modern language models, but their attention computation can be expensive for long sequences.
