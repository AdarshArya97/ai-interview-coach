---
topic: python
subtopic: generators_iterators
difficulty: medium
source_name: Claude-assisted study notes
source_url: n/a
license: own work
---
An iterator is any object that produces its values one at a time through the
__iter__ and __next__ methods, and raises StopIteration when it runs out. A for loop
works by calling iter() on an iterable and then calling next() repeatedly. A
generator is a simple way to build an iterator: a function that uses yield instead
of return. Each time it hits yield, it hands back a value and pauses, keeping its
local state until the next call. Generators are lazy, so values are computed only
when requested, and memory use stays small even for huge or infinite sequences. A
generator expression, such as (x * x for x in data), gives the same benefit as a
list comprehension without building the whole list. Typical interview points: the
difference between an iterable (can be looped over) and an iterator (tracks its own
position), why a generator can only be consumed once, how yield differs from return,
and when to prefer a generator over a list. In machine learning, generators are used
to stream training batches or read large files line by line without loading the
whole dataset into memory. A common pitfall is trying to loop over the same
generator twice, which gives an empty result the second time.