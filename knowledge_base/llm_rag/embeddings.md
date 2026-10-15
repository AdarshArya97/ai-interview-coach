---
topic: llm_rag
subtopic: embeddings
difficulty: medium
source_name: Own study notes
source_url: n/a
license: own work
---

Embeddings are numerical representations of text that capture aspects of its semantic meaning. An embedding model converts text into a vector containing numbers. Texts with similar meanings often have vectors that are close to each other in the embedding space, even when they use different words. RAG systems use embeddings to retrieve information based on meaning rather than exact keyword matches alone.

During indexing, documents are divided into chunks, and an embedding model generates a vector for each chunk. The system stores these vectors alongside the original text and metadata. When a user submits a question, the same compatible embedding model converts the question into a vector. The retriever compares this query vector with stored vectors to find relevant chunks.

Common similarity measures include cosine similarity, dot product, and Euclidean distance. The appropriate measure depends on the embedding model and vector database configuration. A high similarity score indicates closeness according to the chosen measure, but it does not guarantee that a passage contains the correct answer.

The embedding model used for queries should be compatible with the model used to embed documents. Changing the embedding model may require generating new vectors for the entire knowledge base. Exact technical terms and identifiers can sometimes be retrieved more effectively through keyword search, making hybrid retrieval useful.

In an interview preparation platform, embeddings can represent technical explanations, interview questions, and preparation notes. The system can use them to retrieve relevant knowledge for a candidate's question. Retrieval quality should be tested using realistic queries rather than relying only on similarity scores.