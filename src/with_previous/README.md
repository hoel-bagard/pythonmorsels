# [with_previous](https://www.pythonmorsels.com/exercises/492b1f182bf44203a3f17227c681bdcc)

### My notes
- Really standard, might be good for people not familiar with iterables or generators.
- The solution gives a way to solve the exercise using the standard library:

```python
from itertools import tee, chain
def with_previous(iterable):
    i1, i2 = tee(iterable)
    return zip(i1, chain([None], i2))
```


### Usage
Run the tests with:
- For all tests: `python -m pytest src/with_previous`.
- For only the base exercise: `python -m pytest src/with_previous -m "not bonus1 or bonus2 or bonus3"`

Run the main file with `python src/with_previous/with_previous.py`.

### Description:
#### Base problem

I want you to write a function that accepts a sequence (a list for example) and returns a new iterable (anything you can loop over) that includes a tuple of each item and the previous item (the item just before it). The first "previous item" should be None.

For example:
```python
>>> list(with_previous("hello"))
[('h', None), ('e', 'h'), ('l', 'e'), ('l', 'l'), ('o', 'l')]
>>> list(with_previous([1, 2, 3]))
[(1, None), (2, 1), (3, 2)]
```

#### Bonus 1
For the first bonus, make sure you accept any iterable as an argument, not just a sequence (which means you can't use index lookups in your answer).

Here's an example with a generator expression, which is a lazy iterable:
```python
>>> list(with_previous(n**2 for n in [1, 2, 3]))
[(1, None), (4, 1), (9, 4)]
```

#### Bonus 2
Note: We don't recommend this bonus for Novice-level users, unless you need an extra challenge.

For the second bonus, I want you to return a lazy iterator (for example a generator) from your `with_previous` function instead of a list.

This should allow your `with_previous` function to accept infinitely long iterables. If your function returns an iterator, this should work:
```python
>>> next(with_previous([1, 2, 3]))
(1, None)
```

#### Bonus 3
As a third bonus, I want you to allow your `with_previous` function to accept an optional fillvalue keyword-only argument (defaulting to None).

This should allow your function to work like this:

```python
>>> list(with_previous([1, 2, 3], fillvalue=0))
[(1, 0), (2, 1), (3, 2)]
But this new argument should only be allowed as a keyword argument. This should raise an error:

>>> list(with_previous([1, 2, 3], 0))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: with_previous() takes 1 positional argument but 2 were given
```
