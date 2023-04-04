"""Example function for unit test"""
def sum(xs: list[float]) -> float:
    """return some of all xs in the list"""
    sum_total: float = 0.0
    idx: int = 0
    while idx < len(xs):
        sum_total += xs[idx]
        idx += 1
    return sum_total