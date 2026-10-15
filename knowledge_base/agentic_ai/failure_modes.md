---
topic: agentic_ai
subtopic: failure_modes
difficulty: medium
source_name: Own study notes
source_url: n/a
license: own work
---
AI agents can fail in ways that go beyond ordinary incorrect text generation because they may plan multiple steps, call tools, and act on external systems. Common failure modes include hallucinated facts, selecting the wrong tool, generating invalid arguments, misinterpreting tool results, repeating actions in loops, losing track of the goal, and stopping before the task is complete. An agent may also rely on stale memory, mishandle conflicting evidence, or treat malicious instructions in retrieved documents as trusted commands. Tool failures such as rate limits, network errors, and timeouts can interrupt a workflow. Mitigations include schema validation, bounded retries, step and cost limits, checkpoints, explicit success criteria, source verification, and structured logging. Idempotent operations help prevent duplicate effects when a tool call is retried. High-impact actions should use approval gates, and systems should provide a safe fallback when they cannot complete a task reliably. Evaluation should test complete workflows, not just individual model responses, using realistic tasks and known failure cases.
