# Naod Philemon
# 12/20/2022

class LinkedList:
    def __init__(self, val):
        self.prev = None
        self.val = val
        self.next = None

def getAllPoints(original):
    allPoints = []
    prev = LinkedList(0)
    first = last = None

    for i, val in enumerate(original):
        current = LinkedList(val)
        current.prev = prev
        prev.next = current
        prev = current

        if i == 0: first = current
        if i == len(original)-1: last = current
        allPoints.append(prev)
    
    first.prev = last
    last.next = first

    return allPoints

def calculate(allPoints, original, mixNum):
    for _ in range(mixNum):
        for point in allPoints:
            # Find The 0
            if point.val == 0:
                start = point
                continue

            move = point.val
            
            if move < 0:
                move = -(abs(move) % (len(original) - 1))
                while move != 0:
                    point.next.prev = point.prev
                    point.prev.next = point.next

                    point.prev = point.prev.prev
                    point.next.prev.prev = point
                    point.next = point.next.prev
                    point.prev.next = point

                    move += 1
            
            elif move > 0:
                move = move % (len(original) - 1)
                while move != 0:
                    point.next.prev = point.prev
                    point.prev.next = point.next

                    point.next = point.next.next
                    point.prev.next.next = point
                    point.prev = point.prev.next
                    point.next.prev = point

                    move -= 1

    finalValue = 0

    for i in range(3001):
        if i % 1000 == 0: finalValue += start.val
        start = start.next
    
    return finalValue

def part1(original):
    allPoints = getAllPoints(original)

    return calculate(allPoints, original, 1)

def part2(original):
    original = [x * 811589153 for x in original]

    allPoints = getAllPoints(original)
    
    return calculate(allPoints, original, 10)

def main():
    file = open('Day 20/day20-input.txt')
    coordinates = []

    for line in file: coordinates.append(int(line))
        
    print('Part 1 -', part1(coordinates)) # Takes Just Under A Min (50 secs)
    print('Part 2 -', part2(coordinates)) # Takes 10 times as long 😭

# Start
main()