from collections.abc import Iterator


def parse_ranges(ranges: str) -> Iterator[int]:
    for interval in ranges.split(","):
        start, stop = interval.split("-")
        # result.extend(range(int(start), int(stop)+1))
        for number in range(int(start), int(stop)+1):
            yield number


def assert_equal(res: object, expected_res: object):
    assert res == expected_res, f"Wrong result, got:\n\t{res}\nbut expected\n\t{expected_res}"


def main():
    # Base Exercise
    print("Base exercise")
    assert_equal(list(parse_ranges("1-2,4-4,8-13")), [1, 2, 4, 8, 9, 10, 11, 12, 13])
    assert_equal(list(parse_ranges("0-0, 4-8, 20-20, 43-45")), [0, 4, 5, 6, 7, 8, 20, 43, 44, 45])

    # Bonus 1
    print("Bonus 1")
    numbers = parse_ranges("100-10000")
    assert_equal(next(numbers), 100)
    assert_equal(next(numbers), 101)

    print("Passed all tests.")


if __name__ == "__main__":
    main()
