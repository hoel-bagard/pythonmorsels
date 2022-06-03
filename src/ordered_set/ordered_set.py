from typing import Any, Iterable


class OrderedSet:
    def __init__(self, data: Iterable = ()):
        self.data = dict.fromkeys(data)

    def __repr__(self):
        return f"{type(self).__name__}({list(self.data.keys())})"

    def __len__(self):
        return len(self.data)

    def __iter__(self):
        return iter(self.data.keys())

    def __contains__(self, item):
        return item in self.data

    # Bonus 2
    def __eq__(self, other: Any):
        if isinstance(other, OrderedSet):
            if not len(self) == len(other):
                return False
            return all(item1 == item2 for item1, item2 in zip(self, other))
        if isinstance(other, set):
            return set(self) == other
        return NotImplemented

    # Bonus 3
    def add(self, item):
        self.data[item] = None

    def discard(self, item):
        self.data.pop(item, None)


if __name__ == "__main__":
    # Base exercise
    ordered_set = OrderedSet()
    ordered_words = ["these", "are", "words", "in", "an", "order"]
    ordered_set = OrderedSet(ordered_words)
    # print(ordered_set)
    # print(*ordered_set)
    words = OrderedSet(["repeated", "words", "are", "not", "repeated"])
    assert list(words) == ["repeated", "words", "are", "not"], f"Oups: {words}"
    assert len(words) == 4, f"Wrong length {len(words)}"
    assert "Python" not in words, "Should not be in words."

    # Bonus 2
    assert OrderedSet(["how", "are", "you"]) != OrderedSet(["how", "you", "are"]), ""
    assert OrderedSet(["how", "are", "you"]) == {"how", "you", "are"}, ""
    assert OrderedSet(["how", "are", "you"]) != ["how", "are", "you"], ""

    # Bonus 3
    words = OrderedSet(["hello", "hello", "how", "are", "you"])
    words.add("doing")
    assert words == OrderedSet(["hello", "how", "are", "you", "doing"]), f"Missing new element: {words}"
    words.discard('are')
    assert words == OrderedSet(["hello", "how", "you", "doing"]), f"Element not deleted: {words}"

    print("Passed the tests")
