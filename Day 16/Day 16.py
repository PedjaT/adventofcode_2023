import copy

from definitions import read_inputs, read_inputs2

input_example, puzzle_input = read_inputs('Day 16')

try:
    input_example2 = read_inputs2('Day 16')
except:
    pass


def move(beams, beam, direction, x1, x2, current_beam):
    if direction == 'r' and beam[1] + 1 < x2:
        newbeam = (beam[0], beam[1] + 1)
        if newbeam not in beams:
            beams[newbeam] = [['r', 1]]
            current_beam.append(newbeam)
        else:
            if ['r', 0] not in beams[newbeam]:
                beams[newbeam].append(['r', 1])
                current_beam.append(newbeam)
    if direction == 'l' and beam[1] - 1 >= 0:
        newbeam = (beam[0], beam[1] - 1)
        if newbeam not in beams:
            beams[newbeam] = [['l', 1]]
            current_beam.append(newbeam)
        else:
            if ['l', 0] not in beams[newbeam]:
                beams[newbeam].append(['l', 1])
                current_beam.append(newbeam)
    if direction == 'u' and beam[0] - 1 >= 0:
        newbeam = (beam[0] - 1, beam[1])
        if newbeam not in beams:
            beams[newbeam] = [['u', 1]]
            current_beam.append(newbeam)
        else:
            if ['u', 0] not in beams[newbeam]:
                beams[newbeam].append(['u', 1])
                current_beam.append(newbeam)
    if direction == 'd' and beam[0] + 1 < x1:
        newbeam = (beam[0] + 1, beam[1])
        if newbeam not in beams:
            beams[newbeam] = [['d', 1]]
            current_beam.append(newbeam)
        else:
            if ['d', 0] not in beams[newbeam]:
                beams[newbeam].append(['d', 1])
                current_beam.append(newbeam)


def step(beams, s, x1, x2, current_beam):
    change = 0
    beam_keys = copy.deepcopy(current_beam)
    current_beam.clear()
    for beam in beam_keys:
        for i in range(len(beams[beam]) - 1, -1, -1):
            if beams[beam][i][1]:
                change = 1
                beams[beam][i][1] = 0
                direction = beams[beam][i][0]
                if s[beam[0]][beam[1]] == '.':
                    move(beams, beam, direction, x1, x2, current_beam)
                elif s[beam[0]][beam[1]] == '\\':
                    if direction == 'r':
                        direction = 'd'
                    elif direction == 'l':
                        direction = 'u'
                    elif direction == 'd':
                        direction = 'r'
                    elif direction == 'u':
                        direction = 'l'
                    move(beams, beam, direction, x1, x2, current_beam)
                elif s[beam[0]][beam[1]] == '/':
                    if direction == 'r':
                        direction = 'u'
                    elif direction == 'l':
                        direction = 'd'
                    elif direction == 'd':
                        direction = 'l'
                    elif direction == 'u':
                        direction = 'r'
                    move(beams, beam, direction, x1, x2, current_beam)
                elif s[beam[0]][beam[1]] == '-':
                    if direction in ['l', 'r']:
                        move(beams, beam, direction, x1, x2, current_beam)
                    elif direction in ['d', 'u']:
                        move(beams, beam, 'l', x1, x2, current_beam)
                        move(beams, beam, 'r', x1, x2, current_beam)
                elif s[beam[0]][beam[1]] == '|':
                    if direction in ['u', 'd']:
                        move(beams, beam, direction, x1, x2, current_beam)
                    elif direction in ['l', 'r']:
                        move(beams, beam, 'u', x1, x2, current_beam)
                        move(beams, beam, 'd', x1, x2, current_beam)
            else:
                break
    return change


def solution(example):
    s = example.split("\n")
    x1, x2 = len(s), len(s[0])
    # part 1
    beams = {(0, 0): [['r', 1]]}
    current_beam = [(0, 0)]
    while step(beams, s, x1, x2, current_beam):
        continue
    print("solution for part 1 is", len(beams))

    # part 2
    result = 0
    for i in range(x1):
        beams = {(i, 0): [['r', 1]]}
        current_beam = [(i, 0)]
        while step(beams, s, x1, x2, current_beam):
            continue
        if len(beams) > result:
            result = len(beams)
        beams = {(i, x2 - 1): [['l', 1]]}
        current_beam = [(i, x2 - 1)]
        while step(beams, s, x1, x2, current_beam):
            continue
        if len(beams) > result:
            result = len(beams)
    for j in range(x2):
        beams = {(0, j): [['d', 1]]}
        current_beam = [(0, j)]
        while step(beams, s, x1, x2, current_beam):
            continue
        if len(beams) > result:
            result = len(beams)
        beams = {(x1 - 1, j): [['u', 1]]}
        current_beam = [(x1 - 1, j)]
        while step(beams, s, x1, x2, current_beam):
            continue
        if len(beams) > result:
            result = len(beams)

    print("solution for part 2 is", result)


print('\ninput_example')
solution(input_example)
print('\npuzzle_input')
solution(puzzle_input)
