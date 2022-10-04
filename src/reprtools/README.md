# [reprtools](https://www.pythonmorsels.com/exercises/67ab93799a034b76b53395569f218340)

### My notes

### Usage
Run the tests with:
- For all tests: `python -m pytest src/reprtools`.
- For only the base exercise: `python -m pytest src/reprtools -m "not (bonus1 or bonus2 or bonus3)"`
- For the base exercise and the first bonus: `python -m pytest src/reprtools -m "not (bonus2 or bonus3)"`

Run the main file with `python src/reprtools/reprtools.py`.

### Description:
#### Base problem
I'd like you to make a series of helper utilities for implementing the `__repr__` method for Python classes.

At first I'd like you to make a format_arguments function which accepts any positional and keyword arguments and returns a programmer-readable string representation of them.

```python
>>> print(format_arguments(1, 2, 3))
1, 2, 3
>>> print(format_arguments("expenses.csv", mode="wt", encoding="utf-8"))
'expenses.csv', mode='wt', encoding='utf-8'
```
This utility function might seem silly, but it will be useful in later bonuses.

#### Bonus 1
For the first bonus, I'd like you to create a make_repr function which will accept `args` and `kwargs` attributes and will return an appropriate `__repr__` method for the class it's attached to:

```python
>>> class Point:
...     def __init__(self, x, y, color='purple'):
...         self.x, self.y = x, y
...         self.color = color
...     __repr__ = make_repr(args=['x', 'y'], kwargs=['color'])
...
>>> Point(1, 2)
Point(1, 2, color='purple')
>>> Point(x=3, y=4, color='green')
Point(3, 4, color='green')
```
This make_repr function should assume that the strings provided in the `args` and `kwargs` lists represent valid attribute names.

#### Bonus 2
For the second bonus, I'd like you to create an `auto_repr` class decorator which accepts `args` and `kwargs` arguments and adds an appropriate `__repr__` method to the decorated class:

```python
>>> @auto_repr(args=['x', 'y'], kwargs=['color'])
... class Point:
...     def __init__(self, x, y, color='purple'):
...         self.x, self.y = x, y
...         self.color = color
...
>>> Point(1, 2)
Point(1, 2, color='purple')
>>> Point(x=3, y=4, color='green')
Point(3, 4, color='green')
```
#### Bonus 3
For the third bonus, I'd like you to allow your `auto_repr` class decorator to called on the class directly (with no arguments given).

In this case auto_repr should derive an appropriate string representation based on the attributes found on each class instance and the arguments accepted by the `__init__` method.

```python
>>> @auto_repr
... class Point:
...     def __init__(self, x, y, color='purple'):
...         self.x, self.y = x, y
...         self.color = color
...
>>> Point(1, 2)
Point(x=1, y=2, color='purple')
>>> Point(x=3, y=4, color='green')
Point(x=3, y=4, color='green')
```
All arguments in the string representation should be keyword arguments.

Note that if attributes are not found on an object and they have a default value, the string representation should leave them out:

```python
>>> @auto_repr
... class BankAccount:
...     def __init__(self, balance=0, account_name=None):
...         self._balance = balance
...         self.opening_balance = balance
...         self.name = account_name
...     @property
...     def balance(self):
...         return self._balance
...
>>> BankAccount()
BankAccount(balance=0)
```
Note that `opening_balance`, `name`, and `_balance` attributes are not included as arguments because they don't appear in the arguments accepted by `__init__` (at least not spelled exactly the same way).

The balance property was included though because it corresponds to the balance argument accepted by `__init__`.

Also note that `account_name` isn't included because no corresponding attribute was found and `account_name` has a default value.

If an argument is required by `__init__` and no corresponding attribute is found a `TypeError` exception should be raised:

```python
>>> @auto_repr
... class Point:
...     def __init__(self, x, y):
...         self.coordinates = (x, y)
...
>>> print(Point(5, 6))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'Point' object has no attribute 'x'
```
This `auto_repr` function obviously has its limitations, but a decorator like it might be handy in cases where you're writing a class (which isn't a dataclass) and need a quick string representation.
