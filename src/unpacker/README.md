# [Interleave](https://www.pythonmorsels.com/exercises/db5f9e6add674a26aa384c6fe302400c)

### My notes
- Use the `self.__dict__` instead of an instance variable dict. This way, the `__getattr__` and `__setattr__` are available for free.
  - If using that shortcut, then be careful to cast the original input into a dict (i.e. use `dict(input_dict)` and not `input_dict.copy()`). That's in case the input was an `OrderedDict`.
- Use `dict.update` + `zip` instead of a for loop to set multiple elements of a dict at once.

### Usage
Run the tests with:
- For all tests: `python -m pytest src/unpacker`.
- For only the base exercise: `python -m pytest src/unpacker -m "not (bonus1 or bonus2 or bonus3)"`
- For the base exercise and the first bonus: `python -m pytest src/unpacker -m "not (bonus2 or bonus3)"`

Run the main file with `python src/unpacker/unpacker.py`.

### Description:
#### Base problem
I'd like you to create an Unpacker class which (optionally) accepts an ordered dictionary as an argument. The given dictionary items should be retrievable and settable using either an attribute or a key syntax on the Unpacker object.

```python
>>> d = {'hello': 4, 'hi': 5}
>>> u = Unpacker(d)
>>> u['hello']
4
>>> u.hi
5
>>> u['hello'] = 8
>>> u.hello
8
```
You can assume that the given dictionary keys will be strings that represent valid attribute names.

I'd like attribute assignment on your object to work as expected:

```python
>>> u.hello = 5
>>> u.hello
5
```

#### Bonus 1
For the first bonus, I'd like you to make sure your Unpacker objects can be "unpacked" using multiple assignment. The unpacking should be in the order of assignment (assuming the given dictionary is ordered).

```python
>>> from collections import OrderedDict
>>> coordinates = OrderedDict([('x', 34), ('y', 67)])
>>> point = Unpacker(coordinates)
>>> x_axis, y_axis = point
>>> x_axis, y_axis
(34, 67)
```

#### Bonus 2
For the second bonus, I'd like you to make a nice string representation for your Unpacker objects.

```python
>>> row = Unpacker({'a': 234, 'b': 54})
>>> row['a'] = 11
>>> row['c'] = 45
>>> row
Unpacker(a=11, b=54, c=45)
```

#### Bonus 3
For third bonus I'd like you to allow getting and setting of multiple attributes using this key-lookup syntax:

```python
>>> row = Unpacker({'a': 234, 'b': 54})
>>> row['a', 'b']
(234, 54)
>>> row['b', 'a'] = (11, 22)
>>> row
Unpacker(a=22, b=11)
```

In case any one attribute doesn't exists, a KeyError exception should be raised:

```python
>>> row = Unpacker({'a': 234, 'b': 54})
>>> row['a', 'c', 'b']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    raise KeyError(key)
KeyError: 'c'
```
