# [alias](https://www.pythonmorsels.com/exercises/31d30a8a37dd452bb7efcf226ac0dae5)

### My notes
- Insteresting exercise, learned quite a bit.
- []Documentation on descriptors](https://docs.python.org/3/howto/descriptor.html#descriptorhowto) (quite good).


### Usage
Run the tests with:
- For all tests: `python -m pytest src/alias`.
- For only the base exercise: `python -m pytest src/alias -m "not (bonus1 or bonus2 or bonus3)"`
- For the base exercise and the first bonus: `python -m pytest src/alias -m "not (bonus2 or bonus3)"`

Run the main file with `python src/alias/alias.py`.

### Description:
#### Base problem
I'd like you to create a callable helper utility, called alias, for making classes with attributes that act as "aliases" to other attributes. The alias callable should work like this:

```python
class DataRecord:
    title = alias("serial")
    def __init__(self, serial):
        self.serial = serial
```
This should allow title to mirror the value of serial when being read:

```python
>>> record = DataRecord("148X")
>>> record.title
"148X"
>>> record.serial = "149S"
>>> record.title
"149S"
```

You don't need to worry about what happens when you write to title, until the first bonus.

This is a very weird one. If you're completely stumped, I recommend taking a look at the hints (specifically the "what is this even" hint).

#### Bonus 1
For the first bonus, I'd like you to make sure an AttributeError exception is raised when your aliases are assigned to.

```python
>>> class DataRecord:
...     title = alias('serial')
...     def __init__(self, serial):
...         self.serial = serial
...
>>> record = DataRecord("148X")
>>> record.title = "149S"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: can't set attribute
```
