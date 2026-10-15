---
topic: python
subtopic: data_structures
difficulty: easy
source_name: Claude-assisted study notes
source_url: n/a
license: own work
---
Python's four core built-in data structures are the list, tuple, dictionary and set,
and each is chosen for a different job. A list is an ordered, mutable sequence: index
access and append are fast, but searching for a value or inserting at the front
takes linear time. A tuple is ordered and immutable, so it works as a fixed record
and can be used as a dictionary key. A dictionary maps hashable keys to values and
keeps insertion order since Python 3.7. A set holds unique hashable items and
supports union, intersection and difference. Dictionaries and sets are built on hash
tables, so lookup, insert and delete take constant time on average, while checking
membership in a list takes linear time. Typical interview points: why a list cannot
be a dictionary key (it is mutable, so unhashable), how to remove duplicates while
keeping order (dict.fromkeys), when to use collections.deque instead of a list for a
queue (fast pops from both ends), and what happens when you modify a list while
looping over it (items get skipped). In machine learning code, this choice affects
how fast large datasets can be deduplicated, indexed and joined, so picking the
right structure is a practical skill and not only theory.