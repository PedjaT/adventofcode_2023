import copy

from definitions import read_inputs, read_inputs2

input_example, puzzle_input = read_inputs('Day 18')

try:
    input_example2 = read_inputs2('Day 18', 1)[0]
except:
    pass


def finddimension(orders, coords, k):
    y, x = coords[-1]
    if orders[k][0] in ["L", 2]:
        x -= orders[k][1]

    elif orders[k][0] in ["R", 0]:
        x += orders[k][1]

    elif orders[k][0] in ["U", 3]:
        y -= orders[k][1]

    elif orders[k][0] in ["D", 1]:
        y += orders[k][1]
    coords.append((y, x))
    return orders[k][1]


def polygonArea(vertices):
    numberOfVertices = len(vertices)
    sum1 = 0
    sum2 = 0
    for i in range(0, numberOfVertices - 1):
        sum1 = sum1 + vertices[i][0] * vertices[i + 1][1]
        sum2 = sum2 + vertices[i][1] * vertices[i + 1][0]
    # Add xn.y1
    sum1 = sum1 + vertices[numberOfVertices - 1][0] * vertices[0][1]
    # Add x1.yn
    sum2 = sum2 + vertices[0][0] * vertices[numberOfVertices - 1][1]

    area = abs(sum1 - sum2) / 2
    return area


def solution(example):
    s = example.split("\n")
    orders1 = {}
    orders2 = {}
    perimeter1 = 0
    perimeter2 = 0
    coords1 = [(0, 0)]
    coords2 = [(0, 0)]
    k = 0
    for l in s:
        direction, meters, colour = l.split(" ")
        orders1[k] = (direction, int(meters))
        orders2[k] = (int(colour[-2:-1]), int(colour[2:-2], 16))
        perimeter1 += finddimension(orders1, coords1, k)
        perimeter2 += finddimension(orders2, coords2, k)
        k += 1

    print("solution for part 1 is", int(perimeter1 / 2 + polygonArea(coords1[:-1]) + 1))
    print("solution for part 2 is", int(perimeter2 / 2 + polygonArea(coords2[:-1]) + 1))


print('\ninput_example')
solution(input_example)
print('\npuzzle_input')
solution(puzzle_input)
