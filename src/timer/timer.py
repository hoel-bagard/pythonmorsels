import time
from types import TracebackType
from typing import Type, TypeVar
# from dataclasses import dataclass

T = TypeVar('T')


# @dataclass
# class Call:
#     args: Any
#     kwargs: Any
#     exception: Optional[Exception] = None


class Timer:
    def __init__(self):
        self.start = 0
        self.elapsed = 0

    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exception_type: Type[Exception], exception: Exception, traceback: TracebackType) -> bool:
        self.elapsed = time.perf_counter() - self.start
        return True


def assert_equal(res, expected_res) -> None:
    assert res == expected_res, f"Wrong result, got:\n\t{res}\nbut expected\n\t {expected_res}"


def main():
    # Base exercise:
    print("Testing the base exercise")
    with Timer() as timer:
        time.sleep(0.5)
    assert 0.5 < timer.elapsed < 0.6, f"Time was not measured properly, expecter 0.5 but got {timer.elapsed=}"

    print("Passed the tests!")


if __name__ == "__main__":
    main()
