"""Tests for the parse_ranges exercise using pytest."""
import pytest

from src.parse_ranges.parse_ranges import parse_ranges


@pytest.mark.parametrize("str_ranges, expected_res", [
    ("1-2,4-4,8-10", [1, 2, 4, 8, 9, 10]),
    ("1-2,4-4,8-13", [1, 2, 4, 8, 9, 10, 11, 12, 13]),
    ("0-0, 4-8, 20-20, 43-45", [0, 4, 5, 6, 7, 8, 20, 43, 44, 45])
])
def test_ranges(str_ranges: str, expected_res: list[int]):
    assert list(parse_ranges(str_ranges)) == expected_res


@pytest.mark.parametrize("str_ranges, expected_res", [
    ("1-2,  4-4, 8-10", [1, 2, 4, 8, 9, 10]),
    ("0-0, 4-8, 20-21, 43-45", [0, 4, 5, 6, 7, 8, 20, 21, 43, 44, 45]),
])
def test_with_spaces(str_ranges: str, expected_res: list[int]):
    assert list(parse_ranges(str_ranges)) == expected_res


@pytest.mark.bonus1
def test_return_iterator():
    numbers = parse_ranges("0-0, 4-8, 20-21, 43-45")
    assert next(numbers) == 0
    assert list(numbers) == [4, 5, 6, 7, 8, 20, 21, 43, 44, 45]
    assert list(numbers) == []
    numbers = parse_ranges("100-1000000000000")
    assert next(numbers) == 100


@pytest.mark.bonus2
@pytest.mark.parametrize("str_ranges, expected_res", [
    ("1, 4-4, 8-10", [1, 4, 8, 9, 10]),
    ("0,4-8,20,43-45", [0, 4, 5, 6, 7, 8, 20, 43, 44, 45])
])
def test_with_individual_numbers(str_ranges: str, expected_res: list[int]):
    assert list(parse_ranges(str_ranges)) == expected_res


@pytest.mark.bonus2
@pytest.mark.parametrize("str_ranges, expected_res", [
    ("1, 4->4, 8-10", [1, 4, 8, 9, 10]),
    ("0,4-8,20->exit,43-45", [0, 4, 5, 6, 7, 8, 20, 43, 44, 45])
])
def test_ignore_arrows(str_ranges: str, expected_res: list[int]):
    assert list(parse_ranges(str_ranges)) == expected_res
