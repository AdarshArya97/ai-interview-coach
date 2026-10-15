---
topic: llm_rag
subtopic: chunking
difficulty: medium
source_name: Own study notes
source_url: n/a
license: own work
---

Chunking is the process of dividing a large document into smaller, meaningful pieces before storing it in a retrieval-augmented generation (RAG) system. When a user asks a question, the retriever searches these chunks and selects the most relevant information instead of passing the entire document to the language model.

Fixed-size chunking divides text according to a specified number of characters or tokens. It is simple to implement but may split sentences or concepts across boundaries. Overlapping chunking allows adjacent chunks to share some text, helping preserve context. Structure-aware chunking divides documents using headings, paragraphs, lists, or sections so that related information stays together.

Chunk size involves a trade-off. Small chunks provide precise retrieval but may lack sufficient context. Large chunks preserve more context but can contain irrelevant information and consume more of the model's context window. The appropriate size depends on document structure, query types, and retrieval performance.

Each chunk should store metadata such as its source filename, heading, chunk index, topic, and source URL when available. This metadata helps the system identify where retrieved information originated and display useful citations.

For a RAG-based interview preparation platform, chunking technical notes into focused sections allows the system to retrieve explanations about specific concepts, such as Python generators or machine-learning overfitting. Chunking strategies should be evaluated using representative questions to determine whether retrieved chunks contain enough relevant information to generate accurate answers.