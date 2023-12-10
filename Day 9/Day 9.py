from definitions import read_inputs, read_inputs2
import math

input_example, puzzle_input = read_inputs('Day 9')

try:
    input_example2 = read_inputs2('Day 9')
except:
    pass


def solution(example):
    s = example.split("\n")
    predictions1 = []
    predictions2 = []
    for l in s:
        l = [int(x) for x in l.split(' ')]
        ldiffs = [l]
        while not all(v == 0 for v in ldiffs[-1]):
            ldiffs.append([j - i for i, j in zip(ldiffs[-1][:-1], ldiffs[-1][1:])])
        # part 1
        ldiffs[-1].append(0)
        for i in range(len(ldiffs) - 2, -1, -1):
            ldiffs[i].append(ldiffs[i][-1] + ldiffs[i + 1][-1])
        predictions1.append(ldiffs[0][-1])
        # part 2
        ldiffs[-1].insert(0, 0)
        for i in range(len(ldiffs) - 2, -1, -1):
            ldiffs[i].insert(0, ldiffs[i][0] - ldiffs[i + 1][0])
        predictions2.append(ldiffs[0][0])

    print('Solution for part 1 is:', sum(predictions1))
    print('Solution for part 2 is:', sum(predictions2))


print('\ninput_example')
solution(input_example)
print('\npuzzle_input')
solution(puzzle_input)
