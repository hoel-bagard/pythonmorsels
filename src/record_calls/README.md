# [Record Calls](https://www.pythonmorsels.com/exercises/3ee85ad3481f428d99458b102cbda7c6/)

### Usage
Run the tests with:
- For all tests: `python -m pytest src/record_calls`.
- For only the base exercise: `python -m pytest src/record_calls -m "not (bonus1 or bonus2 or bonus3)"`
- For the base exercise and the first bonus: `python -m pytest src/record_calls -m "not (bonus2 or bonus3)"`

Run the main file with `python src/record_calls/record_calls.py`.

### My Notes:

About preserving the doctring and function info:\
This doesn't quite pass our tests though. Unfortunately, the record_calls class will still have an unhelpful string representation and it still won't have quite the right documentation.
We could try to fix this ourselves, but it's kind of a pain. The easiest way to fix this is to rely on the third-party wrapt library.

```
import wrapt
class record_calls(wrapt.ObjectProxy):
    """Record calls to the given function."""
    def __init__(self, func):
        super().__init__(func)
        self.call_count = 0

    def __call__(self, *args, **kwargs):
        self.call_count += 1
        return self.__wrapped__(*args, **kwargs)
```
The wrapt library has a lot of decorator helpers in it, but the one that we're concerned with is the one that allows us to make a class which will act as a seamless wrapper around a function. It's a little bit awkward to use wrapt.ObjectProxy, but it works.

I don't usually show third-party libraries in these solutions and I didn't expect you to discover this one, but I wanted you to know it exists because it can come in handy at times (for making any kind of decorator, not just ones that use classes).

#### Sources on decorators:
https://realpython.com/primer-on-python-decorators/
https://www.pythonmorsels.com/exercises/3ee85ad3481f428d99458b102cbda7c6/submit/1/

#### Useful snipets / templates:
Basic boiler plate template:
```
import functools

def decorator(func):
    """ Some comment here """
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # Do something before
        value = func(*args, **kwargs)
        # Do something after
        return value
    return wrapper_decorator
```

Singleton:
```
import functools

def singleton(cls):
    """Make a class a Singleton class (only one instance)"""
    @functools.wraps(cls)
    def wrapper_singleton(*args, **kwargs):
        if not wrapper_singleton.instance:
            wrapper_singleton.instance = cls(*args, **kwargs)
        return wrapper_singleton.instance
    wrapper_singleton.instance = None
    return wrapper_singleton

@singleton
class TheOne:
    pass
```

### Description
#### Base problem
I'd like you to write a decorator function that will record the number of times a function is called.

Your decorator function should be called record_calls and it'll work like this:

```python
@record_calls
def greet(name="world"):
    """Greet someone by their name."""
    print(f"Hello {name}")
```
That `record_calls`-decorated greet function will now have a `call_count` attribute that keeps track of the number of times it was called:

```python
>>> greet("Trey")
Hello Trey
>>> greet.call_count
1
>>> greet()
Hello world
>>> greet.call_count
2
```
Decorator functions are functions which accept another function and return a new version of that function to replace it.

So this should be the same thing as what we typed above:

```python
greet = record_calls(greet)
```
If you haven't ever made a decorator function before, you'll want to look up how to make one.

If you've made a decorator function before, you might want to attempt one of the bonuses.

#### Bonus 1
For the first bonus I'd like you to make sure your decorator function preserves the name and the docstring, and call signature of the original function.

So if we use record_calls on this greet function:

```python
>>> @record_calls
... def greet(name="world"):
...     """Greet someone by their name."""
...     print(f"Hello {name}")
...
```
When we ask for help on that function, we should see something like this:

```python
>>> help(greet)
```
Help on function greet in module `__main__`:

```python
greet(name='world')
    Greet someone by their name.
```

#### Bonus 2
For the second bonus I'd like you to keep track of a calls attribute on our function that records the arguments and keyword arguments provided for each call to our function.

```python
>>> @record_calls
... def greet(name="world"):
...     """Greet someone by their name."""
...     print(f"Hello {name}")
...
>>> greet("Trey")
Hello Trey
>>> greet.calls[0].args
('Trey',)
>>> greet.calls[0].kwargs
{}
>>> greet(name="Trey")
Hello Trey
>>> greet.calls[1].args
()
>>> greet.calls[1].kwargs
{'name': 'Trey'}
```
Note that calls should contain a sequence where each element has an args attribute and a kwargs attribute.

### Bonus 3
For the third bonus, add a `return_value` attribute and an `exception` attribute to each of the objects in our calls list. If the function returned successfully, `return_value` will contain the return value. Otherwise, `exception` will contain the exception raised.

When an exception is raised, `return_value` should be set to a special `NO_RETURN` value. Your module should have a `NO_RETURN` attribute that contains this special value.

```python
>>> @record_calls
... def cube(n):
...     return n**3
...
>>> cube(3)
27
>>> cube.calls
[Call(args=(3,), kwargs={}, return_value=27, exception=None)]
>>> cube(None)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 9, in wrapper
  File "<stdin>", line 3, in cube
TypeError: unsupported operand type(s) for ** or pow(): 'NoneType' and 'int'
>>> cube.calls[-1].exception
TypeError("unsupported operand type(s) for ** or pow(): 'NoneType' and 'int'")
>>> cube.calls[-1].return_value == NO_RETURN
True
```
