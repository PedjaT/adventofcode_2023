import copy

from definitions import read_inputs, read_inputs2

input_example, puzzle_input = read_inputs('Day 17')

try:
    input_example2 = read_inputs2('Day 17', 1)[0]
except:
    pass


def dijkstra(m,start,end):
    d=len(m)
    MAX = 2*d*9
    distances={}
    for i in range(d):
        for j in range(d):
            for steps in range(3):
                for direction in range(4):
                    distances[i,j,steps+1,direction] = 0 if i==0 and j==0 else MAX
    mindistances={}
    for i in range(d):
        for j in range(d):
            mindistances[i, j] = 0 if i == 0 and j == 0 else MAX
    def mindist(distances, i,j):
        mini = MAX
        for steps in range(3):
            for direction in range(4):
                    if distances[i,j,steps+1,direction]<mini:
                        mini = distances[i,j,steps+1,direction]
        return mini
    # if we start as we are in step 1 direction up (3) we will reset direction in the first step for sure
    path = [start+(1,3)]
    ld = [(0,1), (1,0), (0,-1), (-1,0)]
    finished=False
    while path or finished:
        x, y, step, dir = path.pop(0)
        for i in range(len(ld)):
            dx, dy = ld[i]
            newdir = i
            newx, newy = x + dx, y + dy

            if 0 <= newx < d and 0 <= newy < d:
                if mindistances[newx, newy] + 10 < distances[x, y, step, dir] + m[newx][newy]:
                    continue
                if newdir==dir:
                    newstep = step + 1
                    if newstep>3:
                        continue
                elif (newdir-dir)%2==0 and (x,y)!=(0,0):
                    continue
                else:
                    newstep = 1

                new_distance = distances[x,y,step,dir] + m[newx][newy]
                if new_distance < distances[newx,newy,newstep,newdir]:
                    if new_distance < mindistances[newx, newy]:
                        mindistances[newx, newy] = new_distance
                    distances[newx, newy, newstep, newdir] = new_distance

                    for st in range(step):
                        try:
                            if distances[newx,newy,st,newdir]<=new_distance:
                                continue
                        except:
                            pass
                    path.append((newx, newy, newstep, newdir))


    return mindistances[end[0],end[1]], distances


def dijkstra2(m,start,end):
    d=len(m)
    MAX = 2*d*9
    distances={}
    for i in range(d):
        for j in range(d):
            for steps in range(10):
                for direction in range(4):
                    distances[i,j,steps+1,direction] = 0 if i==0 and j==0 else MAX
    mindistances={}
    for i in range(d):
        for j in range(d):
            mindistances[i, j] = 0 if i == 0 and j == 0 else MAX

    # if we start as we are in step 1 direction up (3) we will reset direction in the first step for sure
    path = [start+(5,3)]
    ld = [(0,1), (1,0), (0,-1), (-1,0)]
    while path:
        x, y, step, dir = path.pop(0)
        for i in range(len(ld)):
            dx, dy = ld[i]
            newdir = i
            newx, newy = x + dx, y + dy

            if 0 <= newx < d and 0 <= newy < d:
                # if mindistances[newx, newy] + 10 < distances[x, y, step, dir] + m[newx][newy]:
                #     continue
                if newdir==dir:
                    newstep = step + 1
                    if newstep>10:
                        continue
                elif (newdir-dir)%2==0 and (x,y)!=(0,0):
                    continue
                else:
                    if step<4:
                        continue
                    newstep = 1

                new_distance = distances[x,y,step,dir] + m[newx][newy]
                if new_distance < distances[newx,newy,newstep,newdir]:
                    if new_distance < mindistances[newx, newy] and newstep>=4:
                        mindistances[newx, newy] = new_distance
                    distances[newx, newy, newstep, newdir] = new_distance

                    path.append((newx, newy, newstep, newdir))


    return mindistances[end[0],end[1]], distances

def solution(example):
    s = example.split("\n")
    m=[]
    for l in s:
       m.append([int(x) for x in list(l)])
    d=len(s)
    start, end = (0,0), (d-1,d-1)
    mindistance, distances = dijkstra(m,start,end)
    print("solution for part 1 is", mindistance)

    mindistance, distances = dijkstra2(m, start, end)
    print("solution for part 2 is", mindistance)


print('\ninput_example')
solution(input_example)

print('\npuzzle_input')
solution(puzzle_input)
