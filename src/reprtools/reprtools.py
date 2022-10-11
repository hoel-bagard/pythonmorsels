import inspect
from collections.abc import Callable
from typing import Optional, ParamSpec, TypeVar


_P = ParamSpec("_P")
_R = TypeVar("_R")


def format_arguments(*args: object, **kwargs: object) -> str:
    repr_str = ", ".join(repr(arg) for arg in args)
    if args and kwargs:
        repr_str += ", "
    if kwargs:
        repr_str += ", ".join(f"{key}={repr(value)}" for key, value in kwargs.items())
    return repr_str


def make_repr(args: Optional[list[str]] = None, kwargs: Optional[list[str]] = None) -> Callable[[object], str]:
    def repr(self: object) -> str:
        args_v = tuple(getattr(self, arg) for arg in args) if args is not None else ()
        kwargs_v = {key: getattr(self, key) for key in kwargs} if kwargs else {}
        return type(self).__name__ + "(" + format_arguments(*args_v, **kwargs_v) + ")"
    return repr


def auto_repr(args: Optional[list[str]] | Callable[_P, _R] = None,
              kwargs: Optional[list[str]] = None) -> Callable[_P, _R]:
    if isinstance(args, list) or kwargs:
        def decorator(cls: Callable[_P, _R]) -> Callable[_P, _R]:
            cls.__repr__ = make_repr(args, kwargs)
            return cls
        return decorator
    cls = args

    sig = inspect.signature(cls)
    kwargs: dict[str, bool] = {} # str: name, bool: is_optional
    for name, param in sig.parameters.items():
        kwargs[name] = param.default != inspect.Parameter.empty

    def repr(self: Callable[_P, _R]) -> str:
        kwargs_v = {}
        for key, is_optional in kwargs.items():
            try:
                value = getattr(self, key)
            except AttributeError:
                if not is_optional:
                    raise TypeError(f"'{type(self).__name__}' object has no attribute '{key}'")
                continue
            kwargs_v[key] = value
        return type(self).__name__ + "(" + format_arguments(*(), **kwargs_v) + ")"

    cls.__repr__ = repr
    return cls

def auto_reprB2(args: Optional[list[str]] = None,
                kwargs: Optional[list[str]] = None) -> Callable[[Callable[_P, _R]], Callable[_P, _R]]:
    def decorator(cls: Callable[_P, _R]) -> Callable[_P, _R]:
        cls.__repr__ = make_repr(args, kwargs)
        return cls
    return decorator


def auto_reprB3(cls: Callable[_P, _R]) -> Callable[_P, _R]:
    sig = inspect.signature(cls)
    kwargs: dict[str, bool] = {} # str: name, bool: is_optional
    for name, param in sig.parameters.items():
        kwargs[name] = param.default != inspect.Parameter.empty

    def repr(self: Callable[_P, _R]) -> str:
        kwargs_v = {}
        for key, is_optional in kwargs.items():
            try:
                value = getattr(self, key)
            except AttributeError:
                if not is_optional:
                    raise TypeError(f"'{type(self).__name__}' object has no attribute '{key}'")
                continue
            kwargs_v[key] = value
        return type(self).__name__ + "(" + format_arguments(*(), **kwargs_v) + ")"

    cls.__repr__ = repr
    return cls


def assert_equal(res: str, expected_res: str):
    assert res == expected_res, f"Wrong result, got:\n\t{res}\nbut expected\n\t{expected_res}"


def main():
    # Base Exercise
    print("\nBasic exercise")
    assert_equal(format_arguments(1, 2, 3), "1, 2, 3")
    assert_equal(format_arguments("expenses.csv", mode="wt", encoding="utf-8"),
                 "'expenses.csv', mode='wt', encoding='utf-8'")

    # Bonus 1
    print("\nBonus 1")

    class PointB1:
        def __init__(self, x: int, y: int, color: str = "purple"):
            self.x, self.y = x, y
            self.color = color
        __repr__ = make_repr(args=["x", "y"], kwargs=["color"])  # pyright: ignore

    assert_equal(repr(PointB1(1, 2)), "PointB1(1, 2, color='purple')")
    assert_equal(repr(PointB1(x=3, y=4, color="green")), "PointB1(3, 4, color='green')")

    # Bonus 2
    print("\nBonus 2")

    @auto_repr(args=['x', 'y'], kwargs=['color'])
    class PointB2:
        def __init__(self, x: int, y: int, color: str = "purple"):
            self.x, self.y = x, y
            self.color = color

    assert_equal(repr(PointB2(1, 2)), "PointB2(1, 2, color='purple')")
    assert_equal(repr(PointB2(x=3, y=4, color='green')), "PointB2(3, 4, color='green')")

    # Bonus 3
    print("\nBonus 3")

    @auto_repr
    class PointB3:
        def __init__(self, x: int, y: int, color: str = "purple"):
            self.x, self.y = x, y
            self.color = color

    assert_equal(repr(PointB3(1, 2)), "PointB3(x=1, y=2, color='purple')")
    assert_equal(repr(PointB3(x=3, y=4, color="green")), "PointB3(x=3, y=4, color='green')")

    @auto_repr
    class BankAccount:
        def __init__(self, balance: int = 0, account_name: Optional[str] = None):
            self._balance = balance
            self.opening_balance = balance
            self.name = account_name
        @property
        def balance(self):
            return self._balance
    assert_equal(repr(BankAccount()), "BankAccount(balance=0)")

    @auto_repr
    class Point:
        def __init__(self, x: int, y: int):
            self.coordinates = (x, y)
    try:
        repr(Point(5, 6))
        raise Exception("Should have raised a TypeError but did not.")
    except TypeError:
        pass


if __name__ == "__main__":
    main()
