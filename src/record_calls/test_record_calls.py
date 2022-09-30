"""Tests for the record_calls exercise using Pytest."""
from typing import Any

import pytest

from src.record_calls.record_calls import NO_RETURN, record_calls


def test_call_count_starts_at_zero():
    decorated = record_calls(lambda: None)
    assert decorated.call_count == 0


def test_not_called_on_decoration_time():
    def my_func():
        raise AssertionError("Function called too soon")
    record_calls(my_func)


def test_function_still_callable():
    recordings = []

    def my_func():
        recordings.append("call")
    decorated = record_calls(my_func)
    assert recordings == []
    decorated()
    assert recordings == ["call"]
    decorated()
    assert recordings == ["call", "call"]


def test_return_value():
    def one() -> int:
        return 1
    one = record_calls(one)
    assert one() == 1


def test_takes_arguments():
    def add(x: int, y: int):
        return x + y
    add = record_calls(add)
    assert add(1, 2) == 3
    assert add(1, 3) == 4


def test_takes_keyword_arguments():
    recordings: list[tuple[tuple[Any, ...], dict[str, Any]]] = []

    @record_calls
    def my_func(*args: Any, **kwargs: dict[str, Any]):
        recordings.append((args, kwargs))
        return recordings
    assert my_func() == [((), {})]
    assert my_func(1, 2, **{"a": 3}) == [((), {}), ((1, 2), {"a": 3})]


def test_call_count_increments():
    decorated = record_calls(lambda: None)
    assert decorated.call_count == 0
    decorated()
    assert decorated.call_count == 1
    decorated()
    assert decorated.call_count == 2


def test_different_functions():
    my_func1 = record_calls(lambda: None)
    my_func2 = record_calls(lambda: None)
    my_func1()
    assert my_func1.call_count == 1
    assert my_func2.call_count == 0
    my_func2()
    assert my_func1.call_count == 1
    assert my_func2.call_count == 1


@pytest.mark.bonus1
def test_docstring_and_name_preserved():
    import pydoc

    def example(a: int, b: bool = True) -> int:
        """This is a docstring, yay!"""
        return a + b

    decorated = record_calls(example)
    assert "example" in str(decorated)
    # pydoc.render_doc does basically the same thing as help(...)
    documentation = pydoc.render_doc(decorated)
    assert "example" in documentation
    assert "This is a docstring, yay!" in documentation
    assert "(a: int, b: bool = True)" in documentation


@pytest.mark.bonus2
def test_record_arguments():
    @record_calls
    def my_func(*args: Any, **kwargs: dict[str, Any]):
        return args, kwargs
    assert my_func.calls == []
    my_func()
    assert len(my_func.calls) == 1
    assert my_func.calls[0].args == ()
    assert my_func.calls[0].kwargs == {}
    my_func(1, 2, **{"a": 3})
    assert len(my_func.calls) == 2
    assert my_func.calls[1].args == (1, 2)
    assert my_func.calls[1].kwargs == {"a": 3}


@pytest.mark.bonus3
def test_record_return_values():
    @record_calls
    def my_func(*args: Any, **kwargs: dict[str, Any]):
        return sum(args), kwargs
    my_func()
    assert my_func.calls[0].return_value == (0, {})
    my_func(1, 2, **{"a": 3})
    assert my_func.calls[1].return_value == (3, {"a": 3})
    assert my_func.calls[1].exception is None
    with pytest.raises(TypeError) as context:
        my_func(1, "hi", **{"a": 3})
    assert my_func.calls[2].return_value is NO_RETURN
    assert my_func.calls[2].exception == context.value
