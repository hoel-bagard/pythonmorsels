"""Tests for the Unpacker exercise using Pytest."""
import pytest

from src.vector.vector import Vector


@pytest.fixture
def tuple_sample() -> tuple[float, float, float]:
    return 1, 2, 3


@pytest.fixture
def vector_sample(tuple_sample) -> Vector:
    return Vector(*tuple_sample)


def test_attributes(vector_sample: Vector, tuple_sample: tuple[int, int, int]):
    assert (vector_sample.x, vector_sample.y, vector_sample.z) == tuple_sample


def test_equality_and_inequality(vector_sample: Vector, tuple_sample: tuple[int, int, int]):
    assert vector_sample != Vector(1, 2, tuple_sample[2]+1)
    assert vector_sample == Vector(*tuple_sample)
    assert not vector_sample != Vector(*tuple_sample)


def test_iterable_vector(vector_sample: Vector, tuple_sample):
    x, y, z = vector_sample
    assert (x, y, z) == tuple_sample


def test_no_weird_extras():
    v1 = Vector(1, 2, 3)
    v2 = Vector(4, 5, 6)
    with pytest.raises(TypeError):
        len(v1)
    with pytest.raises(TypeError):
        v1 < v2
    with pytest.raises(TypeError):
        v1 > v2
    with pytest.raises(TypeError):
        v1 <= v2
    with pytest.raises(TypeError):
        v1 >= v2
    with pytest.raises(TypeError):
        v1 + (1, 2, 3)
    with pytest.raises(TypeError):
        (1, 2, 3) + v1
    with pytest.raises(TypeError):
        v1 - (1, 2, 3)
    with pytest.raises(TypeError):
        v1 * 'a'
    with pytest.raises(TypeError):
        v1 / v2


def test_memory_efficient_attributes(vector_sample: Vector):
    with pytest.raises((AttributeError, TypeError)):
        vector_sample.a = 3
    with pytest.raises((AttributeError, TypeError)):
        vector_sample.__dict__

    # # To test bonus 1, comment out the next line
    # @unittest.expectedFailure
    # def test_shifting(self):
    #     v1 = Vector(1, 2, 3)
    #     v2 = Vector(4, 5, 6)
    #     v3 = v2 + v1
    #     v4 = v3 - v1
    #     self.assertEqual((v3.x, v3.y, v3.z), (5, 7, 9))
    #     self.assertEqual((v4.x, v4.y, v4.z), (v2.x, v2.y, v2.z))

    # # To test bonus 2, comment out the next line
    # @unittest.expectedFailure
    # def test_scaling(self):
    #     v1 = Vector(1, 2, 3)
    #     v2 = Vector(4, 5, 6)
    #     v3 = v1 * 4
    #     v4 = 2 * v2
    #     v5 = v3 / 2
    #     self.assertEqual((v3.x, v3.y, v3.z), (4, 8, 12))
    #     self.assertEqual((v4.x, v4.y, v4.z), (8, 10, 12))
    #     self.assertEqual((v5.x, v5.y, v5.z), (2, 4, 6))

    # # To test bonus 3, comment out the next line
    # @unittest.expectedFailure
    # def test_immutable(self):
    #     v1 = Vector(1, 2, 3)
    #     with self.assertRaises(Exception):
    #         v1.x = 4
    #     self.assertEqual(v1.x, 1)

