---
topic: agentic_ai
subtopic: tool_calling
difficulty: medium
source_name: Own study notes
source_url: n/a
license: own work
---
Tool calling allows an AI model to request that an application execute a specific function or external tool, such as searching the web, querying a database, running code, or retrieving a document. The model typically returns a structured request containing the tool name and arguments. The surrounding application validates the request, executes the tool, and sends the result back to the model so it can decide what to do next. The model usually does not execute the tool by itself; the application or agent framework performs the actual operation. Tool descriptions and schemas help the model choose appropriate tools and supply correctly typed arguments. Robust implementations validate inputs, handle timeouts and errors, restrict permissions, and record tool calls for debugging. Tool calling is useful when a model needs current information, reliable calculations, access to private data, or actions beyond text generation. It also introduces risks: a tool may return untrusted content, an argument may be invalid, or an action may have side effects. Sensitive actions should require authorization or human confirmation, and tools should follow the principle of least privilege.
