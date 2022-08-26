from collections.abc import Iterator
from dataclasses import dataclass


@dataclass(slots=True)
class Vector:
    x: float
    y: float
    z: float

    def __iter__(self) -> Iterator[float]:
        return iter((self.x, self.y, self.z))


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


if __name__ == "__main__":
    main()
