import os.path
from typing import List, Tuple

PATH: str = os.path.dirname(os.path.abspath(__file__))
Element = Tuple[int, int, str, str]

def solve(testcase: List[Element]) -> int:
    count = 0

    for pos_a, pos_b, char, password in testcase:

        # decrement by one due to Toboggan Corporate Policies
        char_a, char_b = password[pos_a - 1], password[pos_b - 1]

        if char in (char_a, char_b) and char_a != char_b:
            count += 1

    return count


def main() -> None:

    with open(os.path.join(PATH, 'input.txt'), 'r') as r:
        testcase: List[Element] = []

        for line in r:
            c_range, char, password = line.split(' ')
            pos_a, pos_b = map(int, c_range.split('-'))

            # char[0] to get the character from excample: "c:"
            testcase.append((pos_a, pos_b, char[0], password))

    print(solve(testcase))

main()
