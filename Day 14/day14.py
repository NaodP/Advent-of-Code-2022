# Naod Philemon
# 12/14/2022

import re
import copy

def flow(world, MAX, MIN):
    sand = [500,0]
    count = 0

    while True:
        L, M, R = (sand[0]-1,sand[1]+1), (sand[0], sand[1]+1), (sand[0]+1, sand[1]+1)

        # If Out Of Bounds
        if (sand[0] > MAX[0] or sand[0] < MIN) or (sand[1] > MAX[1] or sand[1] < 0): return count

        # If Can Move
        elif M not in world: sand = list(M)
        elif L not in world: sand = list(L)
        elif R not in world: sand = list(R)

        # If Resting
        elif L in world and M in world and R in world:
            count += 1
            world.add(tuple(sand))
            if sand == [500,0]: return count
            sand = [500,0]

def createWorld(paths):
    world = set()
    MAX, MIN = (0,0), 500

    for path in paths:
        for i in range(len(path)-1):
            start, end = copy.deepcopy(path[i]), copy.deepcopy(path[i+1])
            MAX = (max(MAX[0], start[0], end[0]), max(MAX[1], start[1], end[1]))
            MIN = (min(MIN, start[0], end[0]))
            
            while start != end:
                world.add(tuple(start))
                world.add(tuple(end))
                if start[0] < end[0]: start[0] += 1
                elif start[0] > end[0]: end[0] += 1
                elif start[1] < end[1]: start[1] += 1
                elif start[1] > end[1]: end[1] += 1
                
    return world, MAX, MIN

def part1(paths):
    world, MAX, MIN = createWorld(paths)
    
    return flow(world, MAX, MIN)
    
def part2(paths):
    world, MAX, MIN = createWorld(paths)

    # New Limits
    LIMIT = 145
    MAX = (MAX[0]+LIMIT, MAX[1]+2)
    MIN -= LIMIT
    for i in range(MIN, MAX[0]): world.add((i,MAX[1]))

    return flow(world, MAX, MIN)
    
def main():
    file = open('Day 14/day14-input.txt')
    paths = []

    for line in file:
        line = re.split(',|->', line.strip())
        path = []
        for i in range(0, len(line)-1, 2):
            path.append([int(line[i:i+2][0]), int(line[i:i+2][1])])
        paths.append(path)

    print('Part 1 -', part1(paths))
    print('Part 2 -', part2(paths))

# Start
main()