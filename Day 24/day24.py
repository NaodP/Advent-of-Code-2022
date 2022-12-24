# Naod Philemon
# 12/24/2022

import copy

def pic(world):
    for line in world:
        for pos in line:
            val = '#' if pos == '#' else len(pos)
            print(val, end='')
        print()
    print()

def part1(world):
    # Set Up World
    tempWorld = []
    for line in world:
        tempLine = []
        for pos in line:
            if pos == '#': tempLine.append('#')
            elif pos == '.': tempLine.append([])
            else: tempLine.append([pos])
        tempWorld.append(tempLine)
    world = copy.deepcopy(tempWorld)

    minutes = 0
    currentQueue = [(0,1)]
    safe = False

    while not safe:
        # Set New World
        newWorld = copy.deepcopy(world)
        for i in range(len(newWorld)):
            for j in range(len(newWorld[0])):
                if newWorld[i][j] != '#': newWorld[i][j] = []

        # Move Blizzards
        for i in range(len(world)):
            for j in range(len(world[0])):
                if world[i][j] == '#': continue
                if world[i][j] == []: continue
                
                for direction in world[i][j]:
                    # Up
                    if direction == '^':
                        if i-1 == 0: newWorld[len(world)-2][j].append('^')
                        else: newWorld[i-1][j].append('^')

                    # Right
                    elif direction == '>':
                        if j+1 == len(world[0])-1: newWorld[i][1].append('>')
                        else: newWorld[i][j+1].append('>')

                    # Left
                    elif direction == '<':
                        if j-1 == 0: newWorld[i][len(world[0])-2].append('<')
                        else: newWorld[i][j-1].append('<')

                    # Down
                    elif direction == 'v':
                        if i+1 == len(world)-1: newWorld[1][j].append('v')
                        else: newWorld[i+1][j].append('v')

        # Check If New Position Is Possible
        def possible(pos):
            if pos in newQueue: return False
            if pos[0] < 0 or pos[0] >= len(newWorld): return False
            if pos[1] < 0 or pos[1] >= len(newWorld[0]): return False
            if newWorld[pos[0]][pos[1]] == []: return True
            return False

        # Move To All Possible
        newQueue = []
        for pos in currentQueue:
            up = (pos[0]-1, pos[1])
            left = (pos[0], pos[1]-1)
            down = (pos[0]+1, pos[1])
            right = (pos[0], pos[1]+1)
            if possible(pos): newQueue.append(pos)
            if possible(up): newQueue.append(up)
            if possible(left): newQueue.append(left)
            if possible(down): newQueue.append(down)
            if possible(right): newQueue.append(right)
        currentQueue = copy.deepcopy(newQueue)

        # If Reached The End
        if ((len(world)-1, len(world[0])-2)) in newQueue: safe = True

        minutes += 1
        world = copy.deepcopy(newWorld)
        #pic(newWorld)

    return minutes

def part2(world):
    # Set Up World
    tempWorld = []
    for line in world:
        tempLine = []
        for pos in line:
            if pos == '#': tempLine.append('#')
            elif pos == '.': tempLine.append([])
            else: tempLine.append([pos])
        tempWorld.append(tempLine)
    world = copy.deepcopy(tempWorld)

    total = 0
    startingPositions = [(0,1), (len(world)-1,len(world[0])-2), (0,1), (len(world)-1,len(world[0])-2)]

    for _ in range(3):
        minutes = 0
        currentQueue = [startingPositions[_]]
        safe = False

        while not safe:
            # Set New World
            newWorld = copy.deepcopy(world)
            for i in range(len(newWorld)):
                for j in range(len(newWorld[0])):
                    if newWorld[i][j] != '#': newWorld[i][j] = []

            # Move Blizzards
            for i in range(len(world)):
                for j in range(len(world[0])):
                    if world[i][j] == '#': continue
                    if world[i][j] == []: continue
                    
                    for direction in world[i][j]:
                        # Up
                        if direction == '^':
                            if i-1 == 0: newWorld[len(world)-2][j].append('^')
                            else: newWorld[i-1][j].append('^')

                        # Right
                        elif direction == '>':
                            if j+1 == len(world[0])-1: newWorld[i][1].append('>')
                            else: newWorld[i][j+1].append('>')

                        # Left
                        elif direction == '<':
                            if j-1 == 0: newWorld[i][len(world[0])-2].append('<')
                            else: newWorld[i][j-1].append('<')

                        # Down
                        elif direction == 'v':
                            if i+1 == len(world)-1: newWorld[1][j].append('v')
                            else: newWorld[i+1][j].append('v')

            # Check If New Position Is Possible
            def possible(pos):
                if pos in newQueue: return False
                if pos[0] < 0 or pos[0] >= len(newWorld): return False
                if pos[1] < 0 or pos[1] >= len(newWorld[0]): return False
                if newWorld[pos[0]][pos[1]] == []: return True
                return False

            # Move To All Possible
            newQueue = []
            for pos in currentQueue:
                up = (pos[0]-1, pos[1])
                left = (pos[0], pos[1]-1)
                down = (pos[0]+1, pos[1])
                right = (pos[0], pos[1]+1)
                if possible(pos): newQueue.append(pos)
                if possible(up): newQueue.append(up)
                if possible(left): newQueue.append(left)
                if possible(down): newQueue.append(down)
                if possible(right): newQueue.append(right)
            currentQueue = copy.deepcopy(newQueue)

            # If Reached The End
            if (startingPositions[_+1]) in newQueue: safe = True

            minutes += 1
            world = copy.deepcopy(newWorld)

        total += minutes

    return total

def main():
    file = open('Day 24/day24-input.txt')
    world = []

    for line in file: world.append(line.strip())

    print('Part 1 -', part1(world)) # 271
    print('Part 2 -', part2(world)) # 813

# Start
main()