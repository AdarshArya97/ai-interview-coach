---
topic: python
subtopic: oop
difficulty: medium
source_name: Claude-assisted study notes
source_url: n/a
license: own work
---
Object-oriented programming in Python organizes code into classes, which bundle data
(attributes) and behavior (methods) into objects. The four core ideas are
encapsulation, inheritance, polymorphism and abstraction. Encapsulation keeps
internal state behind a clean interface; Python uses naming conventions such as a
leading underscore instead of strict private fields. Inheritance lets a child class
reuse and extend a parent class, and super() calls the parent's methods. Python
supports multiple inheritance and resolves method lookup using the method
resolution order (MRO). Polymorphism means different classes can be used through the
same interface, which Python often achieves through duck typing: if an object has
the needed method, it works. Abstraction can be enforced with the abc module and
abstract base classes. Typical interview points: the difference between instance,
class and static methods, what __init__ does compared to __new__, what dunder
methods like __repr__ and __len__ are for, how @property controls attribute access,
and the difference between composition and inheritance. In machine learning code,
OOP appears everywhere: a model class with fit and predict methods, custom datasets
and data loaders, and scikit-learn style estimators. A common pitfall is using a
mutable default argument, such as a list, in a method signature, which is shared
across calls.