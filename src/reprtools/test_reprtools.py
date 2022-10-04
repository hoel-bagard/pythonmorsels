"""Tests for the reprtools exercise using pytest."""
# from collections import UserDict

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


# # To test bonus 2, comment out the next line
# @unittest.expectedFailure
# class AutoReprTests(unittest.TestCase):

#     """Tests for auto_repr."""

#     def test_with_args(self):
#         from reprtools import auto_repr

#         @auto_repr(args=['x', 'y', 'z'])
#         class Point:
#             def __init__(self, x, y, z):
#                 self.x, self.y, self.z = x, y, z
#         self.assertEqual(str(Point(1, 2, 3)), "Point(1, 2, 3)")
#         self.assertEqual(repr(Point(x=3, y=4, z=5)), "Point(3, 4, 5)")

#     def test_with_kwargs(self):
#         from reprtools import auto_repr

#         @auto_repr(kwargs=['x', 'y'])
#         class Point:
#             def __init__(self, x, y, color="purple"):
#                 self.x, self.y = x, y
#                 self.color = color
#         self.assertEqual(str(Point(1, 2)), "Point(x=1, y=2)")
#         self.assertEqual(repr(Point(x=3, y=4)), "Point(x=3, y=4)")

#     def test_with_inheritance(self):
#         from reprtools import auto_repr

#         @auto_repr(kwargs=['x', 'y', 'data'])
#         class Point(UserDict):
#             def __init__(self, x, y, **data):
#                 self.x, self.y = x, y
#                 super().__init__(data)
#         point = Point(1, 2, color="purple")
#         self.assertEqual(
#             str(point),
#             "Point(x=1, y=2, data={'color': 'purple'})",
#         )
#         self.assertEqual(list(point), ["color"])


# # To test bonus 3, comment out the next line
# @unittest.expectedFailure
# class auto_repr(unittest.TestCase):

#     """Tests for auto_repr with no arguments."""

#     def test_with_concrete_attributes_no_defaults(self):
#         from reprtools import auto_repr

#         @auto_repr
#         class Point:
#             def __init__(self, x, y, z):
#                 self.x, self.y, self.z = x, y, z
#         self.assertEqual(str(Point(1, 2, 3)), "Point(x=1, y=2, z=3)")
#         self.assertEqual(repr(Point(x=3, y=4, z=5)), "Point(x=3, y=4, z=5)")

#     def test_argument_with_a_default(self):
#         from reprtools import auto_repr

#         @auto_repr
#         class Thing:
#             def __init__(self, name, color="purple"):
#                 self.name = name
#                 self.color = color
#         self.assertEqual(
#             str(Thing("duck")),
#             "Thing(name='duck', color='purple')",
#         )

#     def test_with_property(self):
#         from reprtools import auto_repr

#         @auto_repr
#         class BankAccount:

#             current_id = 0

#             def __init__(self, balance=0):
#                 self._balance = balance
#                 BankAccount.current_id += 1
#                 self.account_id = BankAccount.current_id

#             @property
#             def balance(self):
#                 return self._balance

#         self.assertEqual(
#             str(BankAccount()),
#             "BankAccount(balance=0)",
#         )
#         self.assertEqual(
#             str(BankAccount(5)),
#             "BankAccount(balance=5)",
#         )

#     def test_argument_without_an_attribute(self):
#         from reprtools import auto_repr

#         @auto_repr
#         class BankAccount:

#             def __init__(self, opening_balance):
#                 self.balance = opening_balance

#         with self.assertRaises(TypeError):
#             str(BankAccount(10))

#         with self.assertRaises(TypeError):
#             repr(BankAccount(10))

#     def test_default_argument_without_an_attribute(self):
#         from reprtools import auto_repr

#         @auto_repr
#         class BankAccount:

#             current_id = 0

#             def __init__(self, balance=0, custom_id=None):
#                 self._balance = balance
#                 if not custom_id:
#                     BankAccount.current_id += 1
#                     custom_id = BankAccount.current_id
#                 self.account_id = custom_id

#             @property
#             def balance(self):
#                 return self._balance

#         self.assertEqual(
#             str(BankAccount(custom_id=10)),
#             "BankAccount(balance=0)",
#         )
#         self.assertEqual(
#             str(BankAccount(5)),
#             "BankAccount(balance=5)",
#         )
