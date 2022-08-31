import os
# import re
# import shlex
import shutil
# import sys
# from contextlib import redirect_stderr, redirect_stdout
from contextlib import redirect_stdout
from importlib import reload
# from importlib.machinery import SourceFileLoader
# from importlib.util import module_from_spec, spec_from_loader
from io import StringIO
from typing import Callable, Optional
from unittest.mock import patch

import pytest

import src.countdown.countdown as countdown


class TestDuration:
    @pytest.mark.parametrize("duration_str, duration_value",
                             [("10s", 10),
                              ("60s", 60)])
    def test_seconds(self, duration_str: str, duration_value: int):
        assert countdown.duration(duration_str) == duration_value

    @pytest.mark.parametrize("duration_str, duration_value",
                             [("10m", 600),
                              ("35m", 2100)])
    def test_minutes(self, duration_str: str, duration_value: int):
        assert countdown.duration(duration_str) == duration_value

    @pytest.mark.parametrize("duration_str, duration_value",
                             [("3m30s", 210),
                              ("99m9s", 5949),
                              ("100m10s", 6010),
                              ("2m8s", 128)])
    def test_complex(self, duration_str: str, duration_value: int):
        assert countdown.duration(duration_str) == duration_value

    @pytest.mark.parametrize("invalid_duration_str", ["10x", "10y5z", "10m5x", "ms", "10"])
    def test_invalid_duration(self, invalid_duration_str: str):
        with pytest.raises(ValueError):
            countdown.duration(invalid_duration_str)


class TestGetNumberLines:
    """Tests for get_number_lines."""

    @pytest.mark.parametrize("seconds, representation",
                             [(10, ["██████ ██████       ██  ██████",
                                    "██  ██ ██  ██ ██   ███  ██  ██",
                                    "██  ██ ██  ██       ██  ██  ██",
                                    "██  ██ ██  ██ ██    ██  ██  ██",
                                    "██████ ██████       ██  ██████"])])
    def test_seconds_only(self, seconds: int, representation: list[str]):
        assert countdown.get_number_lines(seconds) == representation

    @pytest.mark.parametrize("seconds, representation",
                             [(60, ["██████    ██     ██████ ██████",
                                    "██  ██   ███  ██ ██  ██ ██  ██",
                                    "██  ██    ██     ██  ██ ██  ██",
                                    "██  ██    ██  ██ ██  ██ ██  ██",
                                    "██████    ██     ██████ ██████"]),

                              (2700, ["██  ██ ██████    ██████ ██████",
                                      "██  ██ ██     ██ ██  ██ ██  ██",
                                      "██████ ██████    ██  ██ ██  ██",
                                      "    ██     ██ ██ ██  ██ ██  ██",
                                      "    ██ ██████    ██████ ██████"]),

                              (540, ["██████ ██████    ██████ ██████",
                                     "██  ██ ██  ██ ██ ██  ██ ██  ██",
                                     "██  ██ ██████    ██  ██ ██  ██",
                                     "██  ██     ██ ██ ██  ██ ██  ██",
                                     "██████  █████    ██████ ██████"])])
    def test_minutes_only(self, seconds: int, representation: list[str]):
        assert countdown.get_number_lines(seconds) == representation

    @pytest.mark.parametrize("seconds, representation",
                             [(1024, ["   ██  ██████    ██████ ██  ██",
                                      "  ███      ██ ██ ██  ██ ██  ██",
                                      "   ██     ██     ██  ██ ██████",
                                      "   ██    ██   ██ ██  ██     ██",
                                      "   ██    ██      ██████     ██"]),

                              (486, ["██████  ████     ██████ ██████",
                                     "██  ██ ██  ██ ██ ██  ██ ██    ",
                                     "██  ██  ████     ██  ██ ██████",
                                     "██  ██ ██  ██ ██ ██  ██ ██  ██",
                                     "██████  ████     ██████ ██████"]),

                              (2118, ["██████ ██████       ██   ████ ",
                                      "    ██ ██     ██   ███  ██  ██",
                                      " █████ ██████       ██   ████ ",
                                      "    ██     ██ ██    ██  ██  ██",
                                      "██████ ██████       ██   ████ "])])
    def test_minutes_and_seconds(self, seconds: int, representation: list[str]):
        assert countdown.get_number_lines(seconds) == representation


@pytest.mark.bonus1
class TestPrintFullScreen:
    """Tests for print_full_screen."""

    def fake_size(self, columns: int, lines: int) -> Callable[[], tuple[int, int]]:
        def get_terminal_size(fd: Optional[str] = None):
            return os.terminal_size([columns, lines])
        return get_terminal_size

    def assert_lines_equal(self, actual_text: str, expected_text: str):
        actual_lines: list[str] = [
            line.rstrip()
            for line in actual_text.rstrip().splitlines()
        ]
        expected_lines: list[str] = [
            line.rstrip()
            for line in expected_text.rstrip().splitlines()
        ]

        assert "\n".join(actual_lines) == "\n".join(expected_lines)

    @pytest.mark.parametrize("nb_columns, nb_lines",
                             [(40, 10),
                              (80, 24)])
    def test_hello_world(self, nb_columns: int, nb_lines: int):
        hello_world = "hello_world"
        with patch("os.get_terminal_size", self.fake_size(nb_columns, nb_lines)):
            reload(shutil)
            reload(countdown)
            with redirect_stdout(StringIO()) as stdout:
                countdown.print_full_screen([hello_world])
        output = stdout.getvalue()

        text_width, text_height = len(hello_world), 1
        lines_before = (nb_lines-text_height) // 2
        indentation = (nb_columns-text_width) // 2

        assert output[:6] == "\x1b[H\x1b[J"  # Check that the screen was cleaned
        assert output[6:] == '\n' * lines_before + ' ' * indentation + hello_world + '\n'

    @pytest.mark.parametrize("nb_columns, nb_lines",
                             [(100, 30),
                              (80, 24)])
    def test_timer(self, nb_columns: int, nb_lines: int):
        lines = ["██████ ██████       ██   ████ ",
                 "    ██ ██     ██   ███  ██  ██",
                 " █████ ██████       ██   ████ ",
                 "    ██     ██ ██    ██  ██  ██",
                 "██████ ██████       ██   ████ "]
        with patch("os.get_terminal_size", self.fake_size(nb_columns, nb_lines)):
            reload(shutil)
            reload(countdown)
            with redirect_stdout(StringIO()) as stdout:
                countdown.print_full_screen(lines)
        output = stdout.getvalue()

        text_width, text_height = len(lines[0]), len(lines)
        lines_before = (nb_lines-text_height) // 2
        indentation = (nb_columns-text_width) // 2

        assert output[:6] == "\x1b[H\x1b[J"  # Check that the screen was cleaned
        assert output[6:] == '\n' * lines_before + '\n'.join(' ' * indentation + line for line in lines) + '\n'


# @pytest.mark.bonus2
# class CountdownModuleTests:
#     """Tests for countdown.py."""

#     def assertOutput(self, actual_text, expected_text, allow_wiggle=True):
#         expected_text = expected_text.rstrip()
#         actual_text = re.sub(r"^[\s\S]*?\033\[H\033\[J", r"", actual_text)
#         actual_text = re.sub(r"\033\[([HJ]|\?25[lh])", r"", actual_text)
#         actual_text = "\n".join([
#             line.rstrip(" ")
#             for line in actual_text.splitlines()
#         ]).rstrip()
#         try:
#             self.assertEqual(actual_text, expected_text)
#         except AssertionError as e:
#             if not allow_wiggle:
#                 raise
#             try:
#                 new1 = "\n".join(line[1:] for line in actual_text.split("\n"))
#                 self.assertOutput(new1, expected_text, allow_wiggle=False)
#             except AssertionError:
#                 try:
#                     new2 = indent(actual_text, " ")
#                     self.assertOutput(new2, expected_text, allow_wiggle=False)
#                 except AssertionError:
#                     raise e from None

#     def test_3_seconds(self):
#         with patch("os.get_terminal_size", self.fake_size(60, 20)):
#             with patch("time.sleep", FakeSleep()) as sleep_patch:
#                 reload(shutil)
#                 reload(countdown)
#                 self.assertOutput(run_program("countdown.py 3s"), """
#                 """)
#         self.assertEqual(sleep_patch.slept, 4, "3 seconds = 4 sleeps")

#     def test_1_minute(self):
#         with patch("os.get_terminal_size", self.fake_size(32, 8)):
#             with patch("time.sleep", FakeSleep()) as sleep_patch:
#                 reload(shutil)
#                 reload(countdown)
#                 # Raise exception after 11 seconds
#                 sleep_patch.raise_at(11, SystemExit(0))
#                 self.assertOutput(run_program("countdown.py 1m"), """
# ██████    ██     ██████ ██████
# ██  ██   ███  ██ ██  ██ ██  ██
# ██  ██    ██     ██  ██ ██  ██
# ██  ██    ██  ██ ██  ██ ██  ██
# ██████    ██     ██████ ██████

# ██████ ██████    ██████ ██████
# ██  ██ ██  ██ ██ ██     ██  ██
# ██  ██ ██  ██    ██████ ██████
# ██  ██ ██  ██ ██     ██     ██
# ██████ ██████    ██████  █████

# ██████ ██████    ██████  ████
# ██  ██ ██  ██ ██ ██     ██  ██
# ██  ██ ██  ██    ██████  ████
# ██  ██ ██  ██ ██     ██ ██  ██
# ██████ ██████    ██████  ████

# ██████ ██████    ██████ ██████
# ██  ██ ██  ██ ██ ██         ██
# ██  ██ ██  ██    ██████    ██
# ██  ██ ██  ██ ██     ██   ██
# ██████ ██████    ██████   ██

# ██████ ██████    ██████ ██████
# ██  ██ ██  ██ ██ ██     ██
# ██  ██ ██  ██    ██████ ██████
# ██  ██ ██  ██ ██     ██ ██  ██
# ██████ ██████    ██████ ██████

# ██████ ██████    ██████ ██████
# ██  ██ ██  ██ ██ ██     ██
# ██  ██ ██  ██    ██████ ██████
# ██  ██ ██  ██ ██     ██     ██
# ██████ ██████    ██████ ██████

# ██████ ██████    ██████ ██  ██
# ██  ██ ██  ██ ██ ██     ██  ██
# ██  ██ ██  ██    ██████ ██████
# ██  ██ ██  ██ ██     ██     ██
# ██████ ██████    ██████     ██

# ██████ ██████    ██████ ██████
# ██  ██ ██  ██ ██ ██         ██
# ██  ██ ██  ██    ██████  █████
# ██  ██ ██  ██ ██     ██     ██
# ██████ ██████    ██████ ██████

# ██████ ██████    ██████ ██████
# ██  ██ ██  ██ ██ ██         ██
# ██  ██ ██  ██    ██████ ██████
# ██  ██ ██  ██ ██     ██ ██
# ██████ ██████    ██████ ██████

# ██████ ██████    ██████    ██
# ██  ██ ██  ██ ██ ██       ███
# ██  ██ ██  ██    ██████    ██
# ██  ██ ██  ██ ██     ██    ██
# ██████ ██████    ██████    ██

# ██████ ██████    ██████ ██████
# ██  ██ ██  ██ ██ ██     ██  ██
# ██  ██ ██  ██    ██████ ██  ██
# ██  ██ ██  ██ ██     ██ ██  ██
# ██████ ██████    ██████ ██████
#                 """)

#     def test_10_minutes_has_over_600_clear_screens(self):
#         with patch("os.get_terminal_size", self.fake_size(32, 10)):
#             with patch("time.sleep", FakeSleep()) as sleep_patch:
#                 reload(shutil)
#                 reload(countdown)
#                 output = run_program("countdown.py 10m")
#                 self.assertEqual(
#                     sleep_patch.slept,
#                     601,
#                     "10 minutes = 601 sleeps",
#                 )
#                 self.assertIn(
#                     output.count("\033[H\033[J"),
#                     [601, 602, 603],
#                     # 10 minutes means 601 seconds and a clear screen for each
#                 )


# # To test bonus 3, comment out the next line
# @unittest.expectedFailure
# class MoreCountdownModuleTests(unittest.TestCase):

#     """Continued tests for countdown.py."""

#     maxDiff = None

#     def fake_size(self, columns, lines):
#         def get_terminal_size(fd=None):
#             return os.terminal_size([columns, lines])
#         return get_terminal_size

#     def test_cursor_hides_at_beginning(self):
#         with patch("os.get_terminal_size", self.fake_size(32, 10)):
#             with patch("time.sleep", FakeSleep()):
#                 reload(shutil)
#                 reload(countdown)
#                 output = run_program("countdown.py 5m").encode()
#                 self.assertEqual(output[:6], b"\033[?25l", "Hide cursor first")

#     def test_show_cursor_at_end(self):
#         with patch("os.get_terminal_size", self.fake_size(32, 10)):
#             with patch("time.sleep", FakeSleep()):
#                 reload(shutil)
#                 reload(countdown)
#                 output = run_program("countdown.py 5m").encode()
#                 self.assertIn(b"\033[?25h", output[-12:], "Show cursor last")

#     def test_show_cursor_even_on_early_exit(self):
#         with patch("os.get_terminal_size", self.fake_size(32, 10)):
#             with patch("time.sleep", FakeSleep()) as sleep_patch:
#                 reload(shutil)
#                 reload(countdown)
#                 # Hit Ctrl+C after 4 seconds
#                 sleep_patch.raise_at(4, KeyboardInterrupt)
#                 output = run_program("countdown.py 15m").encode()
#                 self.assertIn(
#                     len(output.splitlines()),
#                     range(24, 43),
#                     "Stop after ~4 seconds-worth of lines printed",
#                 )
#                 self.assertIn(b"\033[?25h", output[-6:], "Show cursor last")


# def undent(text):
#     return dedent(text.lstrip("\n")).strip("\n")


# class FakeSleep:

#     """Fake time.sleep."""

#     def __init__(self):
#         self.slept = 0
#         self.raises = {}

#     def __call__(self, seconds):
#         self.slept += seconds
#         if self.slept in self.raises:
#             raise self.raises[self.slept]

#     def raise_at(self, seconds, exception):
#         self.raises[seconds] = exception


# def run_program(arguments="", raises=DummyException):
#     """
#     Run program at given path with given arguments.

#     If raises is specified, ensure the given exception is raised.
#     """
#     arguments = arguments.replace('\\', '\\\\')
#     path, *args = shlex.split(arguments)
#     old_args = sys.argv
#     assert all(isinstance(a, str) for a in args)
#     try:
#         sys.argv = [path] + args
#         with redirect_stdout(StringIO()) as output:
#             with redirect_stderr(output):
#                 try:
#                     if '__main__' in sys.modules:
#                         del sys.modules['__main__']
#                     loader = SourceFileLoader('__main__', path)
#                     spec = spec_from_loader(loader.name, loader)
#                     module = module_from_spec(spec)
#                     sys.modules['__main__'] = module
#                     loader.exec_module(module)
#                 except raises:
#                     return output.getvalue()
#                 except KeyboardInterrupt:
#                     return output.getvalue()
#                 except SystemExit as e:
#                     if e.args != (0,):
#                         raise SystemExit(output.getvalue()) from e
#                 finally:
#                     sys.modules['__main__'].__dict__.clear()
#                     sys.modules.pop('__main__', None)  # Closes any open files
#                 if raises is not DummyException:
#                     raise AssertionError("{} not raised".format(raises))
#                 return output.getvalue()
#     finally:
#         sys.argv = old_args
