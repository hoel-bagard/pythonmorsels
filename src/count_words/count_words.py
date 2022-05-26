import re
from collections import defaultdict


def count_words(sentence: str) -> dict[str, int]:
    word_list = sentence.lower().split()  # .lower() for bonus 1
    count_dict: dict[str, int] = defaultdict(lambda: 0)
    for word in word_list:
        word = re.findall(r"\b.*\b", word)[0]   # Bonus 2 here
        count_dict[word] += 1
    return dict(count_dict)


def main():
    # Base exercise:
    res = count_words("oh what a day what a lovely day")
    expected_res = {'oh': 1, 'what': 2, 'a': 2, 'day': 2, 'lovely': 1}
    assert res == expected_res, f"Wrong result, got:\n\t{res}\nbut expected\n\t {expected_res}"

    res = count_words("don't stop believing")
    expected_res = {"don't": 1, 'stop': 1, 'believing': 1}
    assert res == expected_res, f"Wrong result, got:\n\t{res}\nbut expected\n\t {expected_res}"

    # Bonus 1
    res = count_words("Oh what a day what a lovely day")
    expected_res = {'oh': 1, 'what': 2, 'a': 2, 'day': 2, 'lovely': 1}
    assert res == expected_res, f"Wrong result, got:\n\t{res}\nbut expected\n\t {expected_res}"

    # Bonus 2
    res = count_words("Oh what a day, what a lovely day!")
    expected_res = {'oh': 1, 'what': 2, 'a': 2, 'day': 2, 'lovely': 1}
    assert res == expected_res, f"Wrong result, got:\n\t{res}\nbut expected\n\t {expected_res}"


if __name__ == "__main__":
    main()
