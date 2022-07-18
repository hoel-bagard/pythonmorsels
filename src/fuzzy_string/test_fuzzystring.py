from src.fuzzy_string.fuzzy_string import FuzzyString


def test_equality_and_inequality_with_same_string():
    hello = FuzzyString("hello")
    assert hello == "hello"
    assert not hello != "hello"


def test_equality_with_completely_different_string():
    hello = FuzzyString("hello")
    assert not hello == "Hello there"
    assert not hello == "Hello there"


def test_equality_and_inequality_with_different_case_string():
    hello = FuzzyString("hellO")
    assert hello == "Hello"
    assert not hello != "Hello"
    assert hello == "HELLO"
    assert not hello != "HELLO"


def test_string_representation():
    hello = FuzzyString("heLlO")
    assert str(hello) == "heLlO"
    assert repr(hello) == repr("heLlO")

    # # To test bonus 1, comment out the next line
    # def test_other_string_comparisons():
    #     apple = FuzzyString("Apple")
    #     .assertGreater(apple, "animal")
    #     .assertLess("animal", apple)
    #     assert not apple < "animal")
    #     assert not "animal" > apple)
    #     .assertGreaterEqual(apple, "animal")
    #     .assertGreaterEqual(apple, "apple")
    #     .assertLessEqual("animal", apple)
    #     .assertLessEqual("animal", "animal")
    #     assert not apple <= "animal")
    #     assert not "animal" >= apple)

    #     # Additional test between the FuzzyString objects

    #     tashkent = FuzzyString("Tashkent")
    #     taipei = FuzzyString("taipei")

    #     .assertGreater(tashkent, taipei)
    #     .assertLess(taipei, tashkent)
    #     assert not tashkent < taipei)
    #     assert not taipei > tashkent)
    #     .assertGreaterEqual(tashkent, taipei)
    #     .assertGreaterEqual(tashkent, tashkent)
    #     .assertLessEqual(taipei, tashkent)
    #     .assertLessEqual(taipei, taipei)
    #     assert not tashkent <= taipei)
    #     assert not taipei >= tashkent)

    # # To test bonus 2, comment out the next line
    # def test_string_operators(self):
    #     hello = FuzzyString("heLlO")
    #     selfassert hello + "!", "helLo!")
    #     selfassert not hello + "!", "hello")
    #     self.assertTrue("he" in hello)
    #     self.assertIn("He", hello)
    #     self.assertNotIn("He!", hello)

    #     # Additional test between the FuzzyString objects

    #     new_delhi = FuzzyString("NeW DELhi")
    #     new = FuzzyString("New")
    #     delhi = FuzzyString("Delhi")
    #     selfassert new + " " + delhi, new_delhi)
    #     selfassert not new + delhi, new_delhi)
    #     self.assertTrue(delhi in new_delhi)
    #     self.assertIn(new, new_delhi)

    # # To test bonus 3, comment out the next line
    # def test_normalizes_strings(self):
    #     string = FuzzyString("\u00df and ss")
    #     selfassert string, "ss and \u00df")
    #     string = FuzzyString("ß, ss, \uf9fb, and \u7099")
    #     selfassert string, "ss, ß, \u7099, and \uf9fb")

    #     accent = '\u0301'
    #     accented_e = FuzzyString('\u00e9')
    #     selfassert '\u0065\u0301', accented_e)
    #     self.assertIn(accent, accented_e)
