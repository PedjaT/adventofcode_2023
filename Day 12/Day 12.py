from definitions import read_inputs, read_inputs2
import math

input_example, puzzle_input = read_inputs('Day 12')

try:
    input_example2 = read_inputs2('Day 12')
except:
    pass


from functools import cache


@cache
def combinations(p, s, h=0):
    """h - number of damaged in a row
    copied solution for learning/understanding
    """
    if p=="":
        if s==() and h==0:
            return 1
        else:
            return 0
    n = 0
    if p[0] in ("#", "?"):
        n += combinations(p[1:], s, h + 1)
    if p[0] in (".", "?") and ((s and s[0] == h) or not h):
        n += combinations(p[1:], s[1:] if h else s)
    return n


def solution(example):
    s = example.split("\n")
    result1 = 0
    result2 = 0

    for l in s:
        springs, records = l.split(" ")
        records = tuple([int(x) for x in records.split(",")])
        result1 += combinations(springs + '.', records, 0)
        result2 += combinations(((springs+'?')*5)[:-1]+'.', records*5, 0)
    print("solution for part 1 is", result1)
    print("solution for part 2 is", result2)


print('\ninput_example')
solution(input_example)
print('\npuzzle_input')
solution(puzzle_input)
