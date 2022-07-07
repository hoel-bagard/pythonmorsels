# [Pluck](https://www.pythonmorsels.com/exercises/4932f67db2734adda695d20e4441c249)

### My notes
Standard and fairly simple exercise on dictionaries, a bit disappointed that recursion isn't the best answer. 


### Usage
Run the tests with:
- For all tests: `python -m pytest src/pluck`.
- For only the base exercise: `python -m pytest src/pluck -m "not (bonus1 or bonus2 or bonus3)"`
- For the base exercise and the first bonus: `python -m pytest src/pluck -m "not (bonus2 or bonus3)"`
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

#### Bonus 1
For the first bonus, you should make the separator character customizable:

```python
>>> data = {'amount': 10.64, 'category': {'name': 'Music', 'group': 'Fun'}}
>>> pluck(data, 'category/name', sep='/')
'Music'
```

#### Bonus 2
For the second bonus, an optional default value should be accepted which will return a default value for keys that don't exist:
```python
>>> data = {'amount': 10.64, 'category': {'name': 'Music', 'group': 'Fun'}}
>>> pluck(data, 'category.created', default='N/A')
'N/A'
```
Note that when the default argument is not provided, a KeyError should be raised for non-existent keys (just as before).

#### Bonus 3
For the third bonus, your pluck function should accept any number of lookup key paths. When multiple arguments are specified, the return value should be a tuple of all the found keys:
```python
>>> data = {'amount': 10.64, 'category': {'name': 'Music', 'group': 'Fun'}}
>>> pluck(data, 'category.name', 'amount')
('Music', 10.64)
```
