---
topic: agentic_ai
subtopic: guardrails
difficulty: medium
source_name: Own study notes
source_url: n/a
license: own work
---
Guardrails are controls that help keep an AI agent within its intended scope, policies, and safety boundaries. They can validate user inputs, restrict which tools an agent may call, check tool arguments, filter or verify outputs, and require human approval for sensitive actions. Access controls should follow the principle of least privilege: an agent should receive only the permissions needed for its task. Structured schemas can reject malformed tool arguments, while allowlists can limit accessible tools, domains, files, or operations. Prompt instructions are useful but should not be the only safeguard because models can misunderstand instructions or be influenced by untrusted content. Retrieved documents and tool outputs should be treated as data rather than trusted instructions, helping reduce prompt-injection risk. Other controls include rate limits, execution budgets, audit logs, secret management, and monitoring. Guardrails should be tested against both normal and adversarial cases. They reduce risk but cannot guarantee that an agent will always behave correctly, so high-impact systems also need oversight, recovery procedures, and clear accountability.
