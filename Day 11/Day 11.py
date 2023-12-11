from definitions import read_inputs, read_inputs2
import math

input_example, puzzle_input = read_inputs('Day 11')

try:
    input_example2 = read_inputs2('Day 11')
except:
    pass


def expand(s):
    rows = []
    columns = []
    for i in range(len(s)):
        if '#' not in s[i]:
            rows.append(i)
    for j in range(len(s[0])):
        if '#' not in ''.join([l[j] for l in s]):
            columns.append(j)
    return rows, columns


def distance(g1, g2, rows, columns, param):
    d = 0
    for i in range(min(g1[0], g2[0]) + 1, max(g1[0], g2[0])):
        if i in rows:
            d += param
    for j in range(min(g1[1], g2[1]) + 1, max(g1[1], g2[1])):
        if j in columns:
            d += param
    d += abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])
    return d


def solution(example):
    s = example.split("\n")
    rows, columns = expand(s)
    galaxies = []
    for i in range(len(s)):
        for j in range(len(s[0])):
            if s[i][j] == "#":
                galaxies.append((i, j))
    result = 0
    for i in range(len(galaxies) - 1):
        for j in range(i + 1, len(galaxies)):
            dis = distance(galaxies[i], galaxies[j], rows, columns, 1)
            result += dis
    print("solution for part 1 is", result)
    result = 0
    for i in range(len(galaxies) - 1):
        for j in range(i + 1, len(galaxies)):
            dis = distance(galaxies[i], galaxies[j], rows, columns, 999999)
            result += dis
    print("solution for part 2 is", result)


print('\ninput_example')
solution(input_example)
print('\npuzzle_input')
solution(puzzle_input)
