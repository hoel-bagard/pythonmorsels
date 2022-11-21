from __future__ import annotations

from collections import UserDict
from typing import Iterable, TYPE_CHECKING


if TYPE_CHECKING:
    from _typeshed import SupportsKeysAndGetItem


class PermaDict(UserDict[str, str]):
    def __init__(self,
                 *args: Iterable[tuple[str, str]] | SupportsKeysAndGetItem[str, str],
                 silent: bool = False,
                 **kwargs: dict[str, str]):
        super().__init__(*args, **kwargs)  # type: ignore
        self.silent = silent

    def __setitem__(self, key: str, value: str):
        if key not in self.keys():
            super().__setitem__(key, value)
        elif not self.silent:
            raise KeyError(f"'{key}' already in dictionary")

    def force_set(self, key: str, value: str):
        super().__setitem__(key, value)

    def update(self,
               *args: Iterable[tuple[str, str]] | SupportsKeysAndGetItem[str, str],
               force: bool = False,
               **kwargs: dict[str, str]) -> None:
        if force:
            return self.data.update(*args, **kwargs)
        else:
            return super().update(*args, **kwargs)


def main():
    # Base exercise:
    # The PermaDict class should allow keys to be added and deleted, just like any other dictionary:
    locations = PermaDict({"Trey": "San Diego", "Al": "San Francisco"})
    locations["Harry"] = "London"
    locations.update({"Russell": "Perth", "Katie": "Sydney"})
    res, expected_res = locations["Trey"], "San Diego"
    assert res == expected_res, f"Wrong result, got:\n\t{res}\nbut expected\n\t {expected_res}"

    # PermaDict class should have keys, values, and items methods and should be iterable just like a dictionary:
    locations = PermaDict([("Kojo", "Houston"), ("Tracy", "Toronto")])
    res, expected_res = list(locations), ["Kojo", "Tracy"]
    assert res == expected_res, f"Wrong result, got:\n\t{res}\nbut expected\n\t {expected_res}"
    res, expected_res = list(locations.keys()), ["Kojo", "Tracy"]
    assert res == expected_res, f"Wrong result, got:\n\t{res}\nbut expected\n\t {expected_res}"
    res, expected_res = list(locations.values()), ["Houston", "Toronto"]
    assert res == expected_res, f"Wrong result, got:\n\t{res}\nbut expected\n\t {expected_res}"
    # for name, place in locations.items():
    #     print(f"{name} in {place}")

    # Unlike a dictionary when a value is set and for a key that already exists, a KeyError exception should be raised:
    locations = PermaDict({"David": "Boston"})
    try:
        locations["David"] = "Amsterdam"
        raise Exception("Should have raised a KeyError but did not.")
    except KeyError:
        pass

    # Bonus 1
    # Add a force_set method to your PermaDict class which allows keys to be updated without error.
    locations = PermaDict({"David": "Boston"})
    locations.force_set("David", "Amsterdam")
    locations.force_set("Asheesh", "Boston")
    locations.force_set("Asheesh", "San Francisco")
    res, expected_res = locations, {"David": "Amsterdam", "Asheesh": "San Francisco"}
    assert res == expected_res, f"Wrong result, got:\n\t{res}\nbut expected\n\t {expected_res}"

    # Bonus 2
    # Handle an optional silent keyword argument passed to the initializer of your dictionary to allow your dictionary
    # to silently ignore updates to existing keys (when silent is True).
    locations = PermaDict({"David": "Boston"}, silent=True)
    locations["David"] = "Amsterdam"
    locations["Asheesh"] = "Boston"
    res, expected_res = locations, {"David": "Boston", "Asheesh": "Boston"}
    assert res == expected_res, f"Wrong result, got:\n\t{res}\nbut expected\n\t {expected_res}"

    # Bonus 3
    # Make PermaDict class's update method to handle an optional force keyword argument
    # to allow your dictionary's update method to force update the values for existing keys.
    locations = PermaDict({"David": "Boston"})
    locations.update([("David", "Amsterdam"), ("Asheesh", "SF")], force=True)
    res, expected_res = locations, {"David": "Amsterdam", "Asheesh": "SF"}
    assert res == expected_res, f"Wrong result, got:\n\t{res}\nbut expected\n\t {expected_res}"

    print("Passed the tests")


if __name__ == "__main__":
    main()
