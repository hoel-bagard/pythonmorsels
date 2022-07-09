# [alias](https://www.pythonmorsels.com/exercises/31d30a8a37dd452bb7efcf226ac0dae5)

### My notes
- The base exercise was insteresting since I do not use descriptors often. Once the base exercise is done, the bonuses are trivial.
- [Documentation on descriptors](https://docs.python.org/3/howto/descriptor.html#descriptorhowto) (quite good).


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

#### Bonus 2
For the second bonus, I'd like you to accept a write keyword argument to allow your aliased attribute to be written to. Using that attribute would look like this:

```python
class DataRecord:
    title = alias("serial", write=True)
    def __init__(self, serial):
        self.serial = serial
```
And writing to the alias should update the value of the attribute being aliased:

```python
>>> record = DataRecord("148X")
>>> record.title = "149S"
>>> record.serial
'149S'
```


#### Bonus 3
For the third bonus, I'd like you to support class-level aliases and not just instance-level aliases.

For example here's a class that maintains a _registry attribute and a read-only registry attribute aliasing it:

```python
class RegisteredObject:
    _registry = ()
    registry = alias('_registry')
    def __init__(self, name):
        RegisteredObject._registry += (self,)
        self.name = name
```

Accessing the above class's registry attribute should work properly:
```python
>>> object = RegisteredObject("Trey")
>>> object.name
'Trey'
>>> RegisteredObject.registry
(<alias.RegisteredObject object at 0x7f06ca5bf9b0>,)
```

The tests only check for class-level attribute lookups (not assignments).
