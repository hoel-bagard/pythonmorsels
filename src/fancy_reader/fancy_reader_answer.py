import csv
from collections.abc import Iterable
from functools import cached_property
from typing import Any, NamedTuple


class FancyReader:
    def __init__(self, iterable: Iterable[str], **kwargs: dict[str, Any]):
        self.reader = csv.DictReader(iterable, **kwargs)

    def __iter__(self):
        return self

    def __next__(self):
        return self.make_row(**next(self.reader))

    @property
    def line_num(self):
        return self.reader.line_num

    @property
    def fieldnames(self):
        return self.reader.fieldnames

    @cached_property
    def make_row(self):
        return NamedTuple("Row", self.fieldnames)
