## [Suppress exercise](https://www.pythonmorsels.com/exercises/ded322173d47424581be45adaeeca90d/)
Solution [here](https://www.pythonmorsels.com/exercises/ded322173d47424581be45adaeeca90d/solution/)

### Sources on context managers
- https://www.pythonmorsels.com/exercises/ded322173d47424581be45adaeeca90d/submit/1/
- https://docs.python.org/3/library/contextlib.html
For 3rd Bonus:
- https://docs.python.org/3/library/contextlib.html#contextlib.ContextDecorator


### Checking for exceptions
```python
return isinstance(exception, self.exception_types)
```
This works because isinstance will accept a single class or a tuple of classes to check. The issubclass function works the same way.
