"""Tests for the with_previous exercise using Pytest."""
from collections.abc import Iterable
from typing import Optional, TypeVar

import pytest

from src.with_previous.with_previous import with_previous


T = TypeVar("T")


def assert_equal_iterable(iterable1: Iterable[Optional[T]], iterable2: Iterable[Optional[T]]) -> None:
    assert list(iterable1) == list(iterable2)


@pytest.mark.parametrize("iterable, expected_value",
                         [([1, 2, 3], [(1, None), (2, 1), (3, 2)]),
                          (["1", "2"], [("1", None), ("2", "1")]),
                          ([None, None], [(None, None), (None, None)]),
                          ])
def test_basic(iterable: Iterable[Optional[T]], expected_value: list[Optional[T]]):
    assert_equal_iterable(with_previous(iterable), expected_value)


def test_empty():
    assert_equal_iterable(with_previous([]), [])


def test_one_item():
    assert_equal_iterable(with_previous([1]), [(1, None)])


@pytest.mark.bonus1
class TestBonus1:
    def test_lazy_iterable(self):
        generator = (n**2 for n in [1, 2, 3])
        expected_outputs = [(1, None), (4, 1), (9, 4)]
        assert_equal_iterable(with_previous(generator), expected_outputs)


@pytest.mark.bonus2
class TestBonus2:
    def test_returns_lazy_iterable(self):
        inputs = (n**2 for n in [1, 2, 3])
        iterable = with_previous(inputs)
        assert iterable == iter(iterable)
        assert next(iterable) == (1, None)
        assert list(inputs) != []


@pytest.mark.bonus3
class TestBonus3:
    def test_fillvalue_as_keyword_argument_only(self):
        """Test can be called with fillvalue (but only as keyword arg)."""
        inputs = [1, 2, 3]
        expected_outputs = [(1, 0), (2, 1), (3, 2)]
        assert_equal_iterable(with_previous(inputs, fillvalue=0), expected_outputs)
        with pytest.raises(TypeError):
            with_previous(inputs, 0)  # type: ignore
