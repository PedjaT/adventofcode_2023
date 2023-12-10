from definitions import read_inputs, read_inputs2
import math
import numpy as np

input_example, puzzle_input = read_inputs('Day 10')

try:
    input_example2 = read_inputs2('Day 10', 1)[0]
except:
    pass


# d = {"|": "NS", "-": "WE", "L": "NE", "J": "NW", "7": "SW", "F": "SE", ".": "ground", "S": "S"}


def nextstep(current, s, M, queue, x1, x2, d, maximum):
    i, j = current[0], current[1]
    # north
    if (s[i][j] in "S|LJ") and i > 0 and s[i - 1][j] in "|7F" and (i - 1, j) not in d:
        M[i - 1, j] = int(M[i, j]) + 1
        if maximum[-1] < int(M[i, j]) + 1:
            maximum.append(int(M[i, j]) + 1)
        d.append((i - 1, j))
        queue.append((i - 1, j))
    # south
    if (s[i][j] in "S|7F") and i + 1 < x1 and s[i + 1][j] in "|LJ" and (i + 1, j) not in d:
        M[i + 1, j] = int(M[i, j]) + 1
        if maximum[-1] < int(M[i, j]) + 1:
            maximum.append(int(M[i, j]) + 1)
        d.append((i + 1, j))
        queue.append((i + 1, j))

    # west
    if (s[i][j] in "S-J7") and j > 0 and s[i][j - 1] in "-LF" and (i, j - 1) not in d:
        M[i, j - 1] = int(M[i, j]) + 1
        if maximum[-1] < int(M[i, j]) + 1:
            maximum.append(int(M[i, j]) + 1)
        d.append((i, j - 1))
        queue.append((i, j - 1))
    # east
    if (s[i][j] in "S-LF") and j + 1 < x2 and s[i][j + 1] in "-J7" and (i, j + 1) not in d:
        M[i, j + 1] = int(M[i, j]) + 1
        if maximum[-1] < int(M[i, j]) + 1:
            maximum.append(int(M[i, j]) + 1)
        d.append((i, j + 1))
        queue.append((i, j + 1))


def inside(current, M, s, zero, d):
    i, j = current[0], current[1]
    no_of_intersects = 0
    q = "reset"
    if not (zero[0] < i and zero[1] == j):
        for k in range(i):
            if M[k, j] in "|-LJ7F.":
                if M[k, j] == '7':
                    if (k, j) not in d:
                        continue
                else:
                    continue
            if s[k][j] == "-":
                no_of_intersects += 1
                continue
            if s[k][j] == "|":
                continue
            if s[k][j] in "7F":
                q = s[k][j]
                continue
            if s[k][j] in "LJ":
                if (s[k][j] == "L" and q == "7") or (s[k][j] == "J" and q == "F"):
                    no_of_intersects += 1
                q = "reset"
    else:
        for k in range(j):
            if M[i, k] in "|-LJ7F.":
                continue
            if s[i][k] == "|":
                no_of_intersects += 1
                continue
            if s[i][k] == "-":
                continue
            if s[i][k] in "LF":
                q = s[i][k]
                continue
            if s[i][k] in "7J":
                if (s[i][k] == "7" and q == "L") or (s[i][k] == "J" and q == "F"):
                    no_of_intersects += 1
                q = "reset"
    if no_of_intersects % 2:
        return 1
    return 0


def solution(example):
    s = example.split("\n")
    M = np.array([[x for x in l] for l in s], dtype='<U16')
    x1, x2 = len(s), len(s[0])
    for i in range(x1):
        for j in range(x2):
            if s[i][j] == 'S':
                M[i, j] = 0
                zero = (i, j)
                d = [(i, j)]
                queue = [(i, j)]
    maximum = [0]
    while queue:
        current = queue[0]
        nextstep(current, s, M, queue, x1, x2, d, maximum)
        queue.pop(0)
    print('Solution for part 1 is:', maximum[-1])

    result = 0
    for i in range(x1):
        for j in range(x2):
            if M[i, j] in "|-LJ7F.":
                result += inside((i, j), M, s, zero, d)
    print('Solution for part 2 is:', result)


print('\ninput_example1')
solution(input_example)
print('\ninput_example2')
solution(input_example2)
print('\npuzzle_input')
solution(puzzle_input)
