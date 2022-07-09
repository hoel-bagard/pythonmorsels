from typing import TypeVar

T = TypeVar('T')


class alias:  # noqa: N801
    def __init__(self, true_name: str, write: bool = False):
        self.true_name = true_name
        self.write = write

    def __set_name__(self, owner: object, alias_name: str):
        self.alias_name = alias_name

    def __get__(self, obj, objtype=None):
        return getattr(obj, self.true_name)

    def __set__(self, obj, value):
        if not self.write:
            raise AttributeError("can't set attribute")
        setattr(obj, self.true_name, value)


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
    try:
        record.title = "149S"
        raise Exception("Should have raised an AttributeError but did not.")
    except AttributeError:
        pass

    # Bonus 2
    class DataRecord:
        title = alias("serial", write=True)

        def __init__(self, serial):
            self.serial = serial
    record = DataRecord("148X")
    record.title = "149S"
    test_equal(record.serial, "149S")

    print("Passed the tests!")


if __name__ == "__main__":
    main()
