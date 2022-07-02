# [Pluck](https://www.pythonmorsels.com/exercises/4932f67db2734adda695d20e4441c249)

### My notes


### Usage
Run the tests with:
- For all tests: `pytest src/pluck`.
- For only the base exercise: `pytest src/pluck -m "not (bonus1 or bonus2 or bonus3)"`
- For the base exercise and the first bonus: `pytest src/pluck -m "not (bonus2 or bonus3)"`
Run the main file with `python src/pluck/pluck.py`.

### Description:
#### Base problem
Write a function called pluck, which will be a helper for working with nested dictionary-based data (possibly from deserializing some JSON).\
The pluck function will accept a dictionary of dictionaries and a string representing a period-delimited "path" to the nested value we'll be returning:

```python
>>> data = {'amount': 10.64, 'category': {'name': 'Music', 'group': 'Fun'}}
>>> pluck(data, 'amount')
10.64
>>> pluck(data, 'category.group')
'Fun'
>>> pluck(data, 'category.created')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'created'
```
Your pluck function should work for arbitrarily nested dictionary-like data.
