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


def auto_repr(args: Optional[list[str]] = None,
              kwargs: Optional[list[str]] = None) -> Callable[[Callable[_P, _R]], Callable[_P, _R]]:
    def decorator(cls: Callable[_P, _R]) -> Callable[_P, _R]:
        cls.__repr__ = make_repr(args, kwargs)
        return cls
    return decorator


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


if __name__ == "__main__":
    main()
