# Naod Philemon
# 12/15/2022

def part1(points):
    count = 0
    
    for i in range(int(-1e7), int(+1e7)):
        y = 2000000 
        for x1, y1, manhB in points:
            # If Current Point Is Under Any Sensor "Umbrella"
            manh = abs(i-x1) + abs(y-y1)
            if manh <= manhB:
                count += 1
                break

    return count

def safe(points, point):
    if point[0] < 0 or point[0] > 4000000 or point[1] < 0 or point[1] > 4000000:
        return False

    # Check if current point can be seen by another sensor
    for x1, y1, manH in points:
        manB = abs(x1-point[0]) + abs(y1-point[1])
        if manH >= manB:
            return False

    return True

def part2(points):
    for x1, y1, manH in points:
        
        start = y1 - manH - 1
        end = x1 + manH + 1

        x = 0

        for i in range(start,end+1):
            left, right = (x1+x, i), (x1-x, i)

            if safe(points, left): return (left[0]*4000000)+left[1]
            if safe(points, right): return (right[0]*4000000)+right[1]

            if i < y1: x+=1 
            else: x-=1

    return None
        
def main():
    file = open('Day 15/day15-input.txt')
    points = []
    
    for line in file:
        line = line.split(' ')
        x1, y1, x2, y2 = int(line[2][2:-1]), int(line[3][2:-1]), int(line[-2][2:-1]), int(line[-1][2:-1])
        manhattan = abs(x1-x2) + abs(y1-y2)
        points.append((x1, y1, manhattan))
        
    print('Part 1 -', part1(points)) # Takes 2.41 Minutes
    print('Part 2 -', part2(points)) # Takes 3.05 Minutes

# Start
main()