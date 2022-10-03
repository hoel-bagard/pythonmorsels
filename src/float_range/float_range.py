import math
from collections.abc import Iterable
from typing import Optional


class float_range(Iterable[float]):  # noqa: N801
    def __init__(self, start: float, stop: Optional[float] = None, step: float = 1):
        self.start = start if stop is not None else 0
        self.stop = stop if stop is not None else start
        self.step = step

    def _item(self, index: int) -> float:
        """Return item at given location, even if out of bounds."""
        return self.start + self.step*index

    def __getitem__(self, key: int | slice) -> float | "float_range":
        if isinstance(key, slice):
            start, stop, step = key.indices(len(self))
            return float_range(self._item(start), self._item(stop), self.step * step)
        if 0 <= key < len(self):
            return self._item(key)
        if -len(self) <= key < 0:
            return self._item(len(self) + key)
        raise IndexError(f"float_range index out of range: {key}")

    def __len__(self) -> int:
        return max(0, math.ceil((self.stop-self.start) / self.step))

    def __eq__(self, other: object) -> bool:
        if isinstance(other, (float_range, range)):
            if len(self) == len(other) == 0:
                return True
            return (self[0] == other[0]
                    and self[-1] == other[-1]
                    and len(self) == len(other))
        return NotImplemented

    def __repr__(self) -> str:
        return f"{type(self).__name__}({self.start}, {self.stop}, {self.step})"


def test_equal(res: object, expected_res: object) -> None:
    assert res == expected_res, f"Wrong result, got:\n\t{res}\nbut expected\n\t {expected_res}"


def main():
    # Base exercise:
    r = float_range(0.5, 2.5, 0.5)
    test_equal(list(r), [0.5, 1.0, 1.5, 2.0])
    test_equal(len(r), 4)

    test_equal(list(float_range(3.5, 0, -1)), [3.5, 2.5, 1.5, 0.5])
    test_equal(len(float_range(3.5, 0, -1)), 4)

    test_equal(len(float_range(0.0, 3.0)), 3)
    test_equal(list(float_range(3.0)), [0.0, 1.0, 2.0])

    # Bonus 1
    # For the first bonus, make float_range objects indexable and reversible:
    my_range = float_range(0.5, 7, 0.75)
    test_equal(my_range[1], 1.25)
    test_equal(my_range[-1], 6.5)
    try:
        my_range[10]
        raise Exception("Should have raised IndexError but did not.")
    except IndexError:
        pass
    test_equal(list(reversed(my_range)), [6.5, 5.75, 5.0, 4.25, 3.5, 2.75, 2.0, 1.25, 0.5])

    # Bonus 2
    # Make sure that you can take the object returned from float_range and ask if it's equal to
    # another object returned from float_range.
    a = float_range(0.5, 2.5, 0.5)
    b = float_range(0.5, 2.5, 0.5)
    c = float_range(0.5, 3.0, 0.5)
    test_equal(a == b, True)
    test_equal(a == c, False)

    # Take that a step further and make sure you can compare these objects to range objects also
    # and that other comparisons won't raise exceptions:
    test_equal(float_range(5) == range(0, 5), True)
    test_equal(float_range(4) == range(5), False)
    test_equal(float_range(4) == 3, False)

    # Bonus 3
    # For the third bonus, make the float_range objects sliceable:
    my_range = float_range(0.5, 7, 0.75)
    test_equal(list(my_range[:2]), [0.5, 1.25])  # type: ignore
    test_equal(list(my_range[-1:100]), [6.5])  # type: ignore
    test_equal(list(my_range[-3:]), [5.0, 5.75, 6.5])  # type: ignore
    test_equal(list(my_range[::2]), [0.5, 2.0, 3.5, 5.0, 6.5])  # type: ignore

    print("Passed the tests.")


if __name__ == "__main__":
    main()
