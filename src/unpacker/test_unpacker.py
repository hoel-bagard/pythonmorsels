"""Tests for the Unpacker exercise using Pytest."""
# pyright: reportGeneralTypeIssues=false
from collections import OrderedDict
from datetime import date
from typing import TypeVar

import pytest

from src.unpacker.unpacker import Unpacker


T = TypeVar("T")


@pytest.fixture
def dict_sample() -> dict[str, int]:
    return {"a": 2, "b": 3}


@pytest.fixture
def unpacker_sample(dict_sample: dict[str, T]) -> Unpacker[T]:
    return Unpacker(dict_sample)


@pytest.mark.parametrize("in_dict", [
    ({}),
    ({"d": 3}),
    ({"a": 2, "b": 3}),
])
def test_constructor(in_dict: dict[str, int]) -> None:
    Unpacker(in_dict)


def test_empty_constructor() -> None:
    Unpacker()


def test_indpendence_from_dict(dict_sample: dict[str, int]) -> None:
    unpacker = Unpacker(dict_sample)
    dict_sample["a"] = 4
    unpacker["a"] = 5
    assert dict_sample["a"] == 4
    assert unpacker["a"] == 5


@pytest.mark.parametrize("key", [
    ("a"),
    ("b"),
])
def test_key_access(unpacker_sample: Unpacker[int], dict_sample: dict[str, int], key: str) -> None:
    assert unpacker_sample[key] == dict_sample[key]


def test_attribute_access(unpacker_sample: Unpacker[int], dict_sample: dict[str, int]) -> None:
    assert unpacker_sample.a == dict_sample["a"]
    assert unpacker_sample.b == dict_sample["b"]


def test_key_assignment(unpacker_sample: Unpacker[int]) -> None:
    unpacker_sample["a"] = 45
    unpacker_sample["b"] = 67
    assert unpacker_sample["a"] == 45
    assert unpacker_sample["b"] == 67


def test_attribute_assignment(unpacker_sample: Unpacker[int]) -> None:
    unpacker_sample.a = 45
    unpacker_sample.b = 67
    assert unpacker_sample.a == 45
    assert unpacker_sample.b == 67
    assert unpacker_sample["a"] == 45
    assert unpacker_sample["b"] == 67


def test_only_as_key_access() -> None:
    unpacker = Unpacker({"shape type": 1, "identifier": "Square"})
    assert unpacker.identifier == "Square"
    assert unpacker["shape type"] == 1


def test_original_dictionary_unchanged(dict_sample: dict[str, int]) -> None:
    original_dict = dict_sample.copy()
    unpacker_sample = Unpacker(dict_sample)
    unpacker_sample.c = 4
    assert dict_sample == original_dict


@pytest.mark.bonus1
def test_multiple_assignment() -> None:
    u = Unpacker(OrderedDict([("a", 12), ("b", 13)]))
    a, b = u
    assert a == u.a
    assert b == u.b
    u.c = 14
    assert u["c"] == 14
    a, b, c = u
    assert a == u.a
    assert b == u.b
    assert c == u.c


@pytest.mark.bonus2
def test_multiple_key_assignment(unpacker_sample: Unpacker[object]) -> None:
    assert repr(unpacker_sample) == "Unpacker(a=2, b=3)"
    assert str(unpacker_sample) == "Unpacker(a=2, b=3)"
    unpacker_sample["c"] = 4
    assert str(unpacker_sample) == "Unpacker(a=2, b=3, c=4)"
    unpacker_sample["c"] = "hi"
    assert str(unpacker_sample) == "Unpacker(a=2, b=3, c='hi')"
    unpacker_sample["a"] = date(2020, 1, 1)
    assert str(unpacker_sample) == "Unpacker(a=datetime.date(2020, 1, 1), b=3, c='hi')"


@pytest.mark.bonus3
def test_multiple_key_return(unpacker_sample: Unpacker[int]) -> None:
    assert unpacker_sample["a", "b"] == (2, 3)

    unpacker_sample.b = 4
    assert unpacker_sample["a", "b"] == (2, 4)

    unpacker_sample["a", "b", "c"] = (5, 6, 7)
    assert unpacker_sample["a"] == 5
    assert unpacker_sample["b"] == 6
    assert unpacker_sample["c"] == 7

    unpacker_sample["a", "e"] = 100, 300
    unpacker_sample["b", "c"] = (n**2 for n in [2, 3])
    assert unpacker_sample["a"] == 100
    assert unpacker_sample["b"] == 4
    assert unpacker_sample["c"] == 9
    assert unpacker_sample["e"] == 300

    with pytest.raises(ValueError):
        unpacker_sample["a", "b", "c"] = (5, 6)
    assert unpacker_sample["a"] == 100
    assert unpacker_sample["b"] == 4
    assert unpacker_sample["c"] == 9
    assert unpacker_sample["e"] == 300

    with pytest.raises(ValueError):
        unpacker_sample["a", "b"] = (5, 6, 7)
    assert unpacker_sample["a"] == 100
    assert unpacker_sample["b"] == 4
    assert unpacker_sample["c"] == 9
    assert unpacker_sample["e"] == 300
