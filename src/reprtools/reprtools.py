def format_arguments(*args: object, **kwargs: object) -> str:
    res_str = ", ".join(repr(arg) for arg in args)
    if args and kwargs:
        res_str += ", "
    if kwargs:
        res_str += ", ".join(f"{key}={repr(value)}" for key, value in kwargs.items())
    return res_str


def assert_equal(res: str, expected_res: str):
    assert res == expected_res, f"Wrong result, got:\n\t{res}\nbut expected\n\t {expected_res}"


def main():
    # Base Exercise
    print("\nBasic exercise")
    assert_equal(format_arguments(1, 2, 3), "1, 2, 3")
    assert_equal(format_arguments("expenses.csv", mode="wt", encoding="utf-8"),
                 "'expenses.csv', mode='wt', encoding='utf-8'")

    # Bonus 1
    print("\nBonus 1")

    # Bonus 2
    print("\nBonus 2")

    # Bonus 3
    print("\nBonus 3")


if __name__ == "__main__":
    main()
