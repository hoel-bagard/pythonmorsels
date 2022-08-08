from collections.abc import Iterable
from typing import TypeVar

T1 = TypeVar("T2")
T2 = TypeVar("T1")


def interleave_b1(iter1: Iterable[T1], iter2: Iterable[T2]) -> Iterable[T1 | T2]:
    for elt1, elt2 in zip(iter1, iter2):
        yield elt1
        yield elt2


def interleave(*iterables: Iterable[object]) -> Iterable[object]:
    for elts in zip(*iterables):
        for elt in elts:
            yield elt


def assert_equal(res, expected_res) -> None:
    assert res == expected_res, f"Wrong result, got:\n\t{res}\nbut expected\n\t {expected_res}"


def main():
    # Base exercise:
    numbers = [1, 2, 3, 4]
    assert_equal(list(interleave(numbers, range(5, 9))), [1, 5, 2, 6, 3, 7, 4, 8])
    assert_equal(list(interleave(numbers, (n**2 for n in numbers))), [1, 1, 2, 4, 3, 9, 4, 16])

    # Bonus 1
    i = interleave([1, 2, 3, 4], [5, 6, 7, 8])
    assert_equal(next(i), 1)
    assert_equal(list(i), [5, 2, 6, 3, 7, 4, 8])

    # Bonus 2
    assert_equal(list(interleave([1, 2, 3], [4, 5, 6], [7, 8, 9])), [1, 4, 7, 2, 5, 8, 3, 6, 9])

    # Bonus 3

    print("Passed the tests.")


if __name__ == "__main__":
    main()
