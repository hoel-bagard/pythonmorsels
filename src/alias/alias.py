from typing import TypeVar

T = TypeVar('T')


class alias:  # noqa: N801
    def __init__(self, true_name: str):
        self.true_name = true_name

    def __set_name__(self, owner: object, alias_name: str):
        self.alias_name = alias_name

    def __get__(self, obj, objtype=None):
        return getattr(obj, self.true_name)


def test_equal(res: T, expected_res: T) -> None:
    assert res == expected_res, f"Wrong result, got:\n\t{res}\nbut expected\n\t {expected_res}"


def main():
    # Base exercise:
    class DataRecord:
        title = alias("serial")

        def __init__(self, serial):
            self.serial = serial

    record = DataRecord("148X")
    test_equal(record.title, "148X")
    record.serial = "149S"
    test_equal(record.title, "149S")

    # Bonus 1

    # Bonus 2

    print("Passed the tests!")


if __name__ == "__main__":
    main()
