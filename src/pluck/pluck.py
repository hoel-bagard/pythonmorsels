from typing import TypeVar

T = TypeVar("T")
D = TypeVar("D")
NestedDict = dict[str, "NestedDict[T]" | T]


def pluck(nested_dict: NestedDict[T],
          *key_paths: str,
          sep: str = ".",
          default: D = (PLUCK_NO_DEFAULT := object())  # noqa: N806 B008
          ) -> tuple[NestedDict[T] | T | D, ...] | NestedDict[T] | T | D:
    if len(key_paths) > 1:
        return tuple(pluck(nested_dict, key_path, sep=sep, default=default) for key_path in key_paths)

    key_path = key_paths[0]
    partial_dict: NestedDict[T] | T = nested_dict
    for key in key_path.split(sep):
        try:
            if isinstance(partial_dict, dict):
                partial_dict = partial_dict[key]
            else:
                raise KeyError(f"Key {repr(key)} not found.")
        except KeyError:
            if default is not PLUCK_NO_DEFAULT:
                return default  # type: ignore  # Not sure how to fix typing here.
            raise
    return partial_dict


def test_equal(res: object, expected_res: object) -> None:
    assert res == expected_res, f"Wrong result, got:\n\t{res}\nbut expected\n\t {expected_res}"


def main():
    data: NestedDict[str] = {"amount": "10.64", "category": {"name": "Music", "group": "Fun"}}

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

    print("Passed the tests.")


if __name__ == "__main__":
    main()
