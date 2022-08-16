from collections import OrderedDict
from collections.abc import Iterator
from typing import Generic, Optional, TypeVar

T = TypeVar('T')


class Unpacker(Generic[T]):
    def __init__(self, input_dict: Optional[dict[str, T]] = None):
        self.data_dict = input_dict.copy() if input_dict is not None else {}

    def __setitem__(self, key: str | tuple[str], value: T | tuple[T]):
        if isinstance(key, tuple):
            value = list(value)
            if len(key) != len(value):
                raise ValueError
            for k, v in zip(key, value, strict=True):
                self.data_dict[k] = v
        else:
            self.data_dict[key] = value

    def __getitem__(self, key: str | tuple[str]):
        if isinstance(key, tuple):
            return tuple(self.data_dict[k] for k in key)
        return self.data_dict[key]

    def __getattr__(self, key: str) -> T:
        return self.data_dict[key]

    def __setattr__(self, key: str, value: T) -> None:
        if key != "data_dict":
            self.data_dict[key] = value
        else:
            super.__setattr__(self, key, value)

    def __iter__(self) -> Iterator[T]:
        yield from self.data_dict.values()

    def __repr__(self):
        return f"{type(self).__name__}({', '.join([f'{attr}={repr(val)}' for attr, val in self.data_dict.items()])})"


def assert_equal(res: object, expected_res: object) -> None:
    assert res == expected_res, f"Wrong result, got:\n\t{res}\nbut expected\n\t {expected_res}"


def main():
    # Base exercise:
    d = {'hello': 4, 'hi': 5}
    u = Unpacker(d)
    assert_equal(u['hello'], 4)
    assert_equal(u.hi, 5)

    u['hello'] = 8
    assert_equal(u.hello, 8)
    u.hello = 5
    assert_equal(u.hello, 5)

    # Bonus 1
    coordinates = OrderedDict([('x', 34), ('y', 67)])
    point = Unpacker(coordinates)
    x_axis, y_axis = point
    assert_equal(x_axis, 34)
    assert_equal(y_axis, 67)

    # Bonus 2
    row = Unpacker({'a': 234, 'b': 54})
    row['a'] = 11
    row['c'] = 45
    assert_equal(str(row), "Unpacker(a=11, b=54, c=45)")

    # Bonus 3
    row = Unpacker({'a': 234, 'b': 54})
    assert_equal(row['a', 'b'], (234, 54))
    row['b', 'a'] = (11, 22)
    assert_equal(str(row), "Unpacker(a=22, b=11)")
    print("Passed the tests")


if __name__ == "__main__":
    main()
