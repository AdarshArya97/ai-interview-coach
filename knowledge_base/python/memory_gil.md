---
topic: python
subtopic: memory_gil
difficulty: hard
source_name: Claude-assisted study notes
source_url: n/a
license: own work
---
CPython manages memory automatically using reference counting: every object tracks
how many references point to it, and it is freed when that count reaches zero.
Reference counting cannot free objects that reference each other in a cycle, so a
cyclic garbage collector also runs periodically to clean those up. Variables are
names bound to objects, so assignment copies a reference, not the object; this is
why modifying a list through one name changes it through all names. The Global
Interpreter Lock (GIL) is a mutex in standard CPython that lets only one thread run
Python bytecode at a time. It keeps reference counting safe and simple, but it means
threads do not give real parallelism for CPU-bound code. Threads still help with
I/O-bound work, because the GIL is released while waiting. For CPU-bound work, use
multiprocessing, which gives each process its own interpreter and memory, or use
libraries like NumPy whose C code releases the GIL. Recent Python versions offer an
optional free-threaded build without the GIL, but the standard build still has it.
Typical interview points: what the GIL is and why it exists, threads versus
processes, shallow versus deep copy, and how memory leaks happen through lingering
references. In machine learning, data loaders often use worker processes to avoid
the GIL. A common pitfall is expecting threads to speed up heavy computation.