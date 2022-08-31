import argparse
import re
import shutil
import time


digit_to_glyph = {
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
    m = re.search(r"^(\d+)([ms])(\d*)s?$", duration_str)
    if m is None:
        raise ValueError("Invalid duration: {duration_str}")

    minutes = int(m.group(1)) if m.group(2) == 'm' else 0
    seconds = int(m.group(1)) if m.group(2) == 's' else (int(m.group(3)) if len(m.group(3)) > 0 else 0)

    return 60 * minutes + seconds


def get_number_lines(seconds: int) -> list[str]:
    minutes = f"{seconds//60:02d}"
    seconds = f"{seconds%60:02d}"

    result = [" ".join(line) for line in zip(*[
        digit_to_glyph[minutes[0]].split('\n'),
        digit_to_glyph[minutes[1]].split('\n'),
        digit_to_glyph[':'].split('\n'),
        digit_to_glyph[seconds[0]].split('\n'),
        digit_to_glyph[seconds[1]].split('\n'),
    ])]
    return result


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


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("countdown", type=str, help="Countdown duration, format <min>m<seconds>s")
    args = parser.parse_args()

    countdown: int = args.countdown
    seconds = duration(countdown)

    for remaining_time in range(seconds, -1, -1):
        print_full_screen(get_number_lines(remaining_time))
        time.sleep(1)


if __name__ == "__main__":
    main()


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
    # Bonus 1
    print("Not testing the first bonus.")
    # print_full_screen(get_number_lines(754))

    # Bonus 2
    print("Testing the second bonus.")

    # Bonus 3
    print("Testing the third bonus.")

    print("Passed the tests!")
