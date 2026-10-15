---
topic: llm_rag
subtopic: retrieval_and_reranking
difficulty: medium
source_name: Own study notes
source_url: n/a
license: own work
---

Retrieval is the process of finding relevant information from a knowledge base in response to a user's query. In a Retrieval-Augmented Generation (RAG) system, the retrieved information is provided to a Large Language Model (LLM) so that it can generate an answer grounded in relevant source material. Retrieval quality is important because the model cannot reliably use information that the retrieval system fails to find.

Dense retrieval uses embeddings to represent queries and documents as numerical vectors. It compares the query vector with stored document vectors using a similarity measure, such as cosine similarity, to identify semantically related content. Dense retrieval can find relevant information even when the query and document use different words to express similar ideas.

Keyword-based retrieval matches words and terms in the query against the indexed documents. BM25 is a widely used ranking method that considers factors such as term frequency, document length, and how informative a term is across the document collection. Keyword retrieval can be especially useful for exact technical terms, programming language names, error messages, company names, and specific identifiers.

Hybrid retrieval combines dense retrieval with keyword-based retrieval. This approach can improve results when a question contains both semantic meaning and important exact terms. The results from different retrieval methods can be combined using a suitable ranking or fusion strategy, such as Reciprocal Rank Fusion (RRF), which combines rankings without requiring the original scores to share the same scale.

Reranking is a second-stage process that reorders an initial set of retrieved documents according to their relevance to the query. A retrieval system may first return a relatively large candidate set using a fast search method. A reranker then evaluates the query-document pairs more closely and places the most useful results near the top. Cross-encoder models are commonly used for reranking because they jointly process the query and a candidate document to estimate relevance.

The number of results retrieved is often controlled by a parameter called top-k. A small top-k may omit useful evidence, while a large top-k may introduce irrelevant context, increase processing costs, and consume more of the model's context window. The appropriate value depends on the knowledge base, query type, chunk size, and reranking strategy.

Metadata filtering can further improve retrieval by restricting results to appropriate categories. Metadata may include topic, difficulty, job role, company, document source, or content type. For example, a request for advanced Python interview questions can use metadata filters to prioritize Python-related content at the requested difficulty level before or during retrieval.

A typical retrieval and reranking pipeline includes receiving the user's query, applying any relevant metadata filters, retrieving candidate chunks using dense search, keyword search, or hybrid search, merging candidate rankings if necessary, reranking the candidates, selecting the most relevant chunks, and passing those chunks to the LLM with the original question. The generated answer should remain grounded in the selected context.

Retrieval quality should be evaluated using representative test questions and relevance judgments. Metrics such as Recall@k, Precision@k, and Mean Reciprocal Rank (MRR) help measure whether relevant information is retrieved and ranked appropriately. Comparing dense, keyword, and hybrid approaches can reveal which strategy works best for a particular knowledge base.

In the PrepPilot AI interview platform, retrieval and reranking can find relevant technical explanations, interview questions, reference answers, resume-improvement guidance, and grading rubrics. For example, when a candidate preparing for a backend developer role asks about REST API idempotency, hybrid retrieval can use semantic similarity to find relevant explanations while exact keyword matching helps locate documents containing terms such as PUT, PATCH, and idempotency. A reranker can then prioritize the chunks most useful for answering the question.

The goal is not simply to retrieve documents that share words with a query. It is to provide the LLM with accurate, relevant, and sufficient evidence to generate a useful answer while minimizing irrelevant context and unsupported claims.