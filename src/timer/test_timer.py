"""Tests for the tail exercise using Pytest."""
from time import perf_counter

import pytest


from src.timer.timer import Timer

# _baseline = None

# @staticmethod
# def get_baseline(count=100):
#     times = 0
#     for _ in range(count):
#         with Timer() as timer:
#             sleep(0)
#         times += timer.elapsed
#     return times / count

# def assertTimeEqual(self, actual, expected):
#     if self._baseline is None:
#         self._baseline = self.get_baseline()
#     self.assertAlmostEqual(actual, self._baseline+expected, delta=0.15)


def test_short_time():
    with Timer() as timer:
        sleep(0.1)
    assert 0.009 < timer.elapsed < 0.8


def test_very_short_time():
    with Timer() as timer:
        pass
    assert pytest.approx(timer.elapsed, abs=1e-3) == 0


def test_two_timers():
    with Timer() as timer1:
        sleep(0.005)
        with Timer() as timer2:
            sleep(0.05)
        sleep(0.05)
    assert timer2.elapsed < timer1.elapsed


def test_reusing_same_timer():
    timer = Timer()
    with timer:
        sleep(0.01)
    elapsed1 = timer.elapsed
    with timer:
        sleep(0.2)
    elapsed2 = timer.elapsed
    assert elapsed1 < elapsed2


@pytest.mark.bonus1
class TestBonus1:
    def test_runs_recorded(self):
        timer1 = Timer()
        timer2 = Timer()
        with timer1:
            with timer2:
                sleep(0.001)
            with timer2:
                sleep(0.002)
        with timer1:
            sleep(0.005)
        with timer1:
            pass
        self.assertEqual(len(timer1.runs), 3)
        self.assertEqual(len(timer2.runs), 2)
        self.assertGreater(timer1.runs[0], sum(timer2.runs))
        self.assertTimeEqual(timer1.runs[2], 0.000)


@pytest.mark.bonus2
class TestBonus2:
    def test_works_as_decorator(self):
        @Timer
        def wait(*args, **kwargs):
            sleep(0.01)
            return args, kwargs
        args, kwargs = wait(1, a=3)
        self.assertEqual(args, (1,))
        self.assertEqual(kwargs, {'a': 3})
        self.assertTimeEqual(wait.elapsed, 0.01)
        self.assertEqual(wait.runs, [wait.elapsed])


@pytest.mark.bonus3
class TestBonus3:
    def test_stat_recorded(self):
        wait = Timer(sleep)
        wait(0.02)
        wait(0.03)
        wait(0.05)
        wait(0.08)
        wait(0.03)
        times = sorted(wait.runs)
        self.assertTimeEqual(wait.mean, sum(times)/len(times))
        self.assertTimeEqual(wait.median, times[2])
        self.assertTimeEqual(wait.min, times[0])
        self.assertTimeEqual(wait.max, times[-1])


def sleep(duration):
    now = perf_counter()
    end = now + duration
    while now < end:
        now = perf_counter()
