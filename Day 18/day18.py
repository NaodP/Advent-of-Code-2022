# Naod Philemon
# 12/18/2022

def part1(points):
    total = 0
    for i in range(len(points)):
        sides = 6
        for j in range(len(points)):
            dif = sum([abs(one - two) for (one, two) in zip(points[i],points[j])])
            if dif == 1:
                sides -= 1
        total += sides

    return total
    
def part2(points):
    val = 0
    
    return val

def main():
    file = open('Day 18/day18-input.txt')
    points = []

    for line in file: points.append([int(x) for x in line.strip().split(',')])
    
    print('Part 1 -', part1(points))
    print('Part 2 -', part2(points))

# Start
main()