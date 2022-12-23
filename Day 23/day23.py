# Naod Philemon
# 12/23/2022

def pic(positions):
    for i in range(-2, 9):
        for j in range(-2, 10):
            if((i, j) in positions):
                print('#', end='')
            else:
                print('.', end='')
        print()
    print()

def part1(world):
    currentPositions = []
    
    y = 0
    for row in world:
        for x, pos in enumerate(row):
            if pos == '#':
                currentPositions.append((y,x))
        y+=1

    for round in range(10):
        currentPositionsSet = set(currentPositions)
        proposedPositions = []

        def north(pos):
            if (pos[0]-1, pos[1]) not in currentPositionsSet and (pos[0]-1, pos[1]+1) not in currentPositionsSet and (pos[0]-1, pos[1]-1) not in currentPositionsSet:
                proposedPositions.append((pos[0]-1, pos[1]))
                return True
            return False

        def south(pos):
            if (pos[0]+1, pos[1]) not in currentPositionsSet and (pos[0]+1, pos[1]+1) not in currentPositionsSet and (pos[0]+1, pos[1]-1) not in currentPositionsSet:
                proposedPositions.append((pos[0]+1, pos[1]))
                return True
            return False

        def west(pos):
            if (pos[0], pos[1]-1) not in currentPositionsSet and (pos[0]+1, pos[1]-1) not in currentPositionsSet and (pos[0]-1, pos[1]-1) not in currentPositionsSet:
                proposedPositions.append((pos[0], pos[1]-1))
                return True
            return False

        def east(pos):
            if (pos[0], pos[1]+1) not in currentPositionsSet and (pos[0]+1, pos[1]+1) not in currentPositionsSet and (pos[0]-1, pos[1]+1) not in currentPositionsSet:
                proposedPositions.append((pos[0], pos[1]+1))
                return True
            return False
            

        # Propose
        for pos in currentPositions:
            # If no one nearby
            safe = True
            for i in range(-1,2):
                for j in range(-1, 2):
                    if i == 0 == j: continue
                    if (pos[0]+i, pos[1]+j) in currentPositionsSet:
                        safe = False
            if safe: 
                proposedPositions.append((pos[0], pos[1]))
                continue

            # North, South, West, East
            if round % 4 == 0:
                if north(pos): continue
                if south(pos): continue
                if west(pos): continue
                if east(pos): continue
                proposedPositions.append((pos[0], pos[1]))
            # South, West, East, North
            elif round % 4 == 1:
                if south(pos): continue
                if west(pos): continue
                if east(pos): continue
                if north(pos): continue
                proposedPositions.append((pos[0], pos[1]))
            # West, East, North, South
            elif round % 4 == 2:
                if west(pos): continue
                if east(pos): continue
                if north(pos): continue
                if south(pos): continue
                proposedPositions.append((pos[0], pos[1]))
            # East, North, South, West
            elif round % 4 == 3:
                if east(pos): continue
                if north(pos): continue
                if south(pos): continue
                if west(pos): continue
                proposedPositions.append((pos[0], pos[1]))
            
        # Move
        length = len(proposedPositions)
        for i in range(length):
            for j in range(i+1, length):
                if proposedPositions[i] == proposedPositions[j]:
                    proposedPositions[i] = currentPositions[i]
                    proposedPositions[j] = currentPositions[j]

        currentPositions = proposedPositions.copy()
        # pic(currentPositions)

    # Find Result
    Xmax = Ymax = -10000
    Xmin = Ymin = 10000
    for pos in currentPositions:
        Xmax = max(Xmax, pos[1])
        Ymax = max(Ymax, pos[0])
        Xmin = min(Xmin, pos[1])
        Ymin = min(Ymin, pos[0])
    
    empty = ((Xmax-Xmin+1) * (Ymax-Ymin+1)) - len(currentPositions)
    return empty

def part2(world):
    currentPositions = []
    
    y = 0
    for row in world:
        for x, pos in enumerate(row):
            if pos == '#':
                currentPositions.append((y,x))
        y+=1

    for round in range(2000):
        numSafe = 0
        currentPositionsSet = set(currentPositions)
        proposedPositions = []

        def north(pos):
            if (pos[0]-1, pos[1]) not in currentPositionsSet and (pos[0]-1, pos[1]+1) not in currentPositionsSet and (pos[0]-1, pos[1]-1) not in currentPositionsSet:
                proposedPositions.append((pos[0]-1, pos[1]))
                return True
            return False

        def south(pos):
            if (pos[0]+1, pos[1]) not in currentPositionsSet and (pos[0]+1, pos[1]+1) not in currentPositionsSet and (pos[0]+1, pos[1]-1) not in currentPositionsSet:
                proposedPositions.append((pos[0]+1, pos[1]))
                return True
            return False

        def west(pos):
            if (pos[0], pos[1]-1) not in currentPositionsSet and (pos[0]+1, pos[1]-1) not in currentPositionsSet and (pos[0]-1, pos[1]-1) not in currentPositionsSet:
                proposedPositions.append((pos[0], pos[1]-1))
                return True
            return False

        def east(pos):
            if (pos[0], pos[1]+1) not in currentPositionsSet and (pos[0]+1, pos[1]+1) not in currentPositionsSet and (pos[0]-1, pos[1]+1) not in currentPositionsSet:
                proposedPositions.append((pos[0], pos[1]+1))
                return True
            return False
            

        # Propose
        for pos in currentPositions:
            # If no one nearby
            safe = True
            for i in range(-1,2):
                for j in range(-1, 2):
                    if i == 0 == j: continue
                    if (pos[0]+i, pos[1]+j) in currentPositionsSet:
                        safe = False
            if safe: 
                numSafe += 1
                proposedPositions.append((pos[0], pos[1]))
                continue

            # North, South, West, East
            if round % 4 == 0:
                if north(pos): continue
                if south(pos): continue
                if west(pos): continue
                if east(pos): continue
                proposedPositions.append((pos[0], pos[1]))
            # South, West, East, North
            elif round % 4 == 1:
                if south(pos): continue
                if west(pos): continue
                if east(pos): continue
                if north(pos): continue
                proposedPositions.append((pos[0], pos[1]))
            # West, East, North, South
            elif round % 4 == 2:
                if west(pos): continue
                if east(pos): continue
                if north(pos): continue
                if south(pos): continue
                proposedPositions.append((pos[0], pos[1]))
            # East, North, South, West
            elif round % 4 == 3:
                if east(pos): continue
                if north(pos): continue
                if south(pos): continue
                if west(pos): continue
                proposedPositions.append((pos[0], pos[1]))
            
        # Move
        length = len(proposedPositions)
        for i in range(length):
            for j in range(i+1, length):
                if proposedPositions[i] == proposedPositions[j]:
                    proposedPositions[i] = currentPositions[i]
                    proposedPositions[j] = currentPositions[j]

        currentPositions = proposedPositions.copy()

        # If no one moved
        if numSafe == len(currentPositions):
            return round+1

    return -1

def main():
    file = open('Day 23/day23-input.txt')
    world = []

    for line in file: world.append(line)
    print('Part 1 -', part1(world))
    print('Part 2 -', part2(world)) # Both Are Very Slow, try to optimize

# Start
main()