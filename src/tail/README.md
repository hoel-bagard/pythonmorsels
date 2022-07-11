# [tail](https://www.pythonmorsels.com/exercises/83ed2a27b86b41a185036b262fb67c41)

### My notes
- A `deque` can be initialized from an iterable.

### Usage
Run the tests with:
- For all tests: `python -m pytest src/tail`.
- For only the base exercise: `python -m pytest src/tail -m "not bonus1"`

Run the main file with `python src/tail/tail.py`.

### Description:
#### Base problem
I want you to make a function that takes a sequence (like a list, string, or tuple) and a number n and returns the last n elements from the given sequence, as a list.

For example:
```python
>>> tail([1, 2, 3, 4, 5], 3)
[3, 4, 5]
>>> tail('hello', 2)
['l', 'o']
>>> tail('hello', 0)
[]
```

#### Bonus 1
As a bonus, make your function return an empty list for negative values of n:
```python
>>> tail('hello', -2)
[]
```

#### Bonus 2
Note: We don't recommend this bonus for Mixed-level users, unless you need an extra challenge.

As a second bonus, make sure your function works with any iterable, not just sequences. For example:
```python
>>> squares = (n**2 for n in range(10))
>>> tail(squares, 3)
[49, 64, 81]
```
You should make sure you don't loop at all if n is 0 or negative.

See if you can make your function relatively memory efficient (if you're looping over a very long iterable, don't store the entire thing in memory).

