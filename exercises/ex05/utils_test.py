"""EX05 - `list` Utility Functions."""
__author__ = "730458371"

from exercises.ex05.utils import only_evens, sub, concat


def test_only_evens() -> None:
    """Test only_even when empty list is passed."""
    list1: list[int] = []
    assert only_evens(list1) == []


def test_only_evens1() -> None:
    """Test only_even when even number is passed."""
    assert only_evens([2, 4, 6, 8]) == [2, 4, 6, 8]


def test_only_evens2() -> None:
    """Test only_even when odd is passed."""
    assert only_evens([3]) == []


def test_sub() -> None:
    """Test sub when empty lists are passed."""
    list1: list[int] = []
    assert sub([list1], 1, 3) == []


def test_sub1() -> None:
    """Test sub."""
    assert sub([10, 20, 30], 0, 4) == [10, 20, 30]


def test_sub2() -> None:
    """Test sub."""
    assert sub([10, 20, 30], -1, 4) == [10, 20, 30]


def test_concat() -> None:
    """Test concat combining two list."""
    assert concat([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]


def test_concat1() -> None:
    """Test concat when one list is empty and one full."""
    assert concat([], [1, 2, 3]) == [1, 2, 3]


def test_concat2() -> None:
    """Test concat with two empty list."""
    assert concat([], []) == []