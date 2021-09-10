import functools
import traceback
from dataclasses import dataclass
from typing import Optional


NO_RETURN = object()


@dataclass
class Call:
    args: any
    kwargs: any
    return_value: any = NO_RETURN
    exception: Optional[Exception] = None


class record_calls:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.call_count = 0
        self.calls: list[Call] = []

    def __call__(self, *args, **kwargs):
        self.call_count += 1
        try:
            return_value = self.func(*args, **kwargs)
            self.calls.append(Call(args, kwargs, return_value, None))
            return return_value
        except Exception as e:
            self.calls.append(Call(args, kwargs, NO_RETURN, e))
            raise


def main():
    # record_calls exercise from pythonmorsels
    # https://www.pythonmorsels.com/exercises/3ee85ad3481f428d99458b102cbda7c6/submit/1/

    @record_calls
    def greet(name="world"):
        """Greet someone by their name."""
        print(f"Hello {name}")

    # Basic Exercise
    print("\nBasic exercise")
    greet("Trey")
    print(f"{greet.call_count=}")
    greet(name="Trey")
    print(f"{greet.call_count=}")

    # Bonus 1
    print("\nBonus 1")
    help(greet)
    print(str(greet))

    # Bonus 2
    print("\nBonus 2")
    print(f"{greet.calls[0].args=}")
    print(f"{greet.calls[0].kwargs=}")

    print(f"{greet.calls[1].args=}")
    print(f"{greet.calls[1].kwargs=}")

    # Bonus 3
    print("\nBonus 3")

    @record_calls
    def cube(n):
        return n**3

    print(f"{cube(3)=}")
    print(cube.calls)
    try:
        cube(None)
    except Exception as e:
        print(traceback.format_exc())
    print(cube.calls[-1].exception)
    print(cube.calls[-1].return_value == NO_RETURN)


if __name__ == "__main__":
    main()
