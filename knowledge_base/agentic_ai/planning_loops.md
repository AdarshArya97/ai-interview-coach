---
topic: agentic_ai
subtopic: planning_loops
difficulty: medium
source_name: Own study notes
source_url: n/a
license: own work
---
A planning loop is an iterative process in which an AI agent decides what to do, takes an action, observes the result, and then chooses the next step. A common pattern is plan, act, observe, and revise. For example, a research agent may break a broad question into smaller searches, inspect the returned sources, identify missing information, and run additional searches before producing a summary. Unlike a single prompt that produces one response, a planning loop can adapt to intermediate results. The loop needs a clear goal, access to suitable tools, and a stopping condition such as task completion, a step limit, a time limit, or a budget limit. Without boundaries, an agent may repeat actions, waste tokens, or become stuck in a cycle. Good systems track progress, check whether each action contributes to the goal, handle tool failures, and stop safely when confidence is low or required information is unavailable. Planning can be performed by the model dynamically or guided by a predefined workflow.
