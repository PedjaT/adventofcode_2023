import copy

from definitions import read_inputs, read_inputs2

input_example, puzzle_input = read_inputs('Day 19')

try:
    input_example2 = read_inputs2('Day 19', 1)[0]
except:
    pass


def partvalidation(part, all_rules, xmas, workflow):
    while workflow not in ["A", "R"]:
        rules = all_rules[workflow]
        for rule in rules:
            if len(rule) == 1:
                workflow = rule[0]
                break
            if eval(str(part[xmas[rule[0][0]]]) + rule[0][1:]):
                workflow = rule[1]
                break
    if workflow == "R":
        return 0
    elif workflow == "A":
        return sum(part)


def createtree(all_rules, xmas):
    active = 0
    path = ["in"]
    tree = {"in": [[[1, 4000], [1, 4000], [1, 4000], [1, 4000]]]}
    while path:
        key = path.pop(0)
        old_intervals = tree[key][0]
        intervals = copy.deepcopy(old_intervals)
        for rule in all_rules[key]:
            if len(rule) == 2:
                new_intervals = copy.deepcopy(intervals)
                if rule[0][1] == "<":
                    new_intervals[xmas[rule[0][0]]][1] = min(new_intervals[xmas[rule[0][0]]][1], int(rule[0][2:]) - 1)
                    intervals[xmas[rule[0][0]]][0] = max(intervals[xmas[rule[0][0]]][0], int(rule[0][2:]))
                    if new_intervals[xmas[rule[0][0]]][1] < new_intervals[xmas[rule[0][0]]][0]:
                        continue
                elif rule[0][1] == ">":
                    new_intervals[xmas[rule[0][0]]][0] = max(new_intervals[xmas[rule[0][0]]][0], int(rule[0][2:]) + 1)
                    intervals[xmas[rule[0][0]]][1] = min(intervals[xmas[rule[0][0]]][1], int(rule[0][2:]))
                    if new_intervals[xmas[rule[0][0]]][1] < new_intervals[xmas[rule[0][0]]][0]:
                        continue
                if rule[1] == 'A':
                    add = 1
                    for i in range(4):
                        add *= new_intervals[i][1] - new_intervals[i][0] + 1
                    active += add
                elif rule[1] != 'R':
                    path.append(rule[1])
                    tree[rule[1]] = [new_intervals]
            else:
                if rule[0] == 'A':
                    add = 1
                    for i in range(4):
                        add *= intervals[i][1] - intervals[i][0] + 1
                    active += add
                elif rule[0] != 'R':
                    path.append(rule[0])
                    tree[rule[0]] = [intervals]
    return active


def solution(example):
    rules_input, parts = example.split("\n\n")
    rules_input = rules_input.split("\n")
    parts = parts.split("\n")
    workflow = "in"
    all_rules = {}
    for l in rules_input:
        key, value = l[:-1].split('{')
        value = [rule.split(":") for rule in value.split(',')]
        all_rules[key] = value
    # part 1
    xmas = {'x': 0, 'm': 1, 'a': 2, 's': 3}
    for i in range(len(parts)):
        parts[i] = [int(x[2:]) for x in parts[i][1:-1].split(',')]
    result = 0
    for part in parts:
        result += partvalidation(part, all_rules, xmas, workflow)
    # part 2
    result2 = createtree(all_rules, xmas)
    print("solution for part 1 is", result)
    print("solution for part 2 is", result2)


print('\ninput_example')
solution(input_example)
print('\npuzzle_input')
solution(puzzle_input)
