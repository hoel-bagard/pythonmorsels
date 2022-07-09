"""Tests for the alias exercise using Pytest."""
from typing import TypeVar

import pytest
from _pytest.fixtures import SubRequest

from src.alias.alias import alias


class AliasedClass1:
    alias_name = alias("true_name")

    def __init__(self, value):
        self.true_name = value


aliased_class2_base_value = 1


class AliasedClass2:
    true_name = aliased_class2_base_value
    alias_name = alias("true_name")


@pytest.fixture(scope="function")
def aliased_instance(request: SubRequest) -> AliasedClass1:
    return AliasedClass1(request.param)


@pytest.fixture(scope="function")
def aliased_instance2() -> AliasedClass2:
    return AliasedClass2()


@pytest.mark.parametrize("expected_value", [aliased_class2_base_value])
def test_mirrors_attribute_on_class(aliased_instance2, expected_value):
    assert aliased_instance2.true_name == aliased_instance2.alias_name == expected_value


@pytest.mark.parametrize("aliased_instance, expected_value",
                         [(v := 4, v), (v := "123", v)],
                         indirect=["aliased_instance"])
def test_mirrors_attribute_from_initializer(aliased_instance: AliasedClass1, expected_value: int | str):
    assert aliased_instance.true_name == aliased_instance.alias_name == expected_value


@pytest.mark.parametrize("aliased_instance, first_value, second_value",
                         [(v := 1, v, v+1), (v := "123", v, v+'1')],
                         indirect=["aliased_instance"])
def test_attribute_mirroring_maintained(aliased_instance, first_value: int | str, second_value: int | str):
    assert aliased_instance.true_name == aliased_instance.alias_name == first_value

    aliased_instance.true_name = second_value
    assert aliased_instance.true_name == aliased_instance.alias_name == second_value
    assert aliased_instance.alias_name != first_value


@pytest.mark.parametrize("aliased_instance, expected_value",
                         [(a := [], a),
                          (4, 4)],
                         indirect=["aliased_instance"])
def test_attribute_identity(aliased_instance: AliasedClass1, expected_value: int):
    assert aliased_instance.true_name is expected_value
    assert aliased_instance.alias_name is expected_value


@pytest.mark.bonus1
class TestBonus1:
    @pytest.mark.parametrize("aliased_instance, original_value",
                             [(v := 1, v),
                              (v := [1, 2], v)],
                             indirect=["aliased_instance"])
    def test_attribute_unwritable_by_default(self, aliased_instance: AliasedClass1, original_value: int | list[int]):
        with pytest.raises(AttributeError):
            aliased_instance.alias_name = 1
        assert aliased_instance.true_name == aliased_instance.alias_name == original_value


# @pytest.mark.bonus2
# class TestBonus2:
#     def test_writable_attribute(self):
#         class Thing2:
#             blue = alias('red', write=True)
#             red = []
#         thing2 = Thing2()
#         self.assertIs(thing2.blue, thing2.red)
#         thing2.blue = [4, 5]
#         self.assertEqual(thing2.blue, [4, 5])
#         self.assertIs(thing2.blue, thing2.red)

#         # write=False raises an AttributeError (mutation works though)
#         class Thing3:
#             blue = alias('red', write=False)
#             red = []
#         thing3 = Thing3()
#         with self.assertRaises(AttributeError):
#             thing3.blue = [4, 5]
#         thing3.blue.append(6)
#         self.assertEqual(thing3.blue, [6])
#         self.assertIs(thing3.blue, thing3.red)


# # To test bonus 3, comment out the next line
# @unittest.expectedFailure
# def test_attribute_mirrored_on_class(self):
#     class Thing:
#         one = 4
#         two = alias('one')
#     self.assertEqual(Thing.one, 4)
#     self.assertEqual(Thing.two, 4)
