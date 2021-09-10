import functools
from dataclasses import dataclass


@dataclass
class Call:
    args: any
    kwargs: any


NO_RETURN = object()


class record_calls:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.call_count = 0
        self.calls: list[Call] = []

    def __call__(self, *args, **kwargs):
        self.call_count += 1
        self.calls.append(Call(args, kwargs))
        return self.func(*args, **kwargs)


def main():
    # record_calls exercise from pythonmorsels
    # https://www.pythonmorsels.com/exercises/3ee85ad3481f428d99458b102cbda7c6/submit/1/

    @record_calls
    def greet(name="world"):
        """Greet someone by their name."""
        print(f"Hello {name}")

    # Basic Exercise
    greet("Trey")
    print(f"{greet.call_count=}")
    greet(name="Trey")
    print(f"{greet.call_count=}")

    # Bonus 1
    help(greet)

    # Bonus 2
    print(f"{greet.calls[0].args=}")
    print(f"{greet.calls[0].kwargs=}")

    print(f"{greet.calls[1].args=}")
    print(f"{greet.calls[1].kwargs=}")


if __name__ == "__main__":
    main()
