import argparse
import re
import shutil
import time


digit_to_glyph: dict[str, str] = {
    "0": "██████\n██  ██\n██  ██\n██  ██\n██████",
    "1": "   ██ \n  ███ \n   ██ \n   ██ \n   ██ ",
    "2": "██████\n    ██\n██████\n██    \n██████",
    "3": "██████\n    ██\n █████\n    ██\n██████",
    "4": "██  ██\n██  ██\n██████\n    ██\n    ██",
    "5": "██████\n██    \n██████\n    ██\n██████",
    "6": "██████\n██    \n██████\n██  ██\n██████",
    "7": "██████\n    ██\n   ██ \n  ██  \n  ██  ",
    "8": " ████ \n██  ██\n ████ \n██  ██\n ████ ",
    "9": "██████\n██  ██\n██████\n    ██\n █████",
    ":": "  \n██\n  \n██\n  ",
}

CLEAR = "\033[H\033[J"  # Move cursor to top corner and clear screen


def duration(duration_str: str) -> int:
    match = re.search(r"^(?:(\d+)m)?(?:(\d+)s)?$", duration_str)

    if match is None:
        raise ValueError("Invalid duration: {duration_str}")

    minutes, seconds = match.groups(default=0)

    return 60 * int(minutes) + int(seconds)


def get_number_lines(seconds: int) -> list[str]:
    timestamp = f"{seconds//60:02d}:{seconds%60:02d}"
    return [" ".join(line_parts) for line_parts in zip(*[digit_to_glyph[char].splitlines() for char in timestamp])]


def print_full_screen(lines: list[str]) -> None:
    term_width, term_height = shutil.get_terminal_size()
    text_width, text_height = len(lines[0]), len(lines)
    lines_before = (term_height-text_height) // 2
    indentation = (term_width-text_width) // 2

    print(CLEAR, end="")
    print('\n' * lines_before, end="")
    for line in lines:
        print(' ' * indentation + line)


def assert_equal(res: object, expected_res: object) -> None:
    assert res == expected_res, f"Wrong result, got:\n\t{res}\nbut expected\n\t {expected_res}"


def main_morsels(countdown: str) -> None:
    seconds = duration(countdown)

    print("\x1b[?25l", end='')  # Hide cursor
    try:
        for remaining_time in range(seconds, -1, -1):
            print_full_screen(get_number_lines(remaining_time))
            time.sleep(1)
    finally:
        print("\x1b[?25h", end='')  # Show cursor


def main_test():
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

    assert_equal(get_number_lines(15),
                 ["██████ ██████       ██  ██████",
                  "██  ██ ██  ██ ██   ███  ██    ",
                  "██  ██ ██  ██       ██  ██████",
                  "██  ██ ██  ██ ██    ██      ██",
                  "██████ ██████       ██  ██████"])
    assert_equal(get_number_lines(754),
                 ["   ██  ██████    ██████ ██  ██",
                  "  ███      ██ ██     ██ ██  ██",
                  "   ██  ██████     █████ ██████",
                  "   ██  ██     ██     ██     ██",
                  "   ██  ██████    ██████     ██"])

    print("Not testing the bonuses.")
    print("Passed the tests!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("countdown", type=str, help="Countdown duration, format <min>m<seconds>s")
    parser.add_argument("--local_tests", "-t", action="store_true",
                        help="Use this flag to run some tests on the base exercise.")
    args = parser.parse_args()

    countdown: str = args.countdown
    local_testing: bool = args.local_tests

    if local_testing:
        main_test()
    else:
        main_morsels(countdown)
