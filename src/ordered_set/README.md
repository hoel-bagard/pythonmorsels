## [OrderedSet exercise](https://www.pythonmorsels.com/exercises/168511e76186448a9ed337accc5029a2/)

- Initialise with an empty tuple instead of None:
```
    def __init__(self, data: Optional[Iterable] = None):
```
vs
```
    def __init__(self, data: Optional[Iterable] = ()):
```

- In Python 3.6 and above, dictionaries are ordered by default. Therefore using an `OrderedDict` is unecessary.
- Could inherit from `from collections.abc import Set` to have all the set operations (substractions, merge, equality, etc...).
- Or even from `from collections.abc import MutableSet` for even more "free" operations!
