import re


def duration(duration_str: str) -> int:
    m = re.search(r"^(\d+)([ms])(\d*)s?$", duration_str)
    if m is None:
        raise ValueError("Invalid duration: {duration_str}")

    minutes = int(m.group(1)) if m.group(2) == 'm' else 0
    seconds = int(m.group(1)) if m.group(2) == 's' else (int(m.group(3)) if len(m.group(3)) > 0 else 0)

    return 60 * minutes + seconds


def assert_equal(res: object, expected_res: object) -> None:
    assert res == expected_res, f"Wrong result, got:\n\t{res}\nbut expected\n\t {expected_res}"


def main():
    # Base exercise:
    print("Testing the base exercise.")
    assert_equal(duration("5m"), 300)
    assert_equal(duration("2m30s"), 150)
    assert_equal(duration("5s"), 5)
    assert_equal(duration("10m"), 600)

    try:
        duration("100xy")
        print("Should have raised a ValueError but did not.")
    except ValueError:
        pass

    # Bonus 1
    print("Testing the first bonus.")

    # Bonus 2
    print("Testing the second bonus.")

    # Bonus 3
    print("Testing the third bonus.")

    print("Passed the tests!")


if __name__ == "__main__":
    main()
