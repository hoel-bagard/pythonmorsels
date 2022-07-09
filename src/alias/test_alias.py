"""Tests for the alias exercise using Pytest."""
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


@pytest.mark.bonus2
class TestBonus2:
    @pytest.mark.parametrize("original_value, mutated_value",
                             [(4321, 1234),
                              ("test", "success"),
                              (None, [])])
    def test_writable_attribute(self, original_value, mutated_value):
        AliasedClass1.writeable = alias("true_name", write=True)
        aliased_instance = AliasedClass1(original_value)
        assert aliased_instance.writeable == aliased_instance.true_name == original_value
        aliased_instance.writeable = mutated_value
        assert aliased_instance.writeable == aliased_instance.true_name == mutated_value
        assert aliased_instance.writeable is aliased_instance.true_name

    @pytest.mark.parametrize("original_value, append_value", [([1, 2, 3], 4)])
    def test_non_writable_attribute(self, original_value: list[int], append_value: int):
        """Check that write=False raises an AttributeError but mutation works."""
        AliasedClass1.non_writeable = alias("true_name", write=False)
        aliased_instance = AliasedClass1(original_value)

        assert aliased_instance.non_writeable == aliased_instance.true_name == original_value
        with pytest.raises(AttributeError):
            aliased_instance.non_writeable = None

        expected_mutated_value = original_value.copy()
        expected_mutated_value.append(append_value)
        aliased_instance.non_writeable.append(append_value)
        assert aliased_instance.writeable == aliased_instance.true_name == expected_mutated_value
        assert aliased_instance.non_writeable is aliased_instance.true_name


@pytest.mark.bonus2
class TestBonus3:
    def test_attribute_mirrored_on_class(self):
        class AliasedClass3:
            true_name = "Bonus3"
            alias_name = alias("true_name")
        assert AliasedClass3.true_name == AliasedClass3.alias_name == "Bonus3"
