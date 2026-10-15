---
topic: llm_rag
subtopic: hallucination
difficulty: medium
source_name: Own study notes
source_url: n/a
license: own work
---

Hallucination in a Large Language Model (LLM) occurs when the model generates information that is false, fabricated, misleading, or unsupported by the available evidence. Hallucinations can sound confident and convincing, making them difficult to identify without checking the answer against reliable sources.

Hallucinations can occur because an LLM generates responses based on patterns learned during training rather than directly verifying every statement against facts. Other causes include incomplete context, ambiguous questions, irrelevant retrieved documents, outdated information, poorly designed prompts, and attempts to answer questions for which sufficient evidence is unavailable.

Retrieval-Augmented Generation (RAG) can reduce hallucinations by supplying relevant information from an external knowledge base. However, RAG does not eliminate hallucinations completely. If retrieval returns incorrect or incomplete information, or if the model ignores the supplied context, the generated answer may still be unreliable.

Several techniques can help reduce hallucinations. First, retrieve relevant and trustworthy documents before generating an answer. Second, instruct the model to answer using the supplied context and avoid unsupported claims. Third, allow the model to acknowledge when the available information is insufficient. Fourth, include source references where possible so that answers can be checked. Finally, evaluate responses against their supporting evidence and test the system with questions that have no answer in the knowledge base.

A useful distinction is between factual correctness and faithfulness. Factual correctness measures whether an answer agrees with reality or a trusted reference. Faithfulness measures whether the answer is supported by the context provided to the model. An answer can be faithful to an incorrect document while still being factually wrong, so reliable source material is also important.

In the PrepPilot AI interview platform, hallucinations could cause the system to provide incorrect technical explanations, invent interview requirements for a company, generate misleading model answers, or grade a candidate using criteria that were never defined. To reduce these risks, the platform should retrieve relevant interview material and grading rubrics, instruct the model to follow that evidence, and avoid presenting unsupported details as facts.

For example, if a candidate asks about a specific company's interview process and the knowledge base contains no verified information about that company, the system should clearly state that it cannot verify the company's process. It may offer general interview preparation advice, but it should distinguish general guidance from verified company-specific information.

Hallucination management is an ongoing process rather than a single setting. It requires reliable knowledge sources, effective retrieval, clear prompts, appropriate answer validation, and regular evaluation of incorrect or unsupported responses.