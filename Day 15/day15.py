# Naod Philemon
# 12/15/2022

def part1(points):
    count = 0
    
    for i in range(int(-1e7), int(+1e7)):
        y = 2000000 
        for x1, y1, x2, y2, manhB in points:
            # If Is Beacon, Don't count it
            if x2 == i and y2 == y: break

            # If Current Point Is Under Any Sensor "Umbrella"
            manh = abs(i-x1) + abs(y-y1)
            if manh <= manhB:
                count += 1
                break

    return count

def part2():
    pass

def main():
    file = open('Day 15/day15-input.txt')
    points = []
    
    for line in file:
        line = line.split(' ')
        x1, y1, x2, y2 = int(line[2][2:-1]), int(line[3][2:-1]), int(line[-2][2:-1]), int(line[-1][2:-1])
        manhattan = abs(x1-x2) + abs(y1-y2)
        points.append((x1, y1, x2, y2, manhattan))
        
    print('Part 1 -', part1(points)) # Takes wayyyy too long - need to optimize
    print('Part 2 -', part2())

# Start
main()