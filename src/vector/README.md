# [Vecotr](https://www.pythonmorsels.com/exercises/ced757b8a1bd400bb983aa8a2eb0e8fe)

### My notes
- Use `Number` when typing/testing for any type of number, rather than float or int (`from numbers import Number`).
  - (pyright very much does not like it though, as not all operations are defined on `Number`)
- Use `astuple` from the dataset package to convert a dataclass to a tuple (if `__iter__` has been defined a simple `tuple()` call is enough).

### Usage
Run the tests with:
- For all tests: `python -m pytest src/vector`.
- For only the base exercise: `python -m pytest src/vector -m "not (bonus1 or bonus2 or bonus3)"`
- For the base exercise and the first bonus: `python -m pytest src/vector -m "not (bonus2 or bonus3)"`

Run the main file with `python src/vector/vector.py`.

### Description:
#### Base problem

I'd like you to make a 3-dimensional `Vector` class that works with multiple assignment, supports equality and inequality operators.

```python
>>> v = Vector(1, 2, 3)
>>> x, y, z = v
>>> print(x, y, z)
1 2 3
>>> v == Vector(1, 2, 4)
False
>>> v == Vector(1, 2, 3)
True
```

The `Vector` class also must use `__slots__` for efficient attribute lookups, meaning other attributes won't be able to be assigned to it and it won't have a `__dict__` like most classes we make do.

```python
>>> v.a = 4
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Vector' object has no attribute 'a'
>>> v.__dict__
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Vector' object has no attribute '__dict__'
```
Vectors shouldn't have unexpected behavior like having a length or support for operators like < and > or being addable to tuples.

#### Bonus 1
For the first bonus, I'd like you to make your `Vector` objects support addition and subtraction with other Vector objects:

```python
>>> Vector(1, 2, 3) + Vector(4, 5, 6) == Vector(5, 7, 9)
True
>>> Vector(5, 7, 9) - Vector(3, 1, 2) == Vector(2, 6, 7)
True
```
Note that addition and subtraction shouldn't work in-place: they should return a new `Vector` object.

#### Bonus 2
For the second bonus, I'd like your vector to support multiplication and division by numbers (this should return a new scaled vector):

```python
>>> 3 * Vector(1, 2, 3) == Vector(3, 6, 9)
True
>>> Vector(1, 2, 3) * 2 == Vector(2, 4, 6)
True
>>> Vector(1, 2, 3) / 2 == Vector(0.5, 1, 1.5)
True
```

#### Bonus 3
For the third bonus, I'd like you to make your `Vector` class immutable, meaning the coordinates (`x`, `y`, and `z`) cannot be changed after a new `Vector` has been defined:

    ```python
>>> v = Vector(1, 2, 3)
>>> v.x = 4
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    raise AttributeError("Vectors are immutable")
AttributeError: Vectors are immutable
```
