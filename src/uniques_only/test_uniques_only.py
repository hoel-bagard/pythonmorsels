"""Tests for the uniques_only exercise using Pytest."""
from collections.abc import Iterable
from timeit import repeat
from typing import TypeVar

import pytest

from src.uniques_only.uniques_only import uniques_only


T = TypeVar('T')


@pytest.mark.parametrize("input_iter, expected_res", [
    ([1, 2, 3], [1, 2, 3]),
    (['1', "23"], ['1', "23"]),
])
def test_no_duplicates(input_iter: Iterable[T], expected_res: list[T]):
    assert list(uniques_only(input_iter)) == expected_res


@pytest.mark.parametrize("input_iter, expected_res", [
    ([1, 1, 2, 2, 3], [1, 2, 3]),
    (['1', '1', "23", "23"], ['1', "23"]),
])
def test_adjacent_duplicates(input_iter: Iterable[T], expected_res: list[T]):
    assert list(uniques_only(input_iter)) == expected_res


@pytest.mark.parametrize("input_iter, expected_res", [
    ([1, 2, 3, 1, 2], [1, 2, 3]),
    (['1', "23", '1', "23"], ['1', "23"]),
])
def test_non_adjacent_duplicates(input_iter: Iterable[T], expected_res: list[T]):
    assert list(uniques_only(input_iter)) == expected_res


@pytest.mark.parametrize("input_iter, expected_res", [
    ([1, 1, 2, 2, 1, 2], [1, 2]),
    (['1', "23", '1', '1', "23"], ['1', "23"]),
])
def test_lots_of_duplicates(input_iter: Iterable[T], expected_res: list[T]):
    assert list(uniques_only(input_iter)) == expected_res


@pytest.mark.parametrize("input_iter, expected_res", [
    ([4, 8, 3, 7, 2, 8, 4, 2, 1, 9, 3, 5], [4, 8, 3, 7, 2, 1, 9, 5]),
    (['2', '1', "23", "23"], ['2', '1', "23"]),
])
def test_order_maintained(input_iter: Iterable[T], expected_res: list[T]):
    assert list(uniques_only(input_iter)) == expected_res


@pytest.mark.parametrize("input_iter, expected_res", [
    ((n**2 for n in [1, 2, 3]), [1, 4, 9])
])
def test_accepts_iterator(input_iter: Iterable[T], expected_res: list[T]):
    assert list(uniques_only(input_iter)) == expected_res


@pytest.mark.bonus1
class TestBonus1:
    def test_returns_iterator(self):
        nums = iter([1, 2, 3])
        output = uniques_only(nums)
        assert next(output) == 1
        # The below line tests that the incoming generator isn't exhausted.
        # It may look odd to test the nums input, but this is correct because after 1 item has been consumed
        # from the uniques_only iterator, nums should only have 1 item consumed as well.
        try:
            assert next(nums) == 2
        except StopIteration:
            assert False, "The incoming nums iterator was fully consumed!"  # noqa: B011


@pytest.mark.bonus2
class TestBonus2:
    @pytest.mark.parametrize("input_iter, expected_res", [
        ([[1, 2], [3], [1], [3]], [[1, 2], [3], [1]])
    ])
    def test_accepts_nonhashable_types(self, input_iter: Iterable[T], expected_res: list[T]):
        assert list(uniques_only(input_iter)) == expected_res


@pytest.mark.bonus3
class TestBonus3:
    def test_hashable_types_faster(self):
        hashables = [(n, n+1) for n in range(1000)]
        unhashables = [[n] for n in range(1000)]
        variables = {
            "hashables": hashables,
            "unhashables": unhashables,
            "uniques_only": uniques_only,
        }
        hashable_time = min(repeat(
            "list(uniques_only(hashables))",
            number=3,
            repeat=3,
            globals=variables
        ))
        unhashable_time = min(repeat(
            "list(uniques_only(unhashables))",
            number=3,
            repeat=3,
            globals=variables
        ))
        assert hashable_time*3 < unhashable_time
