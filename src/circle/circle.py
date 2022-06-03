import math


class Circle:
    def __init__(self, radius: float = 1):
        self.radius = radius

    def __repr__(self):
        return f"Circle({self.radius})"

    @property
    def area(self):
        return math.pi * self.radius**2

    @property
    def diameter(self):
        return 2 * self.radius

    # Bonus 2
    @diameter.setter
    def diameter(self, diameter: float):
        self.radius = diameter / 2

    # Bonus 3
    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius: float):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = radius


if __name__ == "__main__":
    # Main exercise
    c = Circle(5)
    print(c)
    assert c.radius == 5, "Wrong radius"
    assert c.diameter == 10, "Wrong diameter"
    assert c.area == 78.53981633974483, "Wrong area"

    c = Circle()
    assert c.radius == 1, "Wrong radius"
    assert c.diameter == 2, "Wrong diameter"

    # Bonus 1
    c = Circle(2)
    c.radius = 1
    assert c.diameter == 2, "Wrong diameter"
    assert c.area == 3.141592653589793, "Wrong area"

    # Bonus 2
    c = Circle(1)
    c.diameter = 4
    assert c.radius == 2, "Wrong radius"
    try:
        c.area = 45.678
        raise Exception("Should have raised an AttributeError")
    except AttributeError:
        pass

    # Bonus 3
    c = Circle(5)
    c.radius = 3
    try:
        c.radius = -2
        raise Exception("Should have raised a ValueError")
    except ValueError:
        pass

    print("Passed the tests")

