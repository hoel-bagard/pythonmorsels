from collections import OrderedDict


class Unpacker:
    def __init__(self, input_dict: OrderedDict | dict):
        self.data_dict = input_dict

    def __setitem__(self, key: str | tuple[str], value: object | tuple[object]):
        if isinstance(key, tuple):
            for k, v in zip(key, value):
                self.data_dict[k] = v
        else:
            self.data_dict[key] = value

    def __getitem__(self, key: str | tuple[str]):
        if isinstance(key, tuple):
            return tuple(self.data_dict[k] for k in key)
        return self.data_dict[key]

    def __getattr__(self, key: str):
        return self.data_dict[key]

    def __iter__(self):
        yield from self.data_dict.values()

    def __repr__(self):
        return f"{type(self).__name__}({', '.join([f'{attr}={value}' for attr, value in self.data_dict.items()])})"


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
