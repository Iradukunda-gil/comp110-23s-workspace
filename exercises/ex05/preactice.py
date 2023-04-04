def main() -> None:
    names0: dict[str,str] = {"Pre." : "lily", "VP": "Ruby"}
    names1: dict[str,str] = {"VP":"Carlos", "sec" : "Lin"}
    officers: dict[str,str] = merge(names0, names1)
def merge(a: dict[str,str], b: dict[str,str]) -> dict[str,str]:
    result: dict[str,str] = {}
    for key in a:
        print(key)

main
