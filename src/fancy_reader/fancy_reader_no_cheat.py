import types
from collections.abc import Iterable
from dataclasses import dataclass


@dataclass
class Dialect:
    delimiter: str = ','  # Field separator (one character)
    doublequote: bool = True  # Flag controlling whether quotechar instances are doubled
    escapechar: str = None  # Character used to indicate an escape sequence
    lineterminator: str = "\r\n"  # String used by writer to terminate a line
    quotechar: str = '"'  # String to surround fields containing special values (one character)
    # quoting = QUOTE_MINIMAL # Controls quoting behavior described earlier
    skipinitialspace: bool = False  # Ignore whitespace after the field delimiter


class FancyReader:
    def __init__(self, csv_file: Iterable[str], fieldnames: list[str], dialect='excel', **fmtparams):
        self.csv_file = csv_file
        self.fieldnames = fieldnames
        self.dialect = Dialect()
        self.dialect.quotechar = "'"

    def __iter__(self):
        for line in self.csv_file:
            result = types.SimpleNamespace()
            # line.split(self.dialect.quotechar)
            # https://github.com/python/cpython/blob/main/Lib/csv.py#L222
            values = line.split(self.dialect.delimiter)
            print("######")
            print(values)
            print(self.fieldnames)
            for attribute, value in zip(self.fieldnames, values, strict=True):
                setattr(result, attribute, value)
            yield result

    def __next__(self):
        for line in self.csv_file:
            values = line.split(self.dialect.delimiter)
            yield types.SimpleNamespace(**{attribute: value for attribute, value in zip(self.fieldnames, values)})

    def __repr__(self):
        return f"{type(self).__name__}(file={self.csv_file})"


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
    reader = FancyReader(lines, fieldnames=["w1", "w2"])
    for row in reader:
        print(row)
    print("Passed tests!")


if __name__ == "__main__":
    main()
