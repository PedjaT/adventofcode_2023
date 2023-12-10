from definitions import read_inputs, read_inputs2

input_example, puzzle_input = read_inputs('Day 1')

try:
    input_example2 = read_inputs2('Day 1', 1)[0]
except:
    pass


def solution1(example):
    s = example.split('\n')
    cs = 0
    for l in s:
        num = ''
        for i in l:
            if i.isdigit():
                num += i
        if len(num) == 1:
            num += num
        elif len(num) > 2:
            num = num[0] + num[-1]
        num = int(num)
        cs += num
    print('Solution for part 1 is:', cs)


def solution2(example):
    s = example.split('\n')
    cs = 0
    for l in s:
        d = {'one': 'o1e', 'two': 't2o', 'three': 't3e', 'four': 'f4r', 'five': 'f5e', 'six': 's6x', 'seven': 's7n',
             'eight': 'e8t', 'nine': 'n9e'}
        for k in d:
            l = l.replace(k, d[k])
        num = ''
        for i in l:
            if i.isdigit():
                num += i
        if len(num) == 1:
            num += num
        elif len(num) > 2:
            num = num[0] + num[-1]
        num = int(num)
        cs += num
    print('Solution for part 2 is:', cs)


print('\ninput_example')
solution1(input_example)
solution2(input_example2)
print('\npuzzle_input')
solution1(puzzle_input)
solution2(puzzle_input)
