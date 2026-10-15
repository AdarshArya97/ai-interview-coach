---
topic: python
subtopic: async_basics
difficulty: medium
source_name: Claude-assisted study notes
source_url: n/a
license: own work
---
Asynchronous programming in Python lets a single thread handle many waiting tasks at
once, which suits I/O-bound work such as network calls, database queries and file
reads. The asyncio library runs an event loop that switches between coroutines. A
coroutine is defined with async def, and the await keyword pauses it until a result
is ready, letting the loop run other tasks in the meantime. Calling a coroutine
function does not run it; it returns a coroutine object that must be awaited or
scheduled. asyncio.gather runs several coroutines concurrently, and asyncio.run
starts the event loop from regular code. Async code is concurrent but not parallel:
only one task runs at a time, so it does not speed up CPU-bound work. Typical
interview points: the difference between threading, multiprocessing and asyncio
(threads for blocking I/O, processes for CPU work, asyncio for many lightweight I/O
tasks), what the event loop does, why a blocking call like time.sleep freezes every
task (use asyncio.sleep instead), and what happens if you forget await. In machine
learning systems, async is common in serving APIs, such as FastAPI endpoints, and in
sending many LLM or embedding requests at the same time. A common pitfall is
calling blocking code inside a coroutine, which stalls the whole event loop.