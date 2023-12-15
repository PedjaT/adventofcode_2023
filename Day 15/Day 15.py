from definitions import read_inputs, read_inputs2
import math

input_example, puzzle_input = read_inputs('Day 15')

try:
    input_example2 = read_inputs2('Day 15')
except:
    pass


def HASH(l):
    r = 0
    for c in l:
        r += ord(c)
        r *= 17
        r %= 256
    return r


def solution(example):
    s = example.split(",")
    result1 = 0
    boxes = dict((b, []) for b in range(256))
    for l in s:
        result1 += HASH(l)
        if '-' in l:
            box = HASH(l[:-1])
            for lens in boxes[box]:
                if lens[:-2] == l[:-1]:
                    boxes[box].remove(lens)
                    break
        elif '=' in l:
            box = HASH(l[:-2])
            replace = 0
            for i in range(len(boxes[box])):
                if boxes[box][i][:-2] == l[:-2]:
                    replace = 1
                    boxes[box][i] = l
                    break
            if not replace:
                boxes[box].append(l)
    result2 = 0
    for box in boxes:
        for i in range(len(boxes[box])):
            result2 += (1 + box) * (i + 1) * int(boxes[box][i][-1])

    print("solution for part 1 is", result1)
    print("solution for part 2 is", result2)


print('\ninput_example')
solution(input_example)
print('\npuzzle_input')
solution(puzzle_input)
