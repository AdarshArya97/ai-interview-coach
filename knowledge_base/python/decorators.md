---
topic: python
subtopic: decorators
difficulty: medium
source_name: Claude-assisted study notes
source_url: n/a
license: own work
---
A decorator is a function that takes another function and returns a new function,
usually adding behavior before or after the original runs without changing its code.
The @decorator syntax above a function definition is shorthand for
func = decorator(func). Decorators work because functions are first-class objects in
Python: they can be passed around, returned and stored in variables. Most decorators
define an inner wrapper function that accepts *args and **kwargs, calls the original
function, and returns its result. Common uses are logging, timing, caching,
authentication checks and retrying failed calls. Built-in examples include
@staticmethod, @classmethod, @property and functools.lru_cache. Typical interview
points: how a decorator works step by step, why functools.wraps should be used
inside the wrapper (it keeps the original function's name and docstring), how to
write a decorator that takes its own arguments (an extra outer function layer), and
how closures let the wrapper remember the original function. In machine learning
code, decorators are often used to time training steps, cache expensive feature
computations, or register models and tasks in a framework. A common pitfall is
forgetting to return the wrapper's result, which makes the decorated function
return None.