from definitions import read_inputs, read_inputs2
import math

input_example, puzzle_input = read_inputs('Day 3')

try:
    input_example2 = read_inputs2('Day 3')
except:
    pass


def soolution(example):
    numbers = []
    stars = []
    k = 0
    inputlist = example.split("\n")
    x = len(inputlist[0])
    y = len(inputlist)

    def goodnumber(n, inputlist):
        left = max(n[2] - n[3], 0)
        right = min(n[2] + 1, x - 1) + 1
        up = max(0, n[1] - 1)
        down = min(n[1] + 1, y - 1) + 1
        for i in range(left, right):
            for j in range(up, down):
                c = inputlist[j][i]
                if not c.isdigit() and c != ".":
                    return n[0]
        return 0

    def gear(star, inputlist, numbers):
        left = max(star[1] - 1, 0)
        right = min(star[1] + 1, x - 1) + 1
        up = max(0, star[0] - 1)
        down = min(star[0] + 1, y - 1) + 1
        digitlist = []
        for i in range(left, right):
            for j in range(up, down):
                c = inputlist[j][i]
                if c.isdigit():
                    digitlist.append([j, i])
        surround = []
        for dig in digitlist:
            for n in numbers:
                if dig[0] == n[1] and n[2] >= dig[1] >= n[2] - n[3] + 1:
                    surround.append(n)
        surroundn = list(set(surround))
        if len(surroundn) == 2:
            surroundn = [surroundn[0][0], surroundn[1][0]]
            return math.prod(surroundn)
        return 0

    for l in inputlist:
        curnum = ""
        numlen = 0
        for i in range(x):
            c = l[i]
            if c.isdigit():
                curnum += c
                numlen += 1
                if i == x - 1:
                    number = int(curnum)
                    numbers.append((number, k, i, numlen))
            elif curnum:
                number = int(curnum)
                curnum = ""
                numbers.append((number, k, i - 1, numlen))
                numlen = 0
            if c == "*":
                stars.append((k, i))
        k += 1

    result = 0
    result2 = 0
    for n in numbers:
        gn = goodnumber(n, inputlist)
        result += gn
    for star in stars:
        gearstar = gear(star, inputlist, numbers)
        result2 += gearstar

    print('Solution for part 1 is:', result)
    print('Solution for part 2 is:', result2)


print('\ninput_example')
soolution(input_example)
print('\npuzzle_input')
soolution(puzzle_input)
