# [Countdown](https://www.pythonmorsels.com/exercises/fc3be8467c634f978eae0c315f5677d1)

### My notes

### Usage
Run the tests with:
- For all tests: `python -m pytest src/countdown`.
- For only the base exercise: `python -m pytest src/countdown -m "not (bonus1 or bonus2 or bonus3)"`
- For the base exercise and the first bonus: `python -m pytest src/countdown -m "not (bonus2 or bonus3)"`

Run the main file with `python src/countdown/countdown.py`.

### Description:
#### Base problem

I'd like you to make a command-line countdown timer.

This countdown timer will print minutes and seconds in large numbers, like this:

   ██  ██████    ██████ ██  ██
  ███      ██ ██ ██  ██ ██  ██
   ██     ██     ██  ██ ██████
   ██    ██   ██ ██  ██     ██
   ██    ██      ██████     ██

At first I'd like you to make two functions:
- `duration which` accepts a string representing minutes and seconds and returns the total number of seconds represented
- `get_number_lines` which accepts an integer representing seconds and returns a list of lines representing the time in large glyphs (like above)

You can use this dictionary to help make your big number string:
```python
CHARS = {
    '0': '██████\n██  ██\n██  ██\n██  ██\n██████',
    '1': '   ██ \n  ███ \n   ██ \n   ██ \n   ██ ',
    '2': '██████\n    ██\n██████\n██    \n██████',
    '3': '██████\n    ██\n █████\n    ██\n██████',
    '4': '██  ██\n██  ██\n██████\n    ██\n    ██',
    '5': '██████\n██    \n██████\n    ██\n██████',
    '6': '██████\n██    \n██████\n██  ██\n██████',
    '7': '██████\n    ██\n   ██ \n  ██  \n  ██  ',
    '8': ' ████ \n██  ██\n ████ \n██  ██\n ████ ',
    '9': '██████\n██  ██\n██████\n    ██\n █████',
    ':': '  \n██\n  \n██\n  ',
}
```
The values in that dictionary represent 5-line glyphs for 0 through 9 and :.

```python
>>> CHARS['0']
'██████\n██  ██\n██  ██\n██  ██\n██████'
>>> print(CHARS['0'])
██████
██  ██
██  ██
██  ██
██████
```
The get_number_lines function should accept seconds (as an integer) and return a list of lines representing those large number glyphs in the format MM:SS:

```python
>>> get_number_lines(15)
['██████ ██████       ██  ██████', '██  ██ ██  ██ ██   ███  ██    ', '██  ██ ██  ██       ██  ██████', '██  ██ ██  ██ ██    ██      ██', '██████ ██████       ██  ██████']
>>> print(*get_number_lines(15), sep='\n')
██████ ██████       ██  ██████
██  ██ ██  ██ ██   ███  ██
██  ██ ██  ██       ██  ██████
██  ██ ██  ██ ██    ██      ██
██████ ██████       ██  ██████
>>> get_number_lines(754)
['   ██  ██████    ██████ ██  ██', '  ███      ██ ██     ██ ██  ██', '   ██  ██████     █████ ██████', '   ██  ██     ██     ██     ██', '   ██  ██████    ██████     ██']
>>> print(*get_number_lines(754), sep='\n')
   ██  ██████    ██████ ██  ██
  ███      ██ ██     ██ ██  ██
   ██  ██████     █████ ██████
   ██  ██     ██     ██     ██
   ██  ██████    ██████     ██
```
Note that the list of lines returned by get_number_lines doesn't include any newline characters.

The duration function should accept a string in the format Dm, Ds, or DmDs where D represents one or more digits. The number of seconds represented by the given minutes or seconds should be returned:

```python
>>> duration("5m")  # 5 minutes
300
>>> duration("2m30s")  # 2 minutes, 30 seconds
150
>>> duration("5s")  # 5 seconds
5
>>> duration("10m")  # 10 minutes
600
```
If an invalid duration is given, an exception should be raised (any exception type and message is acceptable):

```python
>>> duration("100xy")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: Invalid duration: 100xy
```


#### Bonus 1
For the first bonus, make a print_full_screen function which accepts a list of lines (strings) and prints those lines in the center of the screen. The list-of-strings returned from get_number_lines should be accepted by this function.

This function should start by printing the ANSI escape sequences Esc-[H and Esc-[J to move the cursor to the home position and clear the screen. You can use this string to represent those two escape sequences:

```python
CLEAR = "\033[H\033[J"  # Move cursor to top corner and clear screen
```
Then terminal size should be detected and an appropriate number of line breaks should be printed to position the countdown timer in the center of the screen.

This text is 30 characters long and 5 lines tall:

██████ ██████       ██  ██████
██  ██ ██  ██ ██   ███  ██
██  ██ ██  ██       ██  ██████
██  ██ ██  ██ ██    ██      ██
██████ ██████       ██  ██████
For a terminal window that has 53 lines and 175 columns, 24 blank lines should be printed out before the numbers and the number lines should be indented by 72 spaces.

```python
>>> term_height, term_width = 53, 175
>>> text_height, text_width = 5, 30
>>> lines_before = (term_height-text_height)//2
>>> indentation = (term_width-text_width)//2
>>> lines_before
24
>>> indentation
72
```

#### Bonus 2
For the second bonus, make your countdown.py file a fully functional Python script.

Running countdown.py should print each time between the given one and 00:00 (inclusive), sleeping 1 second between each time.

Here's an example of countdown.py called with 3 seconds in a 60 column by 16 line terminal:

$ python3 countdown.py 3s





               ██████ ██████    ██████ ██████
               ██  ██ ██  ██ ██ ██  ██     ██
               ██  ██ ██  ██    ██  ██  █████
               ██  ██ ██  ██ ██ ██  ██     ██
               ██████ ██████    ██████ ██████





               ██████ ██████    ██████ ██████
               ██  ██ ██  ██ ██ ██  ██     ██
               ██  ██ ██  ██    ██  ██ ██████
               ██  ██ ██  ██ ██ ██  ██ ██
               ██████ ██████    ██████ ██████





               ██████ ██████    ██████    ██
               ██  ██ ██  ██ ██ ██  ██   ███
               ██  ██ ██  ██    ██  ██    ██
               ██  ██ ██  ██ ██ ██  ██    ██
               ██████ ██████    ██████    ██





               ██████ ██████    ██████ ██████
               ██  ██ ██  ██ ██ ██  ██ ██  ██
               ██  ██ ██  ██    ██  ██ ██  ██
               ██  ██ ██  ██ ██ ██  ██ ██  ██
               ██████ ██████    ██████ ██████
Note that the time should be centered in the terminal (as in bonus 1) and the screen should be cleared before each new time (by printing the ANSI escape sequences from bonus 1).

If you're manually testing in the Windows command prompt and not seeing the screen clear, check the hints.

#### Bonus 3
For the third bonus, your countdown.py script should hide the cursor in your terminal when the program starts and reveal it at the end. Make sure the cursor is revealed again even if the program exits prematurely.

### Hints
