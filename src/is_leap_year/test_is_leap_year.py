"""Tests for the is_leap_year exercise using pytest."""
import pytest

from src.is_leap_year.is_leap_year import is_leap_year


@pytest.mark.parametrize("year", [1996, 2012])
def test_leap_years(year: int):
    assert is_leap_year(year)


@pytest.mark.parametrize("year", [1994, 1995, 2010, 2011])
def test_non_leap_years(year: int):
    assert not is_leap_year(year)


@pytest.mark.parametrize("year", [1900, 1700, 1500])
def test_centennial_nonleap_year(year: int):
    assert not is_leap_year(year)


@pytest.mark.parametrize("year", [1600, 2000])
def test_centennial_leap_year(year: int):
    assert is_leap_year(year)
