import os.path

PATH = os.path.dirname(os.path.abspath(__file__))

def solve(problem_set: set):

    for number in problem_set:
        diff = 2020 - number
        if diff in problem_set:
            return (number * diff)

    return 'NO SOLUTION'


def main():

    with open(os.path.join(PATH, 'testcase.txt'), 'r') as r:
        problem_set = {int(num) for num in r}

    print(solve(problem_set))

main()
