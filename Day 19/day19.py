# Naod Philemon
# 12/19/2022

import copy

def part1(blueprints):
    qualityLevels = 0
    for i, blueprint in enumerate(blueprints):
        currentQueue = [([0,0,0,0], [1,0,0,0])]
        for _ in range(24):
            newQueue = []
            newQueueSet = set()
            for Materials, Robots in currentQueue:
                check = []

                # Get New Mats
                newMats = copy.deepcopy(Materials)
                newMats[0] += Robots[0]
                newMats[1] += Robots[1]
                newMats[2] += Robots[2]
                newMats[3] += Robots[3]

                # Buy New Machines From Old Mats 
                # Geode
                if (Materials[0] >= blueprint[3][0] and Materials[2] >= blueprint[3][1]):
                    mats = [newMats[0]-blueprint[3][0], newMats[1], newMats[2]-blueprint[3][1], newMats[3]]
                    bots = [Robots[0], Robots[1], Robots[2], Robots[3]+1]
                    check.append((mats,bots))
                else:
                    # Obsidian
                    if ((Materials[0] >= blueprint[2][0] and Materials[1] >= blueprint[2][1]) and (Materials[0]-Robots[0]) < blueprint[2][0]) or ((Materials[0] >= blueprint[2][0] and Materials[1] >= blueprint[2][1]) and (Materials[1]-Robots[1]) < blueprint[2][1]):
                        mats = [newMats[0]-blueprint[2][0], newMats[1]-blueprint[2][1], newMats[2], newMats[3]]
                        bots = [Robots[0], Robots[1], Robots[2]+1, Robots[3]]
                        check.append((mats,bots))

                    # Clay
                    if (Materials[0] >= blueprint[1]) and ((Materials[0]-Robots[0]) < blueprint[1]):
                        mats = [newMats[0]-blueprint[1], newMats[1], newMats[2], newMats[3]]
                        bots = [Robots[0], Robots[1]+1, Robots[2], Robots[3]]
                        check.append((mats,bots))

                    # Ore
                    if (Materials[0] >= blueprint[0]) and ((Materials[0]-Robots[0]) < blueprint[0]): 
                        mats = [newMats[0]-blueprint[0], newMats[1], newMats[2], newMats[3]]
                        bots = [Robots[0]+1, Robots[1], Robots[2], Robots[3]]
                        check.append((mats,bots))
                
                    # No New Machine
                    check.append((newMats, Robots))

                # Check All Possible Moves
                for mat, bot in check:
                    if (tuple(mat), tuple(bot)) not in newQueueSet: 
                        newQueue.append((mat, bot))
                        newQueueSet.add((tuple(mat), tuple(bot)))

            # Update Current Queue
            currentQueue = copy.deepcopy(newQueue)
                    
        # Find Max Geode
        geodes = 0
        for mats, bots in currentQueue:
            geodes = max(geodes, mats[-1])

        qualityLevels += (geodes * (i+1))

    return qualityLevels

def part2():
    pass

def main():
    file = open('Day 19/day19-input.txt')
    blueprints = []

    for line in file:
        line = line.strip().split(' ')
        blueprints.append([int(line[6]), int(line[12]), (int(line[18]), int(line[21])), (int(line[27]), int(line[30]))])

    print('Part 1 -', part1(blueprints)) # 1262 (Just under 2 mins)
    print('Part 2 -', part2())

# Start
main()