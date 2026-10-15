---
topic: llm_rag
subtopic: prompting
difficulty: medium
source_name: Own study notes
source_url: n/a
license: own work
---

Prompting is the process of designing instructions and providing context to a Large Language Model (LLM) so that it produces useful, relevant, and appropriately formatted responses. A prompt can define the model's task, provide background information, specify constraints, describe the desired output, and explain how to handle missing information.

A well-designed prompt usually contains a clear task, relevant context, explicit instructions, and an expected output format. For example, asking a model to explain a programming concept is less specific than asking it to explain the concept for a beginner, provide a short example in Python, identify common mistakes, and finish with two interview questions.

In a Retrieval-Augmented Generation (RAG) system, the prompt often includes the user's question and the information retrieved from the knowledge base. The model is instructed to use the retrieved context as evidence for its answer, avoid unsupported claims, and acknowledge when the context does not contain enough information. Clear separation between instructions, retrieved content, and the user's question helps make the prompt easier to understand and maintain.

System instructions define the model's general role and behavioral constraints, while user prompts communicate the immediate task. Retrieved documents supply supporting information. These components should have clearly defined purposes. Retrieved text must be treated as reference data rather than as instructions that can override the system's rules, because external documents may contain irrelevant or malicious prompt-injection content.

Structured output instructions can improve consistency when a response will be processed by software. For example, an application may request a JSON object containing an answer, a list of supporting source identifiers, a confidence assessment, and any limitations. The application should validate the resulting structure because a model may produce invalid JSON or omit required fields despite the instruction.

Prompting strategies include zero-shot prompting, where the model receives instructions without examples; few-shot prompting, where examples demonstrate the desired response; and structured reasoning guidance, where a complex task is divided into clearly defined steps. The best strategy depends on the task, response requirements, latency, cost, and reliability needs.

Prompts should be tested with a representative collection of inputs, including normal requests, ambiguous questions, missing information, irrelevant retrieved context, and attempts to override instructions. Changes should be evaluated for correctness, consistency, relevance, and adherence to the required output format. A prompt that works for one example may fail on other inputs.

In the PrepPilot AI interview platform, prompting can help control resume analysis, interview question generation, follow-up questions, answer evaluation, and final reporting. For example, an answer-evaluation prompt can provide the candidate's response, the expected answer or grading rubric, the job role, and the required scoring criteria. It can instruct the model to return a score, evidence-based feedback, strengths, weaknesses, and suggestions for improvement.

A suitable interview-evaluation prompt should distinguish between the candidate's actual response and the reference answer. It should allow alternative technically correct approaches, avoid penalizing wording differences when the underlying concept is correct, and explain scores using the supplied rubric rather than arbitrary assumptions.

Effective prompting does not guarantee correctness by itself. It works best when combined with reliable retrieved information, explicit evaluation criteria, output validation, and systematic testing.