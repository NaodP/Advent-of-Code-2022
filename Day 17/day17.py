# Naod Philemon
# 12/17/2022

def getRock(index, maxY):
    if index == 0: return [[3,maxY+4],[4,maxY+4],[5,maxY+4],[6,maxY+4]]
    if index == 1: return [[3,maxY+5],[4,maxY+5],[5,maxY+5],[4,maxY+6],[4,maxY+4]]
    if index == 2: return [[3,maxY+4],[4,maxY+4],[5,maxY+4],[5,maxY+5],[5,maxY+6]]
    if index == 3: return [[3,maxY+4],[3,maxY+5],[3,maxY+6],[3,maxY+7]]
    if index == 4: return [[3,maxY+4],[4,maxY+4],[3,maxY+5],[4,maxY+5]]

def part1(directions):
    solid = set()
    maxY, index, length = 0, 0, len(directions)

    for i in range(2022):
        currentRock = getRock(i % 5, maxY)
        
        while True:
            index %= length
            dir = 1 if directions[index] == '>' else -1
            index += 1

            # Move L/R
            safe = True
            for point in currentRock:
                if point[0] + dir < 1 or point[0] + dir > 7 or (point[0] + dir, point[1]) in solid:
                    safe = False
                    break

            if safe:
                for point in currentRock: point[0] += dir

            # Move Down
            safe = True
            for point in currentRock:
                if point[1] - 1 < 1 or (point[0], point[1]-1) in solid:
                    safe = False
                    break
            
            if not safe:
                for point in currentRock:
                    solid.add((point[0], point[1]))
                    maxY = max(maxY, point[1])
                break
                
            # Actually Move It Down
            for point in currentRock: point[1] -= 1 

    return maxY

def part2(directions):
    pass

def main():
    file = open('Day 17/day17-input.txt')
    
    for line in file:
        directions = line

    print('Part 1 -', part1(directions))
    print('Part 2 -', part2(directions))

# Start
main()