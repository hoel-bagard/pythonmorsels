def is_leap_year(year: int) -> bool:
    return year % 400 == 0 or year % 100 != 0 and year % 4 == 0


def assert_equal(res: object, expected_res: object):
    assert res == expected_res, f"Wrong result, got:\n\t{res}\nbut expected\n\t{expected_res}"


def main():
    # Base Exercise
    print("Base exercise")
    assert_equal(is_leap_year(1900), False)
    assert_equal(is_leap_year(2000), True)
    assert_equal(is_leap_year(2012), True)
    assert_equal(is_leap_year(2018), False)

    print("Passed all tests.")


if __name__ == "__main__":
    main()
