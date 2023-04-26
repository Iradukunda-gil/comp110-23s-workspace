"""EX04 - `list` Utility Functions."""
__author__ = "730458371"


def all(list_int: list[int], interger: int) -> bool:
    """Defining functions."""
    counter = 0
    list_int2: list[int] = []
    if list_int == []:
        return False
    while counter < len(list_int):
        if list_int[counter] == interger:
            list_int2.append(list_int[counter])
        else:
            return False
        counter += 1
    return True


def max(max_int: list[int]) -> int:
    """Defining functions."""
    if len(max_int) == 0:
        raise ValueError("max() arg is an empty List")
    count = 0
    checker = 1
    length = len(max_int)
    max_int2: int = max_int[0]
    while checker <= length - 1:
        if max_int2 < max_int[checker]:
            max_int2 = max_int[checker]
        checker += 1
        count += 1
    return max_int2 


def is_equal(list1_int: list[int], list2_int: list[int]) -> int:
    """Defining functions."""
    if list1_int == list2_int:
        return True
    else: 
        return False