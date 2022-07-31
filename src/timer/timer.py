import statistics
import time
from collections.abc import Iterable
from contextlib import ContextDecorator
from types import TracebackType
from typing import Any, Callable, Optional, Type


class Timer(ContextDecorator):
    def __init__(self, func: Optional[Callable[[Any], Any]] = None):
        self.start = 0
        self.elapsed = 0
        self.runs: list[float] = []
        self.func = func

    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exception_type: Type[Exception], exception: Exception, traceback: TracebackType) -> bool:
        self.elapsed = time.perf_counter() - self.start
        self.runs.append(self.elapsed)
        return False

    def __call__(self, *args: Any, **kwargs: dict[str, Any]):
        self.start = time.perf_counter()
        assert self.func is not None  # For Pyright...
        res = self.func(*args, **kwargs)
        self.elapsed = time.perf_counter() - self.start
        self.runs.append(self.elapsed)
        return res

    @property
    def max(self):
        return max(self.runs)

    @property
    def min(self):
        return min(self.runs)

    @property
    def median(self):
        return statistics.median(self.runs)

    @property
    def mean(self):
        return statistics.mean(self.runs)


def assert_equal(res: object, expected_res: object) -> None:
    assert res == expected_res, f"Wrong result, got:\n\t{res}\nbut expected\n\t {expected_res}"


def main():
    # Base exercise:
    print("Testing the base exercise.")
    with Timer() as timer:
        time.sleep(0.5)
    assert 0.5 < timer.elapsed < 0.6, f"Time was not measured properly, expecter 0.5 but got {timer.elapsed=}"

    # Bonus 1
    print("Testing the first bonus.")
    timer = Timer()
    with timer:
        sum(range(2**24))
    t1 = timer.elapsed
    with timer:
        sum(range(2**25))
    t2 = timer.elapsed
    assert_equal(timer.runs, [t1, t2])

    # Bonus 2
    print("Testing the second bonus.")

    @Timer
    def sum_of_squares(numbers: Iterable[int]):
        return sum(n**2 for n in numbers)

    sum_of_squares(range(2**20))
    sum_of_squares(range(2**21))
    assert_equal(len(sum_of_squares.runs), 2)

    # Bonus 3
    print("Testing the third bonus.")
    sum_of_squares(range(2**19))
    sum_of_squares(range(2**22))
    assert_equal(sum_of_squares.min, min(sum_of_squares.runs))
    assert_equal(sum_of_squares.max, max(sum_of_squares.runs))
    assert_equal(sum_of_squares.mean, statistics.mean(sum_of_squares.runs))
    assert_equal(sum_of_squares.median, statistics.median(sum_of_squares.runs))

    print("Passed the tests!")


if __name__ == "__main__":
    main()
