"""Tests for the reprtools exercise using pytest."""
from collections import UserDict
from typing import Optional

import pytest

from src.reprtools.reprtools import format_arguments


class TestFormatArguments:
    """Tests for format_arguments."""

    @pytest.mark.parametrize("arg, expected_res", [
        (1, "1"),
        (None, "None"),
        ("hello", "'hello'"),
    ])
    def test_one_positional_argument(self, arg: object, expected_res: str) -> None:
        assert format_arguments(arg) == expected_res

    @pytest.mark.parametrize("kwargs, expected_res", [
        ({"n": 1}, "n=1"),
        ({"object": None}, "object=None"),
        ({"name": "Ushio"}, "name='Ushio'"),
    ])
    def test_one_keyword_argument(self, kwargs: dict[str, object], expected_res: str):
        assert format_arguments(**kwargs) == expected_res

    @pytest.mark.parametrize("args, expected_res", [
        ((1, 2), "1, 2"),
        ((" ", ["pizza", "crepe"]), "' ', ['pizza', 'crepe']"),
    ])
    def test_multiple_positional_arguments(self, args: tuple[object, ...], expected_res: str):
        assert format_arguments(*args) == expected_res

    @pytest.mark.parametrize("kwargs, expected_res", [
        ({"n": 1, "object": None}, "n=1, object=None"),
        ({"file": "log", "mode": "wt"}, "file='log', mode='wt'"),
    ])
    def test_multiple_keyword_arguments(self, kwargs: dict[str, object], expected_res: str):
        assert format_arguments(**kwargs) == expected_res

    @pytest.mark.parametrize("args, kwargs, expected_res", [
        ((["pizza", "crepe"], ), {"start": 1}, "['pizza', 'crepe'], start=1"),
        (("log", "wt"), {"encoding": "utf-8", "newline": ""}, "'log', 'wt', encoding='utf-8', newline=''"),
    ])
    def test_mixed_arguments(self, args: tuple[object, ...], kwargs: dict[str, object], expected_res: str):
        assert format_arguments(*args, **kwargs) == expected_res


@pytest.mark.bonus1
class MakeReprTests:
    """Tests for make_repr."""

    def test_no_args_or_kwargs(self):
        from src.reprtools.reprtools import make_repr

        class Empty:
            __repr__ = make_repr()  # type: ignore
        assert str(Empty()) == "Empty()"
        assert repr(Empty()) == "Empty()"

    def test_with_args(self):
        from src.reprtools.reprtools import make_repr

        class Point:
            def __init__(self, x: int, y: int, z: int):
                self.x, self.y, self.z = x, y, z
            __repr__ = make_repr(args=["x", "y", "z"])  # type: ignore

        assert str(Point(1, 2, 3)) == "Point(1, 2, 3)"
        assert repr(Point(x=3, y=4, z=5)) == "Point(3, 4, 5)"

    def test_with_kwargs(self):
        from src.reprtools.reprtools import make_repr

        class Point:
            def __init__(self, x: int, y: int, color: str = "purple"):
                self.x, self.y = x, y
                self.color = color
            __repr__ = make_repr(kwargs=["x", "y"])  # type: ignore
        assert str(Point(1, 2)) == "Point(x=1, y=2)"
        assert repr(Point(x=3, y=4)) == "Point(x=3, y=4)"


@pytest.mark.bonus2
class TestAutoRepr:
    """Tests for auto_repr."""

    def test_with_args(self):
        from src.reprtools.reprtools import auto_repr

        @auto_repr(args=["x", "y", "z"])
        class Point:
            def __init__(self, x: int, y: int, z: int):
                self.x, self.y, self.z = x, y, z
        assert str(Point(1, 2, 3)) == "Point(1, 2, 3)"
        assert repr(Point(x=3, y=4, z=5)) == "Point(3, 4, 5)"

    def test_with_kwargs(self):
        from src.reprtools.reprtools import auto_repr

        @auto_repr(kwargs=["x", "y"])
        class Point:
            def __init__(self, x: int, y: int, color: str = "purple"):
                self.x, self.y = x, y
                self.color = color
        assert str(Point(1, 2)) == "Point(x=1, y=2)"
        assert repr(Point(x=3, y=4)) == "Point(x=3, y=4)"

    def test_with_inheritance(self):
        from src.reprtools.reprtools import auto_repr

        @auto_repr(kwargs=["x", "y", "data"])
        class Point(UserDict[str, int | str]):
            def __init__(self, x: int, y: int, **data: str):
                self.x, self.y = x, y
                super().__init__(data)
        point = Point(1, 2, color="purple")
        assert str(point) == "Point(x=1, y=2, data={'color': 'purple'})"
        assert list(point) == ["color"]


@pytest.mark.bonus2
class TestFullAutoRepr:
    """Tests for auto_repr with no arguments."""

    def test_with_concrete_attributes_no_defaults(self):
        from src.reprtools.reprtools import auto_repr

        @auto_repr
        class Point:
            def __init__(self, x: int, y: int, z: int):
                self.x, self.y, self.z = x, y, z
        assert str(Point(1, 2, 3)) == "Point(x=1, y=2, z=3)"  # pyright: ignore
        assert repr(Point(x=3, y=4, z=5)) == "Point(x=3, y=4, z=5)"  # pyright: ignore

    def test_argument_with_a_default(self):
        from src.reprtools.reprtools import auto_repr

        @auto_repr
        class Thing:
            def __init__(self, name: str, color: str = "purple"):
                self.name = name
                self.color = color
        assert str(Thing("duck")) == "Thing(name='duck', color='purple')"  # pyright: ignore

    def test_with_property(self):
        from src.reprtools.reprtools import auto_repr

        @auto_repr
        class BankAccount:
            def __init__(self, balance: int = 0):
                self._balance = balance
                BankAccount.current_id = 1
                self.account_id = BankAccount.current_id

            @property
            def balance(self):
                return self._balance

        assert str(BankAccount()) == "BankAccount(balance=0)"  # pyright: ignore
        assert str(BankAccount(5)) == "BankAccount(balance=5)"  # pyright: ignore

    def test_argument_without_an_attribute(self):
        from src.reprtools.reprtools import auto_repr

        @auto_repr
        class BankAccount:

            def __init__(self, opening_balance: int):
                self.balance = opening_balance

        with pytest.raises(TypeError):
            str(BankAccount(10))  # pyright: ignore

        with pytest.raises(TypeError):
            repr(BankAccount(10))  # pyright: ignore

    def test_default_argument_without_an_attribute(self):
        from src.reprtools.reprtools import auto_repr

        @auto_repr
        class BankAccount:
            def __init__(self, balance: int = 0, custom_id: Optional[int] = None):
                self._balance = balance
                self.account_id = custom_id if custom_id is not None else 1

            @property
            def balance(self):
                return self._balance

        assert str(BankAccount(custom_id=10)) == "BankAccount(balance=0)"  # pyright: ignore
        assert str(BankAccount(5)) == "BankAccount(balance=5)"  # pyright: ignore
