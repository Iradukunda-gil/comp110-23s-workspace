"""Example function for unit test"""
def sum(xs: list[float]) -> float:
    """return some of all xs in the list"""
    sum_total: float = 0.0
    for x in range(0,len(xs)):
        sum_total += xs[x]
    return sum_total
