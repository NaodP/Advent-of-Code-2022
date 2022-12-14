# Naod Philemon
# 12/12/2022

def plot(seen):
    for i in range(40):
        for j in range(77):
            if (i,j) in seen: print('#', end='')
            else: print(' ', end='')
        print()

def part1(world, start):
    seen = set()
    queue = [(start)]
    xMax = len(world)
    yMax = len(world[0])

    while queue:
        current = queue.pop(0)
        if world[current[0]][current[1]] == '{': return current[2]
        seen.add((current[0],current[1]))
        curr = ord(world[current[0]][current[1]])
        directions = [(current[0]-1, current[1]), (current[0]+1, current[1]), (current[0], current[1]-1), (current[0], current[1]+1)]

        # Top
        for dir in directions:
            if dir not in seen and (dir[0] > -1 and dir[0] < xMax) and (dir[1] > -1 and dir[1] < yMax):
                new = ord(world[dir[0]][dir[1]]) 
                if new - curr < 2:
                    queue.append((dir[0],dir[1],current[2]+1))
                    seen.add(dir)
    
    return part1(world,(20,0,0))

def part2(world):
    xMax = len(world)
    yMax = len(world[0])
    candidates = []
    minimum = part1(world,(20,0,0))

    for i in range(xMax):
        for j in range(yMax):
            if world[i][j] == 'a':
                trapped = True
                if(i-1 > -1):
                    if world[i-1][j] != 'a': trapped = False
                if(i+1 < xMax):
                    if world[i+1][j] != 'a': trapped = False
                if(j-1 > -1):
                    if world[i][j-1] != 'a': trapped = False
                if(j+1 < yMax):
                    if world[i][j+1] != 'a': trapped = False

                if not trapped:
                    candidates.append((i,j,0))

    for candidate in candidates:
        minimum = min(minimum,part1(world,candidate))
    
    return minimum

def part2Better(world, start):
    seen = set()
    queue = [(start)]
    xMax = len(world)
    yMax = len(world[0])

    while queue:
        current = queue.pop(0)
        if world[current[0]][current[1]] == 'a': return current[2]
        seen.add((current[0],current[1]))
        curr = ord(world[current[0]][current[1]])
        directions = [(current[0]-1, current[1]), (current[0]+1, current[1]), (current[0], current[1]-1), (current[0], current[1]+1)]

        # Top
        for dir in directions:
            if dir not in seen and (dir[0] > -1 and dir[0] < xMax) and (dir[1] > -1 and dir[1] < yMax):
                new = ord(world[dir[0]][dir[1]]) 
                if new - curr > -2:
                    queue.append((dir[0],dir[1],current[2]+1))
                    seen.add(dir)
    
    return part1(world,(20,52,0))

def main():
    file = open('day12-input.txt')
    world = []
    for line in file: world.append(list(line.strip()))
    print('Part 1 -', part1(world, (20,0,0)))
    print('Part 2 -', part2(world))                    # Initial Solution
    print('Part 2* -', part2Better(world, (20,52,0)))  # Better Solution

# Start
main()