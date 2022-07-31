import time
from types import TracebackType
from typing import Type


class Timer:
    def __init__(self):
        self.start = 0
        self.elapsed = 0
        self.runs: list[float] = []

    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exception_type: Type[Exception], exception: Exception, traceback: TracebackType) -> bool:
        self.elapsed = time.perf_counter() - self.start
        self.runs.append(self.elapsed)
        return True


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

    print("Passed the tests!")


if __name__ == "__main__":
    main()
