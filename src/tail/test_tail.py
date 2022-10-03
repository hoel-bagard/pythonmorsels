"""Tests for the tail exercise using Pytest."""
from collections.abc import Iterable
from typing import TypeVar

import pytest

from src.tail.tail import tail


T = TypeVar("T")


@pytest.mark.parametrize("iterable, length, expected_value",
                         [([1, 2], 0, []),
                          ([1, 2], 1, [2]),
                          ([1, 2], 2, [1, 2]),
                          ("test", 3, ["e", "s", "t"]),
                          ((3, 2, 1), 3, [3, 2, 1])])
def test_basic(iterable: Iterable[T], length: int, expected_value: list[T]):
    assert tail(iterable, length) == expected_value


@pytest.mark.parametrize("iterable, length, expected_value",
                         [([1, 2, 3, 4], 10, [1, 2, 3, 4]),
                          ([], 10, [])])
def test_n_larger_than_iterable_length(iterable: Iterable[T], length: int, expected_value: list[T]):
    assert tail(iterable, length) == expected_value


@pytest.mark.bonus1
class TestBonus1:
    @pytest.mark.parametrize("iterable, length, expected_value",
                             [([1, 2, 3, 4], -1, []),
                              ((), -10, [])])
    def test_negative_n(self, iterable: Iterable[T], length: int, expected_value: list[T]):
        assert tail(iterable, length) == expected_value


@pytest.mark.bonus2
class TestBonus2:
    def test_iterator(self):
        nums = (n**2 for n in [1, 2, 3, 4])
        assert tail(nums, -1) == []  # Don't loop for negative n
        assert tail(nums, 0) == []  # Don't loop for n=0
        assert tail(nums, 2) == [9, 16]  # Consuming the generator
        assert list(nums) == []  # The nums generator is now empty
        assert tail(nums, 1) == []  # n=1 with a now empty generator
