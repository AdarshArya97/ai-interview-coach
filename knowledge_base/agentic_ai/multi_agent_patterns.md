---
topic: agentic_ai
subtopic: multi_agent_patterns
difficulty: medium
source_name: Own study notes
source_url: n/a
license: own work
---
A multi-agent system uses multiple specialized agents that cooperate to complete a task. Each agent may have a distinct role, such as planner, researcher, writer, reviewer, or verifier. In a supervisor pattern, one coordinator delegates work to specialist agents and combines their results. In a sequential pattern, one agent's output becomes the next agent's input. In a parallel pattern, several agents work on independent subtasks at the same time, after which their results are aggregated. A reviewer pattern adds an agent that checks another agent's work and requests revisions when needed. Multi-agent designs can improve modularity and allow tasks to be divided, but they are not automatically better than a single agent. Coordination adds latency, token cost, communication complexity, and more opportunities for errors or conflicting outputs. Each agent should have a clear responsibility, a defined input and output, and limited permissions. The system should also define how disagreements are resolved, when to retry, and when the overall workflow should stop.
