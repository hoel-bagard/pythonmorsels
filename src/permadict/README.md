## PermaDict

Run the python morsels tests with `python src/permadict/test_permadict.py`.\
Run the main file with `python src/permadict/permadict.py`.


### Bonus 1

I first wrote the following:
```python
    def force_set(self, key, value):
        self.data[key] = value
```

However, to make sure that it works nicely with inheritance (and to not relying on the `self.data`), it is better to use the parent's (`UserDict`) setitem method. Like so:

```python
    def force_set(self, key, value):
        super().__setitem__(key, value)
```

### Bonus 3

- The update method of a dictionary should return None (see doc [here](https://docs.python.org/3/library/stdtypes.html#dict.update)).
- Relying on the parent's update method is cleaner and shorter than reimplementing it all.
