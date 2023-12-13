from definitions import read_inputs, read_inputs2
import math

input_example, puzzle_input = read_inputs('Day 13')

try:
    input_example2 = read_inputs2('Day 13')
except:
    pass


def diff_letters(a, b):
    return sum(a[i] != b[i] for i in range(len(a)))


def mirror_location(p, x, smudge):
    for i in range(1, x):
        upper = ''.join(p[max(i - (x - i), 0):i])
        lower = ''.join(p[min(x - 1, 2 * i - 1):i - 1:-1])
        if diff_letters(upper, lower) == smudge:
            return i
    return 0


def mirror(p, smudge=0):
    x1, x2 = len(p[0]), len(p)
    m1 = mirror_location(p, x2, smudge)
    if mirror_location(p, x2, smudge):
        return m1 * 100
    pT = [''.join(s) for s in zip(*p)]
    return mirror_location(pT, x1, smudge)


def solution(example):
    patterns = example.split("\n\n")
    result = 0
    result2 = 0
    for p in patterns:
        p = p.split("\n")
        result += mirror(p)
        result2 += mirror(p, 1)

    print("solution for part 1 is", result)
    print("solution for part 2 is", result2)


print('\ninput_example')
solution(input_example)
print('\npuzzle_input')
solution(puzzle_input)
