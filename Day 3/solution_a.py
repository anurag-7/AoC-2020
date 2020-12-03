import os.path
from typing import List

PATH: str = os.path.dirname(os.path.abspath(__file__))


def solve(testcase: List[str]) -> int:
    x = trees = 0
    height: int = len(testcase)
    max_x: int = len(testcase[0]) - 1

    for y in range(height):
        if testcase[y][x] == '#':
            trees += 1
        x = (x + 3) % max_x

    return trees


def main() -> None:
    with open(os.path.join(PATH, 'input.txt'), 'r') as r:
        testcase: List[str] = [line for line in r]

    print(solve(testcase))

main()
