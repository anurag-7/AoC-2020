import os.path
from typing import List, Tuple

PATH: str = os.path.dirname(os.path.abspath(__file__))
Element = Tuple[int, int, str, str]


def solve(testcase: List[Element]) -> int:
    count: int = 0

    for c_min, c_max, char, password in testcase:

        if c_min <= password.count(char) <= c_max:
            count += 1

    return count


def main() -> None:

    with open(os.path.join(PATH, 'input.txt'), 'r') as r:
        testcase: List[Element] = []

        for line in r:
            c_range, char, password = line.split(' ')
            c_min, c_max = map(int, c_range.split('-'))

            # char[0] to get the character, for example: "c:"
            testcase.append((c_min, c_max, char[0], password))

    print(solve(testcase))

main()
