from shlex import split


def create_dict(attrs: str) -> dict[str, str]:
    attrs_dict: dict[str, str] = {}
    for attr in attrs:
        key, *value = attr.split('=')
        if key not in attrs_dict.keys():  # For Bonus 1
            attrs_dict[key] = value
    return attrs_dict


def tags_equal(tag1: str, tag2: str) -> bool:
    tag1, tag2 = split(tag1[1:-1].lower()), split(tag2[1:-1].lower())

    # Check that tag names are the same.
    if tag1.pop(0) != tag2.pop(0):
        return False

    tag1_dict = create_dict(tag1)
    tag2_dict = create_dict(tag2)

    # Check that they have the same attributes.
    if set(tag1_dict.keys()) != set(tag2_dict.keys()):
        return False

    # Check that they have the same attribute values
    for key in tag1_dict.keys():
        if tag1_dict[key] != tag2_dict[key]:
            return False

    return True


def main():
    # Base exercise:
    assert tags_equal("<img src=cats.jpg height=40>", "<IMG SRC=cats.jpg height=40>")
    assert not tags_equal("<img src=dogs.jpg width=99>", "<img src=dogs.jpg width=20>")
    assert tags_equal("<p>", "<P>")
    assert not tags_equal("<b>", "<p>")

    # Bonus 1
    assert tags_equal("<LABEL FOR=id_email for=id_username>", "<LABEL FOR=id_email>")
    assert not tags_equal("<LABEL FOR=id_email for=id_username>", "<LABEL FOR=id_username>")

    # Bonus 2
    assert tags_equal("<OPTION NAME=hawaii SELECTED>", "<option selected name=hawaii>")
    assert not tags_equal("<option name=hawaii>", "<option name=hawaii selected>")

    # Bonus 3
    assert tags_equal("<input value='hello there'>", '<input value="hello there">')
    assert tags_equal("<input value=hello>", "<input value='hello'>")
    assert not tags_equal("<input value='hi friend'>", "<input value='hi there'>")

    print("Passed the tests!")


if __name__ == "__main__":
    main()
