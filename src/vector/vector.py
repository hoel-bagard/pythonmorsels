from collections.abc import Iterator
from dataclasses import dataclass
from typing import TypeVar


TVector = TypeVar("TVector", bound="Vector")


@dataclass(slots=True, frozen=True)
class Vector:
    x: float
    y: float
    z: float

    def __iter__(self) -> Iterator[float]:
        return iter((self.x, self.y, self.z))

    def __add__(self, other: TVector | object) -> TVector:
        if isinstance(other, Vector):
            return Vector(self.x + other.x,
                          self.y + other.y,
                          self.z + other.z)
        return NotImplemented

    def __sub__(self, other: TVector | object) -> TVector:
        if isinstance(other, Vector):
            return Vector(self.x - other.x,
                          self.y - other.y,
                          self.z - other.z)
        return NotImplemented

    def __mul__(self, mult_factor: int | float | object) -> TVector:
        if isinstance(mult_factor, (float, int)):
            return Vector(self.x * mult_factor,
                          self.y * mult_factor,
                          self.z * mult_factor)
        return NotImplemented

    def __rmul__(self, mult_factor: int | float | object) -> TVector:
        return self * mult_factor

    def __truediv__(self, div_factor: int | float | object) -> TVector:
        if isinstance(div_factor, (float, int)):
            return Vector(self.x / div_factor,
                          self.y / div_factor,
                          self.z / div_factor)
        return NotImplemented


def assert_equal(res: object, expected_res: object) -> None:
    assert res == expected_res, f"Wrong result, got:\n\t{res}\nbut expected\n\t {expected_res}"


def main():
    # Base exercise:
    v = Vector(1, 2, 3)
    x, y, z = v
    assert_equal(x, 1)
    assert_equal(y, 2)
    assert_equal(z, 3)
    assert v != Vector(1, 2, 4)
    assert_equal(v, Vector(1, 2, 3))
    print("Passed base exercise")

    # Bonus 1
    assert_equal(Vector(1, 2, 3) + Vector(4, 5, 6), Vector(5, 7, 9))
    assert_equal(Vector(5, 7, 9) - Vector(3, 1, 2), Vector(2, 6, 7))
    print("Passed bonus 1")

    # Bonus 2
    assert_equal(3 * Vector(1, 2, 3), Vector(3, 6, 9))
    assert_equal(Vector(1, 2, 3) * 2, Vector(2, 4, 6))
    assert_equal(Vector(1, 2, 3) / 2, Vector(0.5, 1, 1.5))
    print("Passed bonus 2")

    # Bonus 2
    v = Vector(1, 2, 3)
    try:
        v.x = 4
        raise TypeError("Vectors should be immutable")
    except AttributeError:
        pass
    print("Passed bonus 3")

    print("Passed the tests")


if __name__ == "__main__":
    main()
