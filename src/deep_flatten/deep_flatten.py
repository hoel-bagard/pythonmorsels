from collections.abc import Iterator
from typing import Iterable, TypeVar


T = TypeVar("T", str, int)
NestedIterable = Iterable[T | "NestedIterable[T]"]


def deep_flatten(my_input: NestedIterable[T]) -> Iterator[T]:
    for item in my_input:
        if isinstance(item, Iterable) and not isinstance(item, str):
            yield from deep_flatten(item)
        else:
            yield item  # type: ignore


def deep_flatten_list(iterable: NestedIterable[T]) -> list[T]:
    return list(deep_flatten(iterable))


def test_equal(res: object, expected_res: object):
    assert res == expected_res, f"Wrong result, got:\n\t{res}\nbut expected\n\t {expected_res}"


def main():
    # Base exercise:
    test_equal(deep_flatten_list([[(1, 2), (3, 4)], [(5, 6), (7, 8)]]), [1, 2, 3, 4, 5, 6, 7, 8])
    test_equal(deep_flatten_list([[1, [2, 3]], 4, 5]), [1, 2, 3, 4, 5])

    # Bonus 1
    # Make sure your deep_flatten function accepts not just lists and tuples, but generators, sets,
    # and other iterable data structures (but don"t worry about handling strings yet, as we"ll handle them in bonus 3).
    test_equal(sorted(deep_flatten({(1, 2), (3, 4), (5, 6), (7, 8)})), [1, 2, 3, 4, 5, 6, 7, 8])

    # Bonus 2
    # For the second bonus, I"d like you to make deep_flatten return an iterator that loops over input lazily.
    numbers_and_words = enumerate([99, 98, 97])
    flattened = deep_flatten(numbers_and_words)
    test_equal(next(flattened), 0)
    test_equal(next(flattened), 99)

    # Bonus 3
    # For the third bonus, I"d like you to make sure deep_flatten works with strings:
    test_equal(list(deep_flatten([["apple", "pickle"], ["pear", "avocado"]])), ["apple", "pickle", "pear", "avocado"])
    print("Passed the tests.")


if __name__ == "__main__":
    main()
