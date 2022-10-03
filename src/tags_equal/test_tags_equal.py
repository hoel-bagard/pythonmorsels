import pytest

from src.tags_equal.tags_equal import tags_equal


@pytest.mark.parametrize("tag1, tag2, is_equal", [
    ("<b>", "<b>", True),
    ("<baba>", "<baba>", True),
    ("<a>", "<b>", False),
    ("<abab>", "<baba>", False),
])
def test_no_attributes(tag1: str, tag2: str, is_equal: bool):
    assert tags_equal(tag1, tag2) == is_equal


@pytest.mark.parametrize("tag1, tag2, is_equal", [
    ("<img width=400>", "<img width=400>", True),
    ("<img width=400>", "<IMG width=400>", True),
    ("<img width=400>", "<img width=200>", False),
    ("<img width=400>", "<img height=400>", False),
    ("<img width=400>", "<IMG height=400>", False),
])
def test_with_matching_attributes(tag1: str, tag2: str, is_equal: bool):
    assert tags_equal(tag1, tag2) == is_equal


@pytest.mark.parametrize("tag1, tag2, is_equal", [
    ("<img width=400 height=200>", "<img width=400 height=200>", True),
    ("<img width=200 height=400>", "<img width=400 height=200>", False),

])
def test_with_multiple_matching_attributes(tag1: str, tag2: str, is_equal: bool):
    assert tags_equal(tag1, tag2) == is_equal


@pytest.mark.parametrize("tag1, tag2, is_equal", [
    ("<img height=200 width=400>", "<img width=400 height=200>", True),
    ("<img height=400 width=200>", "<img width=400 height=200>", False),

])
def test_different_order_attributes(tag1: str, tag2: str, is_equal: bool):
    assert tags_equal(tag1, tag2) == is_equal


@pytest.mark.parametrize("tag1, tag2, is_equal", [
    ("<input type=hidden>", "<input TYPE=hidden>", True),
    ("<input type=hidden>", "<input Type=hidden>", True),
    ("<input type=HIDDEN>", "<input TYPO=HIDDEN>", False),
    ("<input type=hidden>", "<input TYPO=hide>", False),
])
def test_attributes_with_different_case(tag1: str, tag2: str, is_equal: bool):
    assert tags_equal(tag1, tag2) == is_equal


@pytest.mark.parametrize("tag1, tag2, is_equal", [
    ("<IMG height=200 width=400>", "<img Width=400 Height=200>", True),
    ("<img height=400 WIDTH=200>", "<Img width=400 HEIGHT=200>", False),
])
def test_different_order_and_case(tag1: str, tag2: str, is_equal: bool):
    assert tags_equal(tag1, tag2) == is_equal


@pytest.mark.bonus1
class TestBonus1:
    @pytest.mark.parametrize("tag1, tag2, is_equal", [
        ("<input type=hidden type=input>", "<input type=hidden>", True),
        ("<img type=input type=hidden>", "<Img type=hidden>", False),
        ("<input TYPE=hidden type=input>", "<input type=hidden>", True)
    ])
    def test_ignore_duplicate_keys(self, tag1: str, tag2: str, is_equal: bool):
        assert tags_equal(tag1, tag2) == is_equal


@pytest.mark.bonus2
class TestBonus2:
    @pytest.mark.parametrize("tag1, tag2, is_equal", [
        ("<input type=checkbox checked>", "<input checked type=checkbox>", True),
        ("<img type=checkbox checked>", "<Img type=checkbox>", False),
        ("<input type=checkbox checked>", "<input type=checkbox CHECKED>", True)
    ])
    def test_valueless_keys(self, tag1: str, tag2: str, is_equal: bool):
        assert tags_equal(tag1, tag2) == is_equal


@pytest.mark.bonus3
class TestBonus3:
    @pytest.mark.parametrize("tag1, tag2, is_equal", [
        ("<input type='text'>", "<input type=text>", True),
        ("<img type='text'>", "<Img type=hidden>", False),
        ("""<input type=text placeholder='Hi there' value="Hi friend">""",
         "<input type=text value='Hi friend' placeholder='Hi there'>",
         True),
        ("<input type=text value='Hi there' placeholder='Hi friend'>",
         "<input type=text value='Hi friend' placeholder='Hi there'>",
         False)
    ])
    def test_quotes(self, tag1: str, tag2: str, is_equal: bool):
        assert tags_equal(tag1, tag2) == is_equal
