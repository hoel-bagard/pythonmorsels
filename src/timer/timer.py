import time
from contextlib import ContextDecorator
from types import TracebackType
from typing import Callable, Type


class Timer(ContextDecorator):
    def __init__(self, func: Callable = None):
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

    def __call__(self, *args, **kwargs):
        self.start = time.perf_counter()
        res = self.func(*args, **kwargs)
        self.elapsed = time.perf_counter() - self.start
        self.runs.append(self.elapsed)
        return res


def assert_equal(res, expected_res) -> None:
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
    def sum_of_squares(numbers):
        return sum(n**2 for n in numbers)

    sum_of_squares(range(2**20))
    sum_of_squares(range(2**21))
    assert_equal(len(sum_of_squares.runs), 2)
    print("Passed the tests!")


if __name__ == "__main__":
    main()
