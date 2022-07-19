"""Tests for the FuzzyString exercise using Pytest."""
import pytest

from src.fuzzy_string.fuzzy_string import FuzzyString


def test_equality_and_inequality_with_same_string():
    hello = FuzzyString("hello")
    assert hello == "hello"
    assert not hello != "hello"


def test_equality_with_completely_different_string():
    assert FuzzyString("hello") != "Hello there"


def test_equality_and_inequality_with_different_case_string():
    hello = FuzzyString("hellO")
    assert hello == "Hello"
    assert not hello != "Hello"
    assert hello == "HELLO"
    assert not hello != "HELLO"


def test_string_representation():
    hello = "heLlO"
    hello_fuzzy = FuzzyString(hello)
    assert str(hello_fuzzy) == hello
    assert repr(hello_fuzzy) == repr(hello)


@pytest.mark.bonus1
class TestBonus1:
    def test_string_comparisons(self):
        apple = FuzzyString("Apple")
        assert apple > "animal"
        assert "animal" < apple
        assert not apple < "animal"
        assert not "animal" > apple
        assert apple >= "animal"
        assert apple >= "apple"
        assert "animal" <= apple
        assert "animal" <= "animal"
        assert not apple <= "animal"
        assert not "animal" >= apple

    def test_fuzzy_string_comparisons(self):
        """Additional test between the FuzzyString objects."""
        tashkent = FuzzyString("Tashkent")
        taipei = FuzzyString("taipei")

        assert tashkent > taipei
        assert taipei < tashkent
        assert not tashkent < taipei
        assert not taipei > tashkent
        assert tashkent >= taipei
        assert tashkent >= tashkent
        assert taipei <= tashkent
        assert taipei <= taipei
        assert not tashkent <= taipei
        assert not taipei >= tashkent


@pytest.mark.bonus2
class TestBonus2:
    def test_string_operators(self):
        hello = FuzzyString("heLlO")
        assert hello + "!" == "helLo!"
        assert hello + "!" != "hello"
        assert "He" in hello
        assert "He!" not in hello

    def test_fuzzy_string_operators(self):
        """Additional test between the FuzzyString objects."""
        new_delhi = FuzzyString("NeW DELhi")
        new = FuzzyString("New")
        delhi = FuzzyString("Delhi")
        assert new + " " + delhi == new_delhi
        assert new + delhi != new_delhi
        assert delhi in new_delhi
        assert new in new_delhi


@pytest.mark.bonus3
class TestBonus3:
    def test_normalizes_strings(self):
        string = FuzzyString("\u00df and ss")
        assert string == "ss and \u00df"
        string = FuzzyString("ß, ss, \uf9fb, and \u7099")
        assert string == "ss, ß, \u7099, and \uf9fb"

        accent = "\u0301"
        accented_e = FuzzyString("\u00e9")
        assert "\u0065\u0301" == accented_e
        assert accent in accented_e
