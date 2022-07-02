from typing import TypeVar

T = TypeVar('T')
D = TypeVar('D')
NestedDict = dict[str, "NestedDict[T]" | T]
PLUCK_NO_DEFAULT = object()


def pluck(nested_dict: NestedDict[T],
          *paths: str,
          sep: str = '.',
          default: D = PLUCK_NO_DEFAULT) -> NestedDict[T] | T | D:
    if len(paths) > 1:
        return tuple(pluck(nested_dict, path, sep=sep, default=default) for path in paths)
    path = paths[0]
    for key in path.split(sep):
        try:
            nested_dict = nested_dict[key]
        except KeyError:
            if default is not PLUCK_NO_DEFAULT:
                return default
            raise
    return nested_dict


def test_equal(res, expected_res):
    assert res == expected_res, f"Wrong result, got:\n\t{res}\nbut expected\n\t {expected_res}"


def main():
    data = {"amount": 10.64, "category": {"name": "Music", "group": "Fun"}}

    # Base exercise:
    test_equal(pluck(data, "amount"), 10.64)
    test_equal(pluck(data, "category.group"), "Fun")
    try:
        pluck(data, "category.created")
        raise Exception("Should have raised a KeyError but did not.")
    except KeyError:
        pass

    # Bonus 1
    test_equal(pluck(data, "category/name", sep="/"), "Music")

    # Bonus 2
    test_equal(pluck(data, "category.created", default="N/A"), "N/A")

    # Bonus 3
    test_equal(pluck(data, "category.name", "amount"), ("Music", 10.64))


if __name__ == "__main__":
    main()
