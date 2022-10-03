from typing import Iterable, TypeVar


T = TypeVar("T")


class OrderedSet(Iterable[T]):
    def __init__(self, data: Iterable[T] = ()):
        self.data = dict.fromkeys(data)

    def __repr__(self) -> str:
        return f"{type(self).__name__}({list(self.data.keys())})"

    def __len__(self) -> int:
        return len(self.data)

    def __iter__(self) -> Iterable[T]:
        return iter(self.data.keys())

    def __contains__(self, item: T) -> bool:
        return item in self.data

    # Bonus 2
    def __eq__(self, other: "OrderedSet[object]" | set[object] | object) -> bool:
        if isinstance(other, OrderedSet):
            if not len(self) == len(other):  # type: ignore
                return False
            return all(item1 == item2 for item1, item2 in zip(self, other))  # type: ignore
        if isinstance(other, set):
            return set(self) == other
        return NotImplemented

    # Bonus 3
    def add(self, item: T):
        self.data[item] = None

    def discard(self, item: T):
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
    words.discard("are")
    assert words == OrderedSet(["hello", "how", "you", "doing"]), f"Element not deleted: {words}"

    print("Passed the tests")
