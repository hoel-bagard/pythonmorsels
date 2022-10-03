import functools
import traceback
from dataclasses import dataclass
from typing import Any, Callable, Optional, ParamSpec, TypeVar


_P = ParamSpec("_P")
_R = TypeVar("_R")

NO_RETURN = object()


@dataclass
class Call:
    args: tuple[Any, ...]
    kwargs: dict[str, Any]
    return_value: Any = NO_RETURN
    exception: Optional[BaseException] = None


# class record_calls:  # noqa: N801
#     def __init__(self, func: Callable[..., Any]):
#         functools.update_wrapper(self, func)
#         self.func = func
#         self.call_count = 0
#         self.calls: list[Call] = []

#     def __call__(self, *args: Any, **kwargs: dict[str, Any]):
#         self.call_count += 1
#         try:
#             return_value = self.func(*args, **kwargs)
#             self.calls.append(Call(args, kwargs, return_value, None))
#             return return_value
#         except Exception as e:
#             self.calls.append(Call(args, kwargs, NO_RETURN, e))
#             raise


def record_calls(func: Callable[_P, _R]) -> Callable[_P, _R]:
    """Record calls to the given function."""
    @functools.wraps(func)
    def wrapper(*args: _P.args, **kwargs: _P.kwargs):
        wrapper.call_count += 1
        call = Call(args, kwargs)
        wrapper.calls.append(call)
        try:
            call.return_value = func(*args, **kwargs)
        except BaseException as e:
            call.exception = e
            raise
        return call.return_value
    wrapper.call_count = 0
    wrapper.calls = []
    return wrapper


def main():
    @record_calls
    def greet(name: str = "world"):
        """Greet someone by their name."""
        print(f"Hello {name}")

    # Basic Exercise
    print("\nBasic exercise")
    greet("Trey")
    print(f"{greet.call_count=}")
    greet(name="Trey")
    print(f"{greet.call_count=}")

    # Bonus 1
    print("\nBonus 1")
    help(greet)
    print(str(greet))

    # Bonus 2
    print("\nBonus 2")
    print(f"{greet.calls[0].args=}")
    print(f"{greet.calls[0].kwargs=}")

    print(f"{greet.calls[1].args=}")
    print(f"{greet.calls[1].kwargs=}")

    # Bonus 3
    print("\nBonus 3")

    @record_calls
    def cube(n: float):
        return n**3

    print(f"{cube(3)=}")
    print(cube.calls)
    try:
        cube(None)  # type: ignore
    except Exception:
        print(traceback.format_exc())
    print(cube.calls[-1].exception)
    print(cube.calls[-1].return_value == NO_RETURN)


if __name__ == "__main__":
    main()
