"""Suppress exercise from python morsel."""

from contextlib import ContextDecorator   # Class version
from contextlib import contextmanager    # Function version
from dataclasses import dataclass
from types import TracebackType
from typing import Iterator, Optional, Sized, Type


@dataclass
class Context:
    """Store context of an exception."""

    exception: Optional[Exception] = None
    traceback: Optional[TracebackType] = None


@contextmanager
def suppress_fn(*exception_types: Type[Exception]) -> Iterator[Context]:
    context = Context()
    try:
        yield context
    except exception_types as e:
        context.exception = e
        context.traceback = e.__traceback__
        # import traceback
        # context.traceback = traceback.format_exc()
    # finally:
        # Code to release resource


class suppress(ContextDecorator):  # noqa: N801
    """Context manager that suppresses the given exceptions."""

    def __init__(self, *exceptions_types: Type[Exception]):
        self.exceptions_types = exceptions_types
        self.context = Context()

    def __enter__(self) -> Context:
        return self.context

    def __exit__(self, exception_type: Type[Exception], exception: Exception, traceback: TracebackType) -> bool:
        if isinstance(exception, self.exceptions_types):
            self.context.exception = exception
            self.context.traceback = traceback
            return True
        else:
            return False


def main() -> None:
    # Main exercise
    with suppress(NameError):
        print("Hi!")
        print("It's nice to meet you,", name)  # type: ignore  # noqa
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
        int(None)  # type: ignore

    # Bonus 2
    print("\nBonus 2 prints")
    with suppress(ValueError, TypeError) as context:
        int("Hello")
    print(context.exception)
    print(context.traceback)

    # Bonus 3
    print("\nBonus 3 prints")

    @suppress(TypeError)
    def len_or_none(thing: Sized) -> int:
        return len(thing)
    print(len_or_none("Hello"))
    print(len_or_none())  # type: ignore
    print(len_or_none([1, 2, 3]))


if __name__ == "__main__":
    main()
