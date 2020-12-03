import os.path
from typing import List, Tuple

PATH: str = os.path.dirname(os.path.abspath(__file__))


def solve(testcase: List[str], slopes: List[Tuple[int]]) -> int:
    result: int = 1
    height: int = len(testcase)
    max_x: int = len(testcase[0]) - 1

    for i, j in slopes:
        x = trees = 0
        for y in range(0, height, j):
            if testcase[y][x] == '#':
                trees += 1
            x = (x + i) % max_x

        result *= trees

    return result


def main() -> None:

    slopes: List[Tuple[int]] = [
        (1, 1), (3, 1), (5, 1),
        (7, 1), (1, 2)
    ]

    with open(os.path.join(PATH, 'input.txt'), 'r') as r:
        testcase: List[str] = [line for line in r]

    print(solve(testcase, slopes))

main()
