from definitions import read_inputs, read_inputs2
import math

input_example, puzzle_input = read_inputs('Day 8')

try:
    input_example2, input_example3 = read_inputs2('Day 8', 2)
except:
    pass


def soolution1(example):
    s = example.split("\n")
    instructions = s[0]
    current = 'AAA'
    nodes = {}
    for n in s[2:]:
        node = n[:3]
        left = n[7:10]
        right = n[12:15]
        nodes[node] = (left, right)
    steps = 0
    while current != 'ZZZ':
        leftorright = instructions[steps % len(instructions)]
        current = nodes[current][leftorright == 'R']
        steps += 1
    print('Solution for part 1 is:', steps)


def countperiod(current, nodes, instructions):
    steps = 0
    visited_ends = {}
    while 1:
        leftorright = instructions[steps % len(instructions)]
        current = nodes[current][leftorright == 'R']
        steps += 1
        if current[2] == 'Z':
            if current not in visited_ends:
                visited_ends[current] = steps
            else:
                return visited_ends[current], steps - visited_ends[current]


def soolution2(example):
    s = example.split("\n")
    instructions = s[0]
    current = []
    nodes = {}
    for n in s[2:]:
        node = n[:3]
        left = n[7:10]
        right = n[12:15]
        nodes[node] = (left, right)
        if node[2] == 'A':
            current.append(node)
    l = []
    for n in current:
        untilperiod, period = countperiod(n, nodes, instructions)
        # for both example3, and puzzle steps until periodic end and periods are the some, so LCM of periods is enough
        l.append(period)
    print('Solution for part 2 is:', math.lcm(*l))


print('\ninput_example1')
soolution1(input_example)
print('\ninput_example2')
soolution1(input_example2)
print('\ninput_example3')
soolution2(input_example3)
print('\npuzzle_input')
soolution1(puzzle_input)
soolution2(puzzle_input)
