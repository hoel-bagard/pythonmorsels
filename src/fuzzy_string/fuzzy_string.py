from collections import UserString
from typing import TypeVar

T = TypeVar('T')


class FuzzyString(UserString):
    def __init__(self, data: str):
        self.data = data

    def __eq__(self, other: str):
        return self.data.lower() == other.lower()


def assert_equal(res: T, expected_res: T) -> None:
    assert res == expected_res, f"Wrong result, got:\n\t{res}\nbut expected\n\t {expected_res}"


def main():
    # Base exercise:
    print("Testing the base exercise")
    greeting = FuzzyString("Hey!")
    assert_equal(greeting, "hey!")
    assert_equal(greeting == "hey", False)
    print(greeting)

    # Bonus 1
    print("Testing bonus 1")

    # Bonus 2
    print("Testing bonus 2")

    # Bonus 3
    print("Testing bonus 3")

    print("Passed the tests!")


if __name__ == "__main__":
    main()
