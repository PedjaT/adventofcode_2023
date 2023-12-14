from definitions import read_inputs, read_inputs2
import math

input_example, puzzle_input = read_inputs('Day 14')

try:
    input_example2 = read_inputs2('Day 14')
except:
    pass


def step(l, direction='up'):
    change=0
    if direction == 'up':
        for i in range(0,len(l)-1):
            if l[i]=='.' and l[i+1]=='O':
                l[i], l[i+1]='O', '.'
                change=1
    else:
        for i in range(len(l) - 1, 0, -1):
            if l[i] == '.' and l[i - 1] == 'O':
                l[i], l[i - 1] = 'O', '.'
                change = 1
    return change


def round(s, direction='up'):
    sT = [''.join(k) for k in zip(*s)]
    news=[]
    for l in sT:
        l=list(l)
        change=1
        while change:
            change=step(l, direction)
        news.append(l)
    return news


def circle(s):
    return round(round(round(round(s)), "down"), "down")


def fullload(s):
    full=0
    for i in range(len(s)):
        full+=s[i].count('O')*(len(s)-i)
    return full


def solution(example):
    s = example.split("\n")

    # part 2
    new_reflectors=[s]
    new_r = circle(s)
    while new_r not in new_reflectors:
        new_reflectors.append(new_r)
        new_r=circle(new_r)
    ind = new_reflectors.index(new_r)
    period = len(new_reflectors) - ind
    fullload(new_reflectors[ind + ((1000000000 - ind) % period)])

    print("solution for part 1 is", fullload([''.join(k) for k in zip(*round(s))]))
    print("solution for part 2 is", fullload(new_reflectors[ind + ((1000000000 - ind) % period)]))


print('\ninput_example')
solution(input_example)
print('\npuzzle_input')
solution(puzzle_input)
