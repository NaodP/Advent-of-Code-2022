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
    val = part1(points)
    maximum = (0,0,0)

    for point in points: maximum = (max(maximum[0],point[0]), max(maximum[1],point[1]), max(maximum[2],point[2]))
    queue = [maximum]
    limit = (maximum[0]+1, maximum[1]+1, maximum[2]+1)
    seen = {limit}
    seenPoints = set()
    for point in points: seenPoints.add(tuple(point))
    
    # Bfs Start From Max
    # Mark each point visited
    while queue:
        current = queue.pop(0)
        seen.add(current)

        # Top (Z)
        newPoint = (current[0], current[1], current[2]+1)
        if newPoint[2] < limit[2] and newPoint not in seenPoints and newPoint not in seen:
            queue.append(newPoint)
            seen.add(newPoint)

        # Bottom (Z)
        newPoint = (current[0], current[1], current[2]-1)
        if newPoint[2] > -1 and newPoint not in seenPoints and newPoint not in seen:
            queue.append(newPoint)
            seen.add(newPoint)

        # Right (X)
        newPoint = (current[0]+1, current[1], current[2])
        if newPoint[0] < limit[0] and newPoint not in seenPoints and newPoint not in seen:
            queue.append(newPoint)
            seen.add(newPoint)

        # Left (X)
        newPoint = (current[0]-1, current[1], current[2])
        if newPoint[0] > -1 and newPoint not in seenPoints and newPoint not in seen:
            queue.append(newPoint)
            seen.add(newPoint)

        # Up (Y)
        newPoint = (current[0], current[1]+1, current[2])
        if newPoint[1] < limit[1] and newPoint not in seenPoints and newPoint not in seen:
            queue.append(newPoint)
            seen.add(newPoint)

        # Down (Y)
        newPoint = (current[0], current[1]-1, current[2])
        if newPoint[1] > -1 and newPoint not in seenPoints and newPoint not in seen:
            queue.append(newPoint)
            seen.add(newPoint)

    # Check each point in the square if its visited or a lava piece
    for i in range(limit[0]):
        for j in range(limit[1]):
            for k in range(limit[2]):
                if (i,j,k) in seen or (i,j,k) in seenPoints:
                    continue

                # If it's not, check if it has a connection with a lava piece and remove 1 from val
                newVal = (i+1,j,k)
                if newVal not in seen and newVal in seenPoints:
                    val -= 1

                newVal = (i-1,j,k)
                if newVal not in seen and newVal in seenPoints:
                    val -= 1

                newVal = (i,j+1,k)
                if newVal not in seen and newVal in seenPoints:
                    val -= 1

                newVal = (i,j-1,k)
                if newVal not in seen and newVal in seenPoints:
                    val -= 1
                
                newVal = (i,j,k+1)
                if newVal not in seen and newVal in seenPoints:
                    val -= 1
                
                newVal = (i,j,k-1)
                if newVal not in seen and newVal in seenPoints:
                    val -= 1
                
    return val

def main():
    file = open('Day 18/day18-input.txt')
    points = []

    for line in file: points.append([int(x) for x in line.strip().split(',')])
    
    # Very Slow / Dirty Code
    print('Part 1 -', part1(points))
    print('Part 2 -', part2(points))

# Start
main()