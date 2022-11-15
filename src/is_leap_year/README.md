# [is_leap_year](https://www.pythonmorsels.com/exercises/f04ba162d0664a13895f96c9587de8ae/)

### My notes

### Usage
Run the tests with: `python -m pytest src/is_leap_year`.
Run the main file with `python src/is_leap_year/is_leap_year.py`.

### Description:
#### Base problem
Create a function `is_leap_year` that accepts a year and returns `True` if (and only if) the given year is a leap year.

- Leap years are years that are divisible by 4
- Exception: centennials (years divisible by 100) are not leap years
- Exception to exception: years divisible by 400 are leap years
```python
>>> is_leap_year(1900)
False
>>> is_leap_year(2000)
True
>>> is_leap_year(2012)
True
>>> is_leap_year(2018)
False
```
