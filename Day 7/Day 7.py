from definitions import read_inputs, read_inputs2
import math

input_example, puzzle_input = read_inputs('Day 7')

try:
    input_example2 = read_inputs2('Day 7')
except:
    pass

order = {'A': 15, 'K': 14, 'Q': 13, 'J': 12, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}
order2 = {'A': 15, 'K': 14, 'Q': 13, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2, 'J': 1}


def checkhand(h):
    d = {}
    for c in h:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    m = d[max(d, key=d.get)]
    if m == 5:
        return 7  # five of a kind
    if m == 4:
        return 6  # four of a kind
    if m == 3 and len(d) == 2:
        return 5  # full house
    if m == 3:
        return 4  # three of a kind
    if m == 2 and len(d) == 3:
        return 3  # two pairs
    if m == 2 and len(d) == 4:
        return 2  # one pair
    return 1  # high card

def checkhand2(h):
    d = {}
    jokers=0
    for c in h:
        if c=='J':
            jokers+=1
            continue
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    m=0
    if d:
        m = d[max(d, key=d.get)]
    m = min(5, m + jokers)
    if m == 5:
        return 7  # five of a kind
    if m == 4:
        return 6  # four of a kind
    if m == 3 and len(d) == 2:
        return 5  # full house
    if m == 3:
        return 4  # three of a kind
    if m == 2 and len(d) == 3:
        return 3  # two pairs
    if m == 2 and len(d) == 4:
        return 2  # one pair
    return 1  # high card


def compare_hands(h1, h2, f, o):
    score1 = f(h1)
    score2 = f(h2)
    if score1 > score2:
        return 1
    if score1 < score2:
        return 2
    for i in range(len(h1)):
        if o[h1[i]] > o[h2[i]]:
            return 1
        if o[h1[i]] < o[h2[i]]:
            return 2
    return 0  # same hands


def sort(array, f, o):
    less = []
    equal = []
    greater = []
    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if compare_hands(x, pivot, f, o) == 2:
                less.append(x)
            elif compare_hands(x, pivot, f, o) == 0:
                equal.append(x)
            elif compare_hands(x, pivot, f, o) == 1:
                greater.append(x)
        return sort(less, f, o) + equal + sort(greater, f, o)
    else:
        return array


def soolution(example):
    s = example.split("\n")
    hands = []
    bids = {}
    for l in s:
        l = l.split(' ')
        hands.append(l[0])
        bids[l[0]] = int(l[1])
    hands = sort(hands, checkhand, order)
    result = 0
    for i in range(len(hands)):
        result += (i + 1) * bids[hands[i]]
    print('Solution for part 1 is:', result)

    hands2 = sort(hands, checkhand2, order2)
    result = 0
    for i in range(len(hands2)):
        result += (i + 1) * bids[hands2[i]]
    print('Solution for part 2 is:', result)


print('\ninput_example')
soolution(input_example)
print('\npuzzle_input')
soolution(puzzle_input)
