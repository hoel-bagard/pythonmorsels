from collections import deque
from collections.abc import Iterable
from typing import TypeVar


T = TypeVar('T')


def tail(iterable: Iterable[T], nb_elts: int) -> list[T]:
    if nb_elts <= 0:
        return []

    tail_elts = deque(maxlen=nb_elts)
    for elt in iterable:
        tail_elts.append(elt)

    return list(tail_elts)


def test_equal(res: list[T], expected_res: list[T]) -> None:
    assert res == expected_res, f"Wrong result, got:\n\t{res}\nbut expected\n\t {expected_res}"


def main():
    # Base exercise:
    print("Testing the base exercise")
    test_equal(tail([1, 2, 3, 4, 5], 3), [3, 4, 5])
    test_equal(tail("hello", 2), ['l', 'o'])
    test_equal(tail("hello", 0), [])

    # Bonus 1
    print("Testing bonus 1")
    test_equal(tail('hello', -2), [])

    # Bonus 2
    print("Testing bonus 2")
    squares = (n**2 for n in range(10))
    test_equal(tail(squares, 3), [49, 64, 81])

    print("Passed the tests!")


if __name__ == "__main__":
    main()

