"""Suppress exercise from python morsel."""

import traceback
from contextlib import ContextDecorator   # Class version
from contextlib import contextmanager    # Function version
from dataclasses import dataclass
from types import TracebackType
from typing import Optional


@dataclass
class Context:
    """Store context of an exception."""

    exception: Optional[Exception] = None
    traceback: Optional[TracebackType] = None


@contextmanager
def suppress_fn(*exceptions):
    context = Context()
    try:
        yield context
    except exceptions as e:
        context.exception = e
        context.traceback = traceback.format_exc()
    # finally:
        # Code to release resource


class suppress(ContextDecorator):  # noqa: N801
    """Context manager that suppresses the given exceptions."""

    def __init__(self, *exceptions):
        self.exceptions = exceptions
        self.context = Context()

    def __enter__(self, *exceptions):
        return self.context

    def __exit__(self, *exc):
        # if exc[0] in self.exceptions:
        print(self.exceptions[0])
        print(exc[0])
        print(isinstance(exc[0], self.exceptions[0]))
        if any([isinstance(exc[0], exception) for exception in self.exceptions]):
            self.context.exception = exc[1]
            self.context.traceback = exc[2]
            return True  # Stops the exception from being propagated


def main():
    # Main exercise
    with suppress(NameError):
        print("Hi!")
        print("It's nice to meet you,", name)
        print("Goodbye!")

    # with suppress(TypeError):
    #     print("Hi!")
    #     print("It's nice to meet you,", name)
    #     print("Goodbye!")

    with suppress(ValueError):
        int("Hello")

    # Bonus 1
    with suppress(ValueError, TypeError):
        int("Hello")
    with suppress(ValueError, TypeError):
        int(None)

    # Bonus 2
    print("\nBonus 2 prints")
    with suppress(ValueError, TypeError) as context:
        int("Hello")
    print(context.exception)
    print(context.traceback)

    # Bonus 3
    print("\nBonus 3 prints")

    @suppress(TypeError)
    def len_or_none(thing):
        return len(thing)
    print(len_or_none("Hello"))
    print(len_or_none())
    print(len_or_none([1, 2, 3]))


if __name__ == "__main__":
    main()
