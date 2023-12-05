from definitions import read_inputs, read_inputs2
import copy

input_example, puzzle_input = read_inputs('Day 5')

try:
    input_example2 = read_inputs2('Day 5')
except:
    pass


def intointervals(mapping):
    mintervals = []
    for m in mapping:
        mintervals.append([m[1], m[1] + m[2] - 1])
    return sorted(mintervals, key=lambda tup: tup[0])


def split_interval(seed, intervals):
    main_interval = [seed[0], seed[0] + seed[1] - 1]
    result = []
    start, end = main_interval
    for interval in intervals:
        if start < interval[0]:
            result.append([start, min(end, interval[0] - 1)])
        if start <= interval[1] and end >= interval[0]:
            result.append([max(start, interval[0]), min(end, interval[1])])
        start = max(start, interval[1] + 1)
    if start <= end:
        result.append([start, end])
    for i in range(len(result)):
        result[i][1] = result[i][1] - result[i][0] + 1
    return result


def soolution(example):
    s = example.split("\n")
    seeds = [int(x) for x in (s[0].split(": ")[1]).split(" ")]
    m = 0
    mapping = {0: []}
    for l in s[2:]:
        if l == '':
            m += 1
            mapping[m] = []
            continue
        if not l[0].isdigit():
            continue
        mapping[m].append([int(x) for x in l.split(" ")])
    # solution 1
    mappedseeds = []
    for seed in seeds:
        mappedseed = seed
        for k in mapping:
            curmap = mapping[k]
            for l in curmap:
                if not l[1] + l[2] > mappedseed >= l[1]:
                    continue
                else:
                    mappedseed -= l[1] - l[0]
                    break
        mappedseeds.append(mappedseed)
    # solution 2
    all_intervals = copy.deepcopy(seeds)
    for k in mapping:
        intervals = intointervals(mapping[k])
        all_new_intervals = []
        for i in range(0, len(all_intervals), 2):
            seed = [all_intervals[i], all_intervals[i + 1]]
            new_interevals = split_interval(seed, intervals)
            for interval in new_interevals:
                for l in mapping[k]:
                    if not l[1] + l[2] > interval[0] >= l[1]:
                        continue
                    else:
                        interval[0] -= l[1] - l[0]
                        break
                all_new_intervals.append(interval[0])
                all_new_intervals.append(interval[1])
        all_intervals = copy.deepcopy(all_new_intervals)
    print('Solution for part 1 is:', min(mappedseeds))
    print('Solution for part 2 is:', min(all_intervals[::2]))


print('\ninput_example')
soolution(input_example)
print('\npuzzle_input')
soolution(puzzle_input)
