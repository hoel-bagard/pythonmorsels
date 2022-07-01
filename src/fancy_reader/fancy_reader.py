import csv
from collections.abc import Iterable
from typing import Optional


class Row:
    def __iter__(self):
        current = 0
        while current < len(self.__dict__.items()):
            yield list(self.__dict__.values())[current]
            current += 1

    def __repr__(self):
        content = ", ".join([f"{value_name}='{name}'" for value_name, name in self.__dict__.items()])
        return f"{type(self).__name__}({content})"


class FancyReader:
    def __init__(self, csv_file: Iterable[str], fieldnames: Optional[list[str]] = None, **fmt_params):
        self.csv_data = csv.reader(csv_file, **fmt_params)
        self.field_names = fieldnames
        self.line_num = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.field_names is None:
            self.field_names = next(self.csv_data)
            self.line_num += 1
        values = next(self.csv_data)
        row = Row()
        for attribute, value in zip(self.field_names, values, strict=True):
            setattr(row, attribute, value)
        self.line_num += 1
        return row

    def __repr__(self):
        return f"{type(self).__name__}(file={self.csv_data})"


def test_equal(res, expected_res):
    assert res == expected_res, f"Wrong result, got:\n\t{res}\nbut expected\n\t {expected_res}"


def main():
    # Base exercise:
    lines = ["my,fake,file", "has,two,rows"]
    reader = FancyReader(lines, fieldnames=["w1", "w2", "w3"])
    row = next(iter(reader))
    test_equal(row.w1, "my")
    test_equal(row.w2, "fake")
    test_equal(row.w3, "file")

    lines = ["my,second,'fake,file'", "still,'has,two',rows"]
    reader = list(FancyReader(lines, fieldnames=["w1", "w2", "w3"], quotechar="'"))
    test_equal(reader[0].w3, "fake,file")

    # Bonus 1
    lines = ['my,fake,file', 'has,two,rows']
    reader = FancyReader(lines, fieldnames=['w1', 'w2', 'w3'])
    row = next(reader)
    test_equal(repr(row), "Row(w1='my', w2='fake', w3='file')")

    # Bonus 2
    lines = ['w1,w2,w3', 'my,fake,file', 'has,two,rows']
    reader = FancyReader(lines)
    row = next(reader)
    test_equal(repr(row), "Row(w1='my', w2='fake', w3='file')")

    # Bonus 3
    lines = 'red,1\nblue,2\ngreen,3'.splitlines()
    reader = FancyReader(lines, fieldnames=['color', 'number'])
    next(reader)
    test_equal(reader.line_num, 1)
    next(reader)
    test_equal(reader.line_num, 2)

    print("Passed tests!")


if __name__ == "__main__":
    main()
