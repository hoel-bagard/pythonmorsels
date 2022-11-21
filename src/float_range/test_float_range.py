# type: ignore
import sys
from collections.abc import Generator
from functools import partial
from timeit import timeit

import pytest

from src.float_range.float_range import float_range


@pytest.mark.parametrize("start, stop, step, res",
                         [(1, 11, 2, [1, 3, 5, 7, 9]),
                          (0.5, 7, 0.75, [0.5, 1.25, 2.0, 2.75, 3.5, 4.25, 5.0, 5.75, 6.5]),
                          ])
def test_has_iterability(start: float, stop: float, step: float, res: list[float]):
    assert list(float_range(start, stop, step)) == res


@pytest.mark.parametrize("start, stop, res",
                         [(1, 6, [1, 2, 3, 4, 5]),
                          (0.5, 6, [0.5, 1.5, 2.5, 3.5, 4.5, 5.5]),
                          ])
def test_optional_step(start: float, stop: float, res: list[float]):
    assert list(float_range(start, stop)) == res


@pytest.mark.parametrize("stop, res",
                         [(6, [0, 1, 2, 3, 4, 5]),
                          (4.2, [0, 1, 2, 3, 4]),
                          ])
def test_optional_start(stop: float, res: list[float]):
    assert list(float_range(0, stop)) == res
    assert list(float_range(stop)) == res


def test_string_representation():
    assert str(float_range(0, 6, 0.5)) == "float_range(0, 6, 0.5)"
    assert repr(float_range(0, 6)) == "float_range(0, 6, 1)"


@pytest.mark.parametrize("start, stop, step, res",
                         [(1, 6, 0.5, [1, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5]),
                          (1, 5.6, 0.5, [1, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5]),
                          ])
def test_fractional_step_size(start: float, stop: float, step: float, res: list[float]):
    assert list(float_range(start, stop, step)) == res


def test_negative_step():
    with pytest.raises(StopIteration):
        # Should be empty so StopIteration should be raised
        next(iter(float_range(1, 6, -1)))
    assert list(float_range(5, 0, -1)) == [5, 4, 3, 2, 1]
    assert list(float_range(0.5, 6)) == [0.5, 1.5, 2.5, 3.5, 4.5, 5.5]
    assert list(float_range(6, 1, -0.5)) == [6, 5.5, 5.0, 4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5]


def test_no_arguments():
    with pytest.raises(TypeError):
        float_range()


def test_too_many_arguments():
    with pytest.raises(TypeError):
        float_range(0, 5, 1, 1)
    with pytest.raises(TypeError):
        float_range(0, 5, 1, 1, 1)


def test_no_memory_used():
    """Make sure float_range response isn't a giant list of numbers."""
    response = float_range(0, 1024, 2**-4)
    if isinstance(response, Generator):
        next(response)
        size = sum(sys.getsizeof(obj) for obj in response.gi_frame.f_locals.values())
    else:
        size = sys.getsizeof(response)
    assert size < 8000, "Too much memory used"
    assert not isinstance(response, list)
    assert not isinstance(response, tuple)


def test_can_be_looped_over_multiple_times():
    expected = [0.5, 1.25, 2.0, 2.75, 3.5, 4.25, 5.0, 5.75, 6.5]
    output = float_range(0.5, 7, 0.75)
    assert list(output) == list(output)
    assert list(output) == expected


@pytest.mark.parametrize("start, stop, step, length",
                         [(0, 100, 1, 100),
                          (1, 100, 1, 99),
                          (1, 11, 2, 5),
                          (1, 11, -10, 0),
                          (0.5, 7, 0.75, 9),
                          (0, 1_000_000, 1, 1_000_000),
                          (11, 1.2, -2, 5),
                          (11, 1.2, 2, 0),
                          ])
def test_has_length(start: float, stop: float, step: float, length: int):
    assert len(float_range(start, stop, step)) == length


def test_len_fast():
    time = partial(timeit, globals=globals(), number=30)
    small = time("assert len(float_range(1)) == 1")
    big = time("assert len(float_range(1000)) == 1000")
    assert big < small*500, "Timing shouldn't grow with size"


@pytest.mark.bonus1
def test_can_be_indexed_and_reversed():
    # Indexing
    r = float_range(0.5, 7, 0.75)
    assert r[0] == 0.5
    assert r[1] == 1.25
    assert r[3] == 2.75
    assert r[6] == 5.0
    assert r[8] == 6.5
    assert r[-1] == 6.5
    assert r[-3] == 5.0
    assert r[-6] == 2.75
    assert r[-9] == 0.5
    with pytest.raises(IndexError):
        r[9]
    with pytest.raises(IndexError):
        r[-10]
    assert float_range(5, 0, -1)[1] == 4

    # Reversing
    r = reversed(float_range(0.5, 7, 0.75))
    assert list(r) == [6.5, 5.75, 5.0, 4.25, 3.5, 2.75, 2.0, 1.25, 0.5]
    big_num = 1000000
    assert next(reversed(float_range(big_num))) == big_num-1


@pytest.mark.bonus2
def test_equality_fast():
    time = partial(timeit, globals=globals(), number=100)
    small = time("assert float_range(0, 9.5, 1) == float_range(0, 10, 1)")
    big = time("assert float_range(0, 5000.5, 1) == float_range(0, 5000.2, 1)")
    assert big < small*50, "Timing shouldn't grow with size"


@pytest.mark.bonus2
def test_equality():
    assert float_range(0, 5, 0.5) == float_range(0, 5, 0.5)
    assert float_range(5, 5) == float_range(10, 10)
    assert float_range(5, 11, 5) == float_range(5, 12, 5)
    assert float_range(10) == float_range(0, 10)
    assert float_range(0, 2**10, 2**-10) != float_range(0, 2**10+1, 2**-10)
    assert float_range(1000000) == range(1000000)
    assert range(1000000) == float_range(1000000)
    assert not float_range(0, 5, 0.5) != float_range(0, 5, 0.5)

    class EqualToEverything:
        def __eq__(self, other):
            return True
    assert float_range(1000000) == EqualToEverything()
    assert float_range(0, 5, 3) == float_range(0, 4, 3)
    assert float_range(0, 0.3, 0.5) == float_range(0, 0.4, 1.5)
    assert float_range(0, 11, 0.5) != float_range(0, 11, 1.5)


@pytest.mark.bonus3
def test_can_be_sliced_and_supports_equality():
    r = float_range(0.5, 7, 0.75)
    t = float_range(0, 524288, 2**-4)
    assert list(r[0:2]) == [0.5, 1.25]
    assert list(r[:2]) == [0.5, 1.25]
    assert list(r[-3:]) == [5.0, 5.75, 6.5]
    assert list(r[-100:0]) == []
    assert list(r[-1:100]) == [6.5]
    assert list(r[::2]) == [0.5, 2.0, 3.5, 5.0, 6.5]
    assert list(r[len(r)::]) == []
    assert list(t[:3]) == [0, 0.0625, 0.125]
