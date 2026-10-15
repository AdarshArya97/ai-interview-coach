---
topic: llm_rag
subtopic: evaluation_of_rag
difficulty: medium
source_name: Own study notes
source_url: n/a
license: own work
---

Evaluation of Retrieval-Augmented Generation (RAG) is the process of measuring how effectively a system retrieves relevant information from a knowledge base and uses that information to generate accurate, relevant, and well-supported answers. A RAG system should be evaluated at both the retrieval stage and the answer-generation stage because a failure in either stage can reduce the quality of the final response.

Retrieval evaluation measures whether the system finds the correct information for a given query. One important metric is Recall@k, which measures the proportion of relevant documents or chunks found among the top k retrieved results. Mean Reciprocal Rank (MRR) measures how highly the first relevant result appears in the ranked list. Precision@k measures the proportion of the top k retrieved results that are relevant. Higher retrieval quality generally means that the language model receives more useful context.

Generation evaluation measures the quality of the answer produced using the retrieved context. Important dimensions include answer correctness, relevance, completeness, faithfulness to the retrieved context, and clarity. Faithfulness measures whether the answer is supported by the supplied context rather than containing unsupported claims. An answer can be fluent and relevant but still be incorrect or ungrounded, so language quality alone is not enough.

RAG evaluation can use a prepared dataset containing representative questions, expected answers, and relevant source documents or chunks. Each question is run through the system, and the retrieved results and generated answer are compared with the expected evidence and answer. Human reviewers can assess correctness and usefulness, while automated metrics or an LLM-based evaluator can help scale the evaluation. Automated evaluations should be checked against human judgments because evaluators can also make mistakes.

A useful evaluation dataset should include different question types, such as direct factual questions, questions requiring multiple pieces of evidence, questions with ambiguous wording, and questions whose answers are not available in the knowledge base. The system should be tested for its ability to acknowledge missing information instead of inventing an answer. Evaluation should also be repeated after changes to chunking, embedding models, retrieval settings, reranking, or prompts.

For the PrepPilot AI interview platform, RAG evaluation can test whether a candidate's question retrieves the correct technical concepts, role-specific interview questions, model answers, and grading rubrics. For example, a question about database indexing should retrieve relevant database material rather than unrelated content about operating systems. The generated explanation or interview question should be grounded in the retrieved material and consistent with the selected job role and difficulty level.

A practical evaluation workflow is to create a small test set of representative questions, identify the expected relevant chunks, measure retrieval performance, inspect the generated answers for correctness and faithfulness, record failures, and adjust the RAG pipeline. This makes it possible to compare system versions objectively instead of relying only on a few successful demonstrations.