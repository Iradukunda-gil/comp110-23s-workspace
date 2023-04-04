"""EEX07 - Dictionary Functions."""
__author__ = "730458371"


def favorite_color(names_colors: dict[str, str]) -> str:
    """Returns favorite color."""
    color_counts: list[str] = []
    for count in names_colors:
        check = color_counts.append(names_colors[count])
    count: int = 0
    z = color_counts[0]
    for color in color_counts:
        check = color_counts.count(color)
        if check > count:
            count = check
            z = color
    return z
    

def invert(str1: dict[str, str]) -> dict[str, str]:
    """Returns inverted dictionary."""
    inverted: dict[str, str] = {}
    for key in str1:
        if str1[key] in inverted:
            raise KeyError("error message of your choice here!")
        inverted[str1[key]] = key
    return inverted


def count(values: list[str]) -> dict[str, int]:
    """Returns count in list."""
    result = {}
    for item in values:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result  