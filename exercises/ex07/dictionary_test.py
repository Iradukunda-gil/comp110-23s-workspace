"""Pytest for Dictionary."""


import pytest


from exercises.ex07.dictionary import invert, favorite_color, count


def test_invert():
    """Test 1."""
    my_dictionary = {}
    assert invert(my_dictionary) == {}


def test_invert2():
    """Test 2."""
    checker = {}
    checker = {'a': 'z', 'b': 'y', 'c': 'x'}
    assert invert(checker) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_invert_duplicate_values():
    """Test 3."""
    with pytest.raises(KeyError):
        my_dictionary = {'kris': 'jordan', 'michael': 'jordan'}
        invert(my_dictionary)


def test_favColor1():
    """Test 4."""
    checker = {}
    checker = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(checker) == "blue"


def test_favColor2():
    """Test 5."""
    checker = {}
    checker = {"Marc": "yellow", "Gilbert": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(checker) == "yellow"


def test_favColor3(): 
    """Test 6."""
    checker = {} 
    checker = {"Marc": "yellow", "Gilbert": "yellow", "Ezri": "yellow", "Kris": "yellow"}
    assert favorite_color(checker) == "yellow"


def test_count1():
    """Test 7."""
    checker = []
    checker = ["1", "2", "2", "3"]
    assert count(checker) == {"1": 1, "2": 2, "3": 1}


def test_count2():
    """Test 8."""
    checker = []
    checker = ["2", "2", "2", "2"]
    assert count(checker) == {"2": 4}


def test_count3():
    """Test 9."""
    checker = []
    checker = []
    assert count(checker) == {}


if __name__ == '__main__':
    names_colors = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    print(favorite_color(names_colors))