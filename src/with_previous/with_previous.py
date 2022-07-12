from collections.abc import Iterable
from typing import Optional, TypeVar


T = TypeVar('T')


def with_previous(iterable: Iterable[T], *, fillvalue: Optional[T] = None) -> tuple[T, T | None]:
    previous = fillvalue
    for item in iterable:
        yield (item, previous)
        previous = item


def assert_equal(res: list[tuple[T, Optional[T]]], expected_res: list[tuple[T, Optional[T]]]) -> None:
    assert res == expected_res, f"Wrong result, got:\n\t{res}\nbut expected\n\t {expected_res}"


def main():
    # Base exercise:
    print("Testing the base exercise")
    assert_equal(list(with_previous("hello")), [('h', None), ('e', 'h'), ('l', 'e'), ('l', 'l'), ('o', 'l')])
    assert_equal(list(with_previous([1, 2, 3])), [(1, None), (2, 1), (3, 2)])

    # Bonus 1
    print("Testing bonus 1")
    assert_equal(list(with_previous(n**2 for n in [1, 2, 3])), [(1, None), (4, 1), (9, 4)])

    # Bonus 2
    print("Testing bonus 2")
    assert_equal(next(with_previous([1, 2, 3])), (1, None))

    # Bonus 3
    print("Testing bonus 3")
    assert_equal(list(with_previous([1, 2, 3], fillvalue=0)), [(1, 0), (2, 1), (3, 2)])
    try:
        list(with_previous([1, 2, 3], 0))
        raise Exception("Should have raised a TypeError but did not")
    except TypeError:
        pass

    print("Passed the tests!")


if __name__ == "__main__":
    main()
