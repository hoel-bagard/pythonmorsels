# [uniques_only](https://www.pythonmorsels.com/exercises/b684cd595ca745398131f2252ca13064)

### My notes
- None


### Usage
Run the tests with:
- For all tests: `python -m pytest src/uniques_only`.
- For only the base exercise: `python -m pytest src/uniques_only -m "not (bonus1 or bonus2 or bonus3)"`
- For the base exercise and the first bonus: `python -m pytest src/uniques_only -m "not (bonus2 or bonus3)"`
Run the main file with `python src/uniques_only/uniques_only.py`.

### Description:
#### Base problem
See if you can figure out at least one of the bonuses for this exercise if you have time.

I want you to write a function that accepts an iterable and returns a new iterable with all items from the original iterable except for duplicates.

Here's an example:

```python
>>> uniques_only([1, 2, 2, 1, 1, 3, 2, 1])
[1, 2, 3]
>>> nums = [1, -3, 2, 3, -1]
>>> squares = (n**2 for n in nums)
>>> uniques_only(squares)
[1, 9, 4]
```
Note that the order of the returned elements should remain the same.

#### Bonus 1

As a bonus, return an iterator (for example a generator) from your `uniques_only` function instead of a list. This should allow your `uniques_only` function to accept infinitely long iterables (or other lazy iterables).

#### Bonus 2
Note: We don't recommend this bonus for Novice-level users, unless you need an extra challenge.

Here's another bonus to do after you've made your `uniques_only` function return a lazy iterable: allow your `uniques_only` function to work with unhashable objects.

For example when two lists with equal items are provided, they should be seen as duplicates:

```python
>>> list(uniques_only([['a', 'b'], ['a', 'c'], ['a', 'b']]))
[['a', 'b'], ['a', 'c']]
```

#### Bonus 3
For an extra bonus, make sure your function works efficiently with hashable items while still accepting unhashable items.
