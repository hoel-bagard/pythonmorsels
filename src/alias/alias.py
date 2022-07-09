from typing import Optional, TypeVar

T = TypeVar('T')


class alias:  # noqa: N801
    def __init__(self, true_name: str, write: bool = False):
        self.true_name = true_name
        self.write = write

    def __set_name__(self, owner: object, alias_name: str):
        self.alias_name = alias_name

    def __get__(self, obj: Optional[object], objtype: Optional[type] = None) -> object:
        if obj is not None:
            return getattr(obj, self.true_name)
        else:
            return getattr(objtype, self.true_name)

    def __set__(self, obj: object, value: object) -> None:
        if not self.write:
            raise AttributeError(f"{repr(self.alias_name)} is an alias an cannot be set.")
        setattr(obj, self.true_name, value)


def test_equal(res: T, expected_res: T) -> None:
    assert res == expected_res, f"Wrong result, got:\n\t{res}\nbut expected\n\t {expected_res}"


def main():
    # Base exercise:
    print("Testing the base exercise")

    class DataRecord:
        title = alias("serial")

        def __init__(self, serial: str):
            self.serial = serial

    record = DataRecord("148X")
    test_equal(record.title, "148X")
    record.serial = "149S"
    test_equal(record.title, "149S")

    # Bonus 1
    print("Testing bonus 1")
    try:
        record.title = "149S"
        raise Exception("Should have raised an AttributeError but did not.")
    except AttributeError:
        pass

    # Bonus 2
    print("Testing bonus 2")

    class DataRecord2:
        title = alias("serial", write=True)

        def __init__(self, serial: str):
            self.serial = serial
    record = DataRecord2("148X")
    record.title = "149S"
    test_equal(record.serial, "149S")

    # Bonus 3
    print("Testing bonus 3")

    class RegisteredObject:
        _registry = ()
        registry = alias("_registry")

        def __init__(self, name: str):
            RegisteredObject._registry += (self,)
            self.name = name

    _registered_object = RegisteredObject("Bonus3")  # noqa: F841
    assert len(RegisteredObject.registry) == 1  # type: ignore

    print("Passed the tests!")


if __name__ == "__main__":
    main()
