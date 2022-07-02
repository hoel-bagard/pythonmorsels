from typing import TypeVar

import pytest

from src.pluck.pluck import NestedDict, pluck


N = TypeVar('N', bound=int)  # The tests only use ints for simplicity
X = TypeVar('X')


@pytest.fixture
def example_nested_dict() -> NestedDict[int]:
    return {'a': {'b': 5, 'z': 20}, 'c': {'d': 3}, 'x': 40}


@pytest.mark.parametrize("path, expected_result", [
    ('x', 40),
    ('c', {'d': 3}),
])
def test_pluck_top_level(example_nested_dict: NestedDict[N], path: str, expected_result: NestedDict[N] | N):
    assert pluck(example_nested_dict, path) == expected_result


@pytest.mark.parametrize("path, expected_result", [
    ("a.b", 5),
    ("c.d", 3),
])
def test_pluck_one_level_deep(example_nested_dict: NestedDict[N], path: str, expected_result: NestedDict[N] | N):
    assert pluck(example_nested_dict, path) == expected_result


@pytest.mark.parametrize("path, expected_result", [
    ("a.b.c", {'d': {'e': 4}}),
    ("a.b.c.d", {'e': 4}),
    ("a.b.c.d.e", 4),
])
def test_pluck_many_levels_deep(path: str, expected_result: NestedDict[N] | N):
    deep_nested_dict = {'a': {'b': {'c': {'d': {'e': 4}}}}}
    assert pluck(deep_nested_dict, path) == expected_result


@pytest.mark.parametrize("path", [
    ("c.e"),
    ('z'),
])
def test_exception_on_missing_item(example_nested_dict: NestedDict[N], path: str):
    with pytest.raises(KeyError):
        pluck(example_nested_dict, path)


@pytest.mark.bonus1
@pytest.mark.parametrize("path, sep, expected_result", [
    ("c/d", '/', 3),
    ("a.b", '.', 5),
    ("a z", ' ', 20),
])
def test_specifying_separator(example_nested_dict: NestedDict[N],
                              path: str,
                              sep: str,
                              expected_result: NestedDict[N] | N):
    assert pluck(example_nested_dict, path, sep=sep) == expected_result


@pytest.mark.bonus2
@pytest.mark.parametrize("path, default, expected_result", [
    ("c.e", None, None),
    ("y.z", 0, 0),
])
def test_specifying_default_value(example_nested_dict: NestedDict[N],
                                  path: str,
                                  default: X,
                                  expected_result: NestedDict[N] | N | X):
    assert pluck(example_nested_dict, path, default=default) == expected_result


@pytest.mark.bonus3
@pytest.mark.parametrize("paths, default, expected_result", [
    (("a.b", "c.e", "c.d", "x"), None, (5, None, 3, 40)),
])
def test_multiple_lookups_accepted(example_nested_dict: NestedDict[N],
                                   paths: tuple[str, ...],
                                   default: X,
                                   expected_result: tuple[NestedDict[N] | N | X, ...]):
    assert pluck(example_nested_dict, *paths, default=default) == expected_result
