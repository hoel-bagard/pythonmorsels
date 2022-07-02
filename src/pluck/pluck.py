from typing import TypeVar

T = TypeVar('T')
NestedDict = dict[str, "NestedDict[T]" | T]


def pluck(nested_dict: NestedDict, path: str):
    for key in path.split('.'):
        nested_dict = nested_dict[key]
    return nested_dict


def test_equal(res, expected_res):
    assert res == expected_res, f"Wrong result, got:\n\t{res}\nbut expected\n\t {expected_res}"


def main():
    # Base exercise:
    data = {"amount": 10.64, "category": {"name": "Music", "group": "Fun"}}
    test_equal(pluck(data, "amount"), 10.64)
    test_equal(pluck(data, "category.group"), "Fun")
    try:
        pluck(data, "category.created")
        raise Exception("Should have raised a KeyError but did not.")
    except KeyError:
        pass


if __name__ == "__main__":
    main()
