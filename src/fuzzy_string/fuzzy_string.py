import unicodedata
from collections import UserString
from typing import TypeVar

T = TypeVar('T')


class FuzzyString(UserString):
    @staticmethod
    def _preprocess_str(string: str | "FuzzyString") -> str:
        return unicodedata.normalize("NFKD", str(string.casefold()))

    def __eq__(self, other: str | "FuzzyString" | object) -> bool:
        if isinstance(other, (str, FuzzyString)):
            return self._preprocess_str(self.data) == self._preprocess_str(other)
        return NotImplemented

    def __lt__(self, other: str | "FuzzyString" | object) -> bool:
        if isinstance(other, (str, FuzzyString)):
            return self._preprocess_str(self.data) < self._preprocess_str(other)
        return NotImplemented

    def __gt__(self, other: str | "FuzzyString" | object) -> bool:
        if isinstance(other, (str, FuzzyString)):
            return self._preprocess_str(self.data) > self._preprocess_str(other)
        return NotImplemented

    def __ge__(self, other: str | "FuzzyString" | object) -> bool:
        if isinstance(other, (str, FuzzyString)):
            return self._preprocess_str(self.data) >= self._preprocess_str(other)
        return NotImplemented

    def __le__(self, other: str | "FuzzyString" | object) -> bool:
        if isinstance(other, (str, FuzzyString)):
            return self._preprocess_str(self.data) <= self._preprocess_str(other)
        return NotImplemented

    def __add__(self, other: str | "FuzzyString" | object) -> "FuzzyString":
        if isinstance(other, (str, FuzzyString)):
            return FuzzyString(self.data + other)
        return NotImplemented

    def __contains__(self, other: str | "FuzzyString" | object) -> bool:
        if isinstance(other, (str, FuzzyString)):
            return str(self._preprocess_str(other)) in self._preprocess_str(self.data)
        return NotImplemented


def assert_equal(res: T, expected_res: T) -> None:
    assert res == expected_res, f"Wrong result, got:\n\t{res}\nbut expected\n\t {expected_res}"


def main():
    # Base exercise:
    print("Testing the base exercise")
    greeting = FuzzyString("Hey!")
    assert_equal(greeting, "hey!")
    assert_equal(greeting == "hey", False)
    # print(greeting)

    # Bonus 1
    print("Testing bonus 1")
    greeting = FuzzyString("Ohayou")
    assert "hashtag" < greeting
    assert not "hashtag" > greeting

    tokyo = FuzzyString("tokyo")
    toronto = FuzzyString("TORONTO")
    assert tokyo < toronto
    assert not toronto < tokyo

    # Bonus 2
    print("Testing bonus 2")
    beginning = FuzzyString("Beginning")
    assert "BEGI" in beginning
    concat_string = beginning + "End"
    assert concat_string == "beginningEnd"

    city_name = FuzzyString("New Delhi")
    city_name_part = FuzzyString("w del")
    assert city_name_part in city_name

    # Bonus 3
    print("Testing bonus 3")
    ss = FuzzyString("ss")
    assert "\u00df" == ss
    e = FuzzyString("\u00e9")
    assert "\u0065\u0301" == e
    assert "\u0301" in e

    print("Passed the tests!")


if __name__ == "__main__":
    main()
