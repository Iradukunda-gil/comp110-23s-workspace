"""EX05 - `list` Utility Functions."""
__author__ = "730458371"


def only_evens(even_list: list[int]) -> list[int]:
    """Defining only_evens and return functions."""
    even_num = []
    for num in even_list:
        if num % 2 == 0:
            even_num.append(num)
    return even_num


def concat(even_lists: list[int], even_lists2: list[int]) -> list[int]:
    """Defining concat and return functions."""
    even_nums = []
    for num in even_lists:
        even_nums.append(num)
    for num in even_lists2:
        even_nums.append(num)
    return even_nums 


def sub(a_lists: list[int], start_idx: int, end_idx: int) -> list[int]:
    """Defining sub and return functions."""
    b_lists: list[int] = []
    if start_idx < 0:
        start_idx = 0
    if start_idx == len(a_lists):
        return b_lists
    if len(a_lists) == 0:
        return b_lists
    if start_idx >= len(a_lists):
        return b_lists
    if end_idx <= 0:
        return b_lists
    for x in a_lists:
        if end_idx > len(a_lists) and x >= a_lists[start_idx]:
            b_lists.append(x)
        else:
            if x >= a_lists[start_idx]:
                if x < a_lists[end_idx]: 
                    b_lists.append(x)
    return b_lists