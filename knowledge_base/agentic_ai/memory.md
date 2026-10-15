---
topic: agentic_ai
subtopic: memory
difficulty: medium
source_name: Own study notes
source_url: n/a
license: own work
---
Memory in an AI agent is information retained or retrieved to help it respond consistently across steps or sessions. Short-term memory usually contains the current conversation, task state, and recent observations. Long-term memory stores information that may be useful later, such as user preferences, past tasks, or previously learned facts. Long-term memory can be implemented using a database, searchable documents, or a vector store that retrieves semantically relevant information through embeddings. A memory system should decide what to save, how to update outdated facts, and which memories are relevant to the current request. Storing every interaction can increase cost and surface irrelevant or sensitive information, so memory should be selective and subject to appropriate privacy controls. Retrieved memories are context, not automatically verified truth; an agent should account for source quality and possible conflicts. Memory is distinct from the model's parameters: external memory can be updated without retraining the model. Good memory improves continuity but does not guarantee correctness.
