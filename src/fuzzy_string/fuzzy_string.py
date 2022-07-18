from typing import Optional, TypeVar

T = TypeVar('T')


def test_equal(res: T, expected_res: T) -> None:
    assert res == expected_res, f"Wrong result, got:\n\t{res}\nbut expected\n\t {expected_res}"


def main():
    # Base exercise:
    print("Testing the base exercise")

    # Bonus 1
    print("Testing bonus 1")
    # try:
    #     record.title = "149S"
    #     raise Exception("Should have raised an AttributeError but did not.")
    # except AttributeError:
    #     pass

    # Bonus 2
    print("Testing bonus 2")

    # Bonus 3
    print("Testing bonus 3")

    print("Passed the tests!")


if __name__ == "__main__":
    main()
