# [Record Calls](https://www.pythonmorsels.com/exercises/3ee85ad3481f428d99458b102cbda7c6/)


## Sources on decorators: ##

https://realpython.com/primer-on-python-decorators/
https://www.pythonmorsels.com/exercises/3ee85ad3481f428d99458b102cbda7c6/submit/1/


## Notes: ##

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


## Useful snipets / templates: ##

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

Validating a json:
```
from flask import Flask, request, abort
import functools
app = Flask(__name__)

def validate_json(*expected_args):                  # 1
    def decorator_validate_json(func):
        @functools.wraps(func)
        def wrapper_validate_json(*args, **kwargs):
            json_object = request.get_json()
            for expected_arg in expected_args:      # 2
                if expected_arg not in json_object:
                    abort(400)
            return func(*args, **kwargs)
        return wrapper_validate_json
    return decorator_validate_json
```
