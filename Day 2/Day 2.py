from definitions import read_inputs, read_inputs2

input_example, puzzle_input = read_inputs('Day 2')

try:
    input_example2 = read_inputs2('Day 2')
except:
    pass


def soolution(example):
    s = example.split('\n')
    gamenumber=1
    cubes = {"red": 12, "green": 13, "blue": 14}
    gamesum = 0
    part2sum = 0
    for l in s:
        game=1
        l=l.split(':')[1][1:]
        l=l.split('; ')
        mincubes = {"red": 1, "green": 1, "blue": 1}
        for i in l:
            i=i.split(', ')
            for k in i:
                k=k.split(' ')
                if k[1]=="red":
                    mincubes["red"]=max(mincubes["red"], int(k[0]))
                    if int(k[0])>cubes["red"]:
                        game=0
                elif k[1]=="green":
                    mincubes["green"] = max(mincubes["green"], int(k[0]))
                    if int(k[0])>cubes["green"]:
                        game=0
                elif k[1]=="blue":
                    mincubes["blue"] = max(mincubes["blue"], int(k[0]))
                    if int(k[0])>cubes["blue"]:
                        game=0
        multipl=mincubes["red"]*mincubes["green"]*mincubes["blue"]
        if game:
            gamesum+=gamenumber
        part2sum+=multipl
        gamenumber+=1

    print('Solution for part 1 is:', gamesum)
    print('Solution for part 2 is:', part2sum)



print('\ninput_example')
soolution(input_example)
print('\npuzzle_input')
soolution(puzzle_input)
