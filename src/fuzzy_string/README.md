## [FuzzyString](https://www.pythonmorsels.com/exercises/9655802abaef47c682555c198ee8b641)

### My notes
- 
- 

### Usage
Run the tests with:
- For all tests: `python -m pytest src/fuzzy_string`.
- For only the base exercise: `python -m pytest src/fuzzy_string -m "not (bonus1 or bonus2 or bonus3)"`
- For the base exercise and the first bonus: `python -m pytest src/fuzzy_string -m "not (bonus2 or bonus3)"`

Run the main file with `python src/fuzzy_string/fuzzy_string.py`.

### Description:
#### Base problem
I'd like you to write a FuzzyString class which acts like a string, but does comparisons in a case-insensitive way.

For example:
```python
>>> greeting = FuzzyString('Hey TREY!')
>>> greeting == 'hey Trey!'
True
>>> greeting == 'heyTrey'
False
>>> greeting
'Hey TREY!'
```

I'd like you to make sure equality and inequality match case-insensitively at first. I'd also like you to ensure that the string representations of your class match Python's string object's default string representations.

#### Bonus 1
For the first bonus, try to ensure the other comparison operators work as expected:
```python
>>> o_word = FuzzyString('Octothorpe')
>>> 'hashtag' < o_word
True
>>> 'hashtag' > o_word
False
```

I'd like you to make sure that comparison works for two FuzzyString objects also:
```python
>>> tokyo = FuzzyString("tokyo")
>>> toronto = FuzzyString("TORONTO")
>>> tokyo < toronto
True
>>> toronto < tokyo
False
```

#### Bonus 2
For the second bonus, ensure your FuzzyString class works with string concatenation and the in operator:

```python
>>> o_word = FuzzyString('Octothorpe')
>>> 'OCTO' in o_word
True
>>> new_string = o_word + ' (aka hashtag)'
>>> new_string == 'octothorpe (AKA hashtag)'
True
>>> city_name = FuzzyString("New Delhi")
>>> city_name_part = FuzzyString("w del")
>>> city_name_part in city_name
True
```

#### Bonus 3
Note: We don't recommend this bonus for Advanced-level users, unless you need an extra challenge.

For the third bonus, also make your string normalize unicode characters when checking for equality:

```python
>>> ss = FuzzyString('ss')
>>> '\u00df' == ss
True
>>> e = FuzzyString('\u00e9')
>>> '\u0065\u0301' == e
True
>>> '\u0301' in e
True
```

#### Hints
- [A class to help in creating custom strings](https://docs.python.org/3/library/collections.html#collections.UserString)
- [Bonus 3: normalizing unicode characters](https://docs.python.org/3/library/unicodedata.html#unicodedata.normalize)

