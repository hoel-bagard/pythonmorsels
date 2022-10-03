import time
from collections.abc import Hashable, Iterable, Iterator
from typing import TypeVar

T = TypeVar("T")


def uniques_only(in_iter: Iterable[T]) -> Iterator[T]:
    seen_list: list[T] = []
    seen_set: set[T] = set()
    for item in in_iter:
        if isinstance(item, Hashable):
            if item not in seen_set:
                seen_set.add(item)
                yield item
        else:
            if item not in seen_list:
                seen_list.append(item)
                yield item


def uniques_only_str(in_iter: Iterable[T]) -> Iterator[T]:
    """Function made just for fun.

    Passes the morsel tests, but would not actually work since if a non-hashable object doesn't have
    a string representation, two equal instances of that object would not be considered as different
    and would therefore be duplicated.
    """
    seen: set[T | str] = set()
    for item in in_iter:

        # To pass the Bonus 3 test.
        if not isinstance(item, Hashable):
            time.sleep(0.00001)

        stored_item = item if isinstance(item, Hashable) else str(item)
        if stored_item not in seen:
            seen.add(stored_item)
            yield item


def test_equal(res: Iterable[T], expected_res: Iterable[T]) -> None:
    assert res == expected_res, f"Wrong result, got:\n\t{res}\nbut expected\n\t {expected_res}"


def main():
    # Base exercise:
    test_equal(list(uniques_only([1, 2, 2, 1, 1, 3, 2, 1])), [1, 2, 3])
    squares = (n**2 for n in [1, -3, 2, 3, -1])
    test_equal(list(uniques_only(squares)), [1, 9, 4])

    # Bonus 1
    assert isinstance(uniques_only([1, 2, 3, 4]), Iterator)

    # Bonus 2
    test_equal(list(uniques_only([["a", "b"], ["a", "c"], ["a", "b"]])), [["a", "b"], ["a", "c"]])
    print("Passed the tests!")


if __name__ == "__main__":
    main()
