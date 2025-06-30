# [Float Range](https://www.pythonmorsels.com/exercises/8ae5aa9f75be40f480ea326c424014e1)

## Notes:

- No need to implement `__iter__` if `__getitem__` and `__len__` are implemented.
- Can use the [slice.indices](https://docs.python.org/3/reference/datamodel.html?highlight=slice%20indices#slice.indices) method to "fix" a slice's boundaries.

### Usage

- Run the python morsels tests with `python src/float_range/test_float_range.py`.
- Run the main file with `python src/float_range/float_range.py`.

### Description:

#### Base problem

I'd like you to write a callable called `float_range` that acts sort of like the built-in `range` callable but it should allow for floating point numbers to be specified as start, stop, and step values.

The object returned by calling `float_range` should be iterable, have a nice string representation, and have a length:

```python
>>> r = float_range(0.5, 2.5, 0.5)
>>> r
float_range(0.5, 2.5, 0.5)
>>> list(r)
[0.5, 1.0, 1.5, 2.0]
>> len(r)
4
>>> for n in r:
...     print(n)
...
0.5
1.0
1.5
2.0
```

Negative step values should work as well:

```python
>>> list(float_range(3.5, 0, -1))
[3.5, 2.5, 1.5, 0.5]
>>> len(float_range(3.5, 0, -1))
4
```

And just like the `range`, the `step` and `start` arguments to be optional:

```python
>>> for n in float_range(0.0, 3.0):
...     print(n)
...
0.0
1.0
2.0
>>> for n in float_range(3.0):
...     print(n)
...
0.0
1.0
2.0
```

Note that the value returned by `float_range` should also be able to be looped over multiple times, but the return value should be memory-efficient (it shouldn't create a large list of numbers).

I recommend attempting the base problem first before attempting the bonuses.

### Bonus 1

For the first bonus, make `float_range` objects indexable and reversible:

```python
>>> my_range = float_range(0.5, 7, 0.75)
>>> my_range[1]
1.25
>>> my_range[-1]
6.5
>>> my_range[10]
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
IndexError: float_range index out of range
>>> list(reversed(my_range))
[6.5, 5.75, 5.0, 4.25, 3.5, 2.75, 2.0, 1.25, 0.5]
```

### Bonus 2

For the second bonus, I'd like you to make sure that you can take the object returned from `float_range` and ask if it's equal to another object returned from `float_range`:

```python
>>> a = float_range(0.5, 2.5, 0.5)
>>> b = float_range(0.5, 2.5, 0.5)
>>> c = float_range(0.5, 3.0, 0.5)
>>> a == b
True
>>> a == c
False
```

In fact I'd like you to take that a step further and make sure you can compare these objects to `range` objects also and that other comparisons won't raise exceptions:

```python
>>> float_range(5) == range(0, 5)
True
>>> float_range(4) == range(5)
False
>>> float_range(4) == 3
False
```

### Bonus 3

For the third bonus, make the `float_range` objects sliceable:

```python
>>> my_range = float_range(0.5, 7, 0.75)
>>> list(my_range[:2])
[0.5, 1.25]
>>> list(my_range[-1:100])
[6.5]
>>> list(my_range[-3:])
[5.0, 5.75, 6.5]
>>> list(my_range[::2])
[0.5, 2.0, 3.5, 5.0, 6.5]
```

Note that slices should allow negative indexing and missing start or end indexes. Also note that a step is allowed and that out-of-range indexes should be accepted by slices just as they usually are.

### Hints

- Base Hints
  - [Accepting optional arguments](https://www.pythonmorsels.com/making-a-function/)
  - [Making an iterable class](https://www.pythonmorsels.com/how-to-make-an-iterable/)
  - [range is not an iterator](https://treyhunner.com/2018/02/python-range-is-not-an-iterator/)
  - [Returning length of custom object](https://www.pythonmorsels.com/making-the-len-function-work-on-your-python-objects/)
  - [A helper for calculating the length](https://stackoverflow.com/a/14822215/2633215)
  - [In case you find specifying start= confusing](https://www.pythonmorsels.com/positional-only-function-arguments/)
- Bonus 1 Hints
  - [Overriding the \[...\] lookup syntax](https://www.pythonmorsels.com/supporting-index-and-key-lookups/)
  - [Making a custom object reversible](https://stackoverflow.com/a/38751057/2633215)
- Bonus 2 Hints
  - [Implementing equality checks](https://www.pythonmorsels.com/overloading-equality-in-python/)
- Bonus 3 Hints
  - [Managing negative or out-of-bounds indexes](https://www.pythonmorsels.com/implementing-slicing/)
