import math
from typing import Optional, TypeVar

TFloatRange = TypeVar("TFloatRange", bound="float_range")


class float_range:  # noqa: N801
    def __init__(self, start: float, stop: Optional[float] = None, step: float = 1):
        self.start = start if stop is not None else 0
        self.stop = stop if stop is not None else start
        self.step = step
        self.current = self.start
        self.step_sign = 1 if step >= 0 else -1
        self.is_ascending = self.stop - self.start > 0

    def __getitem__(self, key: int | slice):
        if isinstance(key, int):
            if key >= 0 and self.step_sign*(result := self.start + key*self.step) < self.stop:
                return result
            elif key < 0 and self.start <= self.step_sign*(result := self.start + len(self)*self.step + key*self.step):
                return result
            raise IndexError("float_range index out of range")
        elif isinstance(key, slice):
            if key.start is not None:
                start = self[key.start] if abs(key.start) < len(self) else self.stop
            else:
                start = self.start
            stop = self[key.stop] if key.stop is not None and key.stop < len(self) else self.stop
            step = key.step * self.step if key.step is not None else self.step
            print((start, stop, step))
            return float_range(start, stop, step)

    def __iter__(self):
        while (((self.is_ascending and self.current < self.stop)
                or (not self.is_ascending and self.stop < self.current))
                and self.step_sign*(self.stop - self.start) > 0):
            yield self.current
            self.current += self.step
        self.current = self.start

    def __len__(self):
        return max(0, math.ceil((self.stop-self.start) / self.step))

    def __eq__(self, other: object):
        if isinstance(other, float_range | range):
            if len(self) == len(other) == 0:
                return True
            elif len(self) == len(other) == 1:
                return self.start == other.start
            return (self.start == other.start
                    and self.step == other.step
                    and len(self) == len(other))
        return NotImplemented

    def __repr__(self):
        return f"float_range({self.start}, {self.stop}, {self.step})"


def test_equal(res, expected_res):
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
    test_equal(list(my_range[:2]), [0.5, 1.25])
    test_equal(list(my_range[-1:100]), [6.5])
    test_equal(list(my_range[-3:]), [5.0, 5.75, 6.5])
    test_equal(list(my_range[::2]), [0.5, 2.0, 3.5, 5.0, 6.5])

    print("Passed the tests.")


if __name__ == "__main__":
    main()
