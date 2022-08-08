from collections.abc import Iterable
from itertools import count
from typing import TypeVar

import pytest

from src.interleave.interleave import interleave


T1 = TypeVar("T1")
T2 = TypeVar("T2")


def assert_equal_iterables(iterable1: Iterable[object], iterable2: Iterable[object]) -> None:
    assert list(iterable1) == list(iterable2)


def test_empty_lists():
    assert_equal_iterables(interleave([], []), [])


def test_single_item_each():
    assert_equal_iterables(interleave([1], [2]), [1, 2])


def test_two_items_each():
    assert_equal_iterables(interleave([1, 2], [3, 4]), [1, 3, 2, 4])


def test_four_items_each():
    in1 = [1, 2, 3, 4]
    in2 = [5, 6, 7, 8]
    out = [1, 5, 2, 6, 3, 7, 4, 8]
    assert_equal_iterables(interleave(in1, in2), out)


def test_none_value():
    in1 = [1, 2, 3, None]
    in2 = [4, 5, 6, 7]
    out = [1, 4, 2, 5, 3, 6, None, 7]
    assert_equal_iterables(interleave(in1, in2), out)


def test_string_and_range():
    out = [0, 'H', 1, 'e', 2, 'l', 3, 'l', 4, 'o']
    assert_equal_iterables(interleave(range(5), "Hello"), out)


def test_with_generator():
    in1 = [1, 2, 3, 4]
    in2 = (n**2 for n in in1)
    out = [1, 1, 2, 4, 3, 9, 4, 16]
    assert_equal_iterables(interleave(in1, in2), out)


@pytest.mark.bonus1
def test_response_is_iterator():
    in1 = [1, 2, 3]
    in2 = [4, 5, 6]
    squares = (n**2 for n in in1)
    output = interleave(in1, in2)
    assert iter(output) is iter(output)
    output = interleave(squares, squares)
    assert next(output) == 1
    assert next(output) == 4
    assert next(squares) == 9
    iterator = interleave(count(), count())
    assert next(iterator) == next(iterator)


@pytest.mark.bonus2
def test_more_than_two_arguments():
    in1 = [1, 2, 3]
    in2 = [4, 5, 6]
    in3 = [7, 8, 9]
    out = [1, 4, 7, 2, 5, 8, 3, 6, 9]
    assert_equal_iterables(interleave(in1, in2, in3), out)


@pytest.mark.bonus3
def test_different_length_lists():
    in1 = [1, 2, 3]
    in2 = [4, 5, 6, 7, 8]
    in3 = [9]
    out1 = [1, 4, 9, 2, 5, 3, 6, 7, 8]
    assert_equal_iterables(interleave(in1, in2, in3), out1)
    assert_equal_iterables(
        interleave([1, 2], [3], [4, 5, 6], [7, 8], [9]),
        [1, 3, 4, 7, 9, 2, 5, 8, 6],
    )
