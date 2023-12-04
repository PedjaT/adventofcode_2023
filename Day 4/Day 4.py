from definitions import read_inputs, read_inputs2

input_example, puzzle_input = read_inputs('Day 4')

try:
    input_example2 = read_inputs2('Day 4')
except:
    pass


def soolution(example):
    result = 0
    inputlist = example.split("\n")
    fl = inputlist[0]
    fl = fl.replace('  ', ' ')
    fl = fl.split(': ')[1].split(' | ')
    nextten = [1] * len(fl[0].split(' '))
    numberofcards = 0
    for l in inputlist:
        card = {"wn": [], "have": []}
        l = l.replace('  ', ' ')
        l = l.split(': ')[1].split(' | ')
        card['wn'] = [int(x) for x in l[0].split(' ')]
        card['have'] = [int(x) for x in l[1].split(' ')]
        winning = list(set(card['wn']) & set(card['have']))
        winningl = len(winning)
        if winning:
            result += 2 ** (winningl - 1)
        next = nextten[0]
        numberofcards += next
        nextten = nextten[1:] + [1]
        for i in range(winningl):
            nextten[i] += next

    print('Solution for part 1 is:', result)
    print('Solution for part 2 is:', numberofcards)


print('\ninput_example')
soolution(input_example)
print('\npuzzle_input')
soolution(puzzle_input)
