from definitions import read_inputs, read_inputs2
import math

input_example, puzzle_input = read_inputs('Day 6')

try:
    input_example2 = read_inputs2('Day 6')
except:
    pass


def solution(example):
    s = example.split("\n")
    # part 1
    l1 = (s[0].split(':'))[1].split(' ')
    times = []
    for k in l1:
        if k:
            times.append(int(k))
    l1 = (s[1].split(':'))[1].split(' ')
    distances = []
    for k in l1:
        if k:
            distances.append(int(k))
    counter = [0] * len(times)
    for i in range(len(times)):
        for j in range(times[i]):
            if (times[i] - j) * j > distances[i]:
                counter[i] += 1
    print('Solution for part 1 is:', math.prod(counter))

    # part 2
    time = int((s[0].split(':'))[1].replace(' ', ''))
    distance = int((s[1].split(':'))[1].replace(' ', ''))

    def solution2(time, distance):
        # (time-x)*x>distance
        # x^2-time*x+b<0
        # x12=(time+-sqrt(time^2-4distance))/2
        x1 = (time + math.sqrt(time ** 2 - 4 * distance)) / 2
        x2 = (time - math.sqrt(time ** 2 - 4 * distance)) / 2
        return math.floor(x1), math.ceil(x2)
    x1,x2=solution2(time, distance)
    print('Solution for part 2 is:', x1-x2+1)


print('\ninput_example')
solution(input_example)
print('\npuzzle_input')
solution(puzzle_input)
