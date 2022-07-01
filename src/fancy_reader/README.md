# [Fancy Reader](https://www.pythonmorsels.com/exercises/7271e894d9f24b8385ad6cda60c519e4)

### My notes
- To print a representation that looks like Python code (`Row(a='b')` vs `Row(a=b)`), use the `repr` function on the variable (the one containing `b` here).
- Use `yield from` when possible.
- Could have used `collections.namedtuple` to make the Row class.


### Usage
Run the python morsels tests with `python src/fancy_reader/test_fancy_reader.py`.\
Run the main file with `python src/fancy_reader/fancy_reader.py`.

### Description:
#### Base problem
I'd like you to make a custom CSV reader that acts slightly different from both csv.reader and csv.DictReader.

I'd like you to make a FancyReader callable that will accept an iterable of strings (which is what csv.reader accepts) and a fieldnames attribute representing the headers. This FancyReader callable will return an iterator that yields Row objects which represent each row.

```python
>>> lines = ['my,fake,file', 'has,two,rows']
>>> reader = FancyReader(lines, fieldnames=['w1', 'w2', 'w3'])
>>> for row in reader:
...     print(row.w1, row.w2, row.w3)
my fake file
has two rows
```

Your FancyReader should accept all the same arguments as csv.reader.
You don't need to worry about headers that are invalid variable names in Python: just assume all headers are valid Python variable names.


#### Bonus 1
For the first bonus, I'd like you to make sure your Row objects are iterable and have a nice string representation.

#### Bonus 2
For the second bonus, I'd like you to make the fieldnames attribute optional. If no fieldnames attribute is specified, the first row should be automatically be read as a header row (and used in place of fieldnames).

#### Bonus 3
For the third bonus, I'd like the return value of FancyReader to have a line_num attribute, the same way csv.reader does:

```python
>>> lines = 'red,1\nblue,2\ngreen,3'.splitlines()
>>> reader = FancyReader(lines, fieldnames=['color', 'number'])
>>> next(reader)
Row(color='red', number='1')
>>> reader.line_num
1
>>> next(reader)
Row(color='blue', number='2')
>>> reader.line_num
2
```

If you get stumped while working on the bonuses, you may want to take a look at the source code for DictReader. You could almost nearly copy what DictReader does if you wanted to. But if you want more of a challenge I recommend not looking at the DictReader source code (until you get stuck).
