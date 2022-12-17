# Naod Philemon
# 12/16/2022

import sys
sys.setrecursionlimit(5000)

possible = 0


def dfs(valves, valve, timeLeft, pressure, opened):
    # Base Case
    if len(opened) == possible: timeLeft = 0
    if timeLeft <= 0: return pressure
    
    maxPressure = pressure
    newOpened = opened.copy()

    # Open The Valve
    if valves[valve]['flow'] != 0 and valve not in newOpened:
        newOpened.add(valve)
        timeLeft -= 1 
        newPressure = pressure + valves[valve]['flow'] * timeLeft
        maxPressure = newPressure
        if timeLeft == 0: return maxPressure

        for connection in valves[valve]['connections']:
            maxPressure = max(dfs(valves, connection, timeLeft-1, newPressure, newOpened), maxPressure)

    # Don't Open The Valve
    for connection in valves[valve]['connections']:
        maxPressure = max(dfs(valves, connection, timeLeft-1, pressure, newOpened), maxPressure)

    return maxPressure


def part1(valves):
    return dfs(valves, 'AA', 30, 0, set())

def part2():
    pass

def main():
    file = open('Day 16/day16-input.txt')
    valves = {}
    global possible

    for line in file:
        line = line.strip().split(';')
        left = line[0].split(' '); right = line[1].split('valves')

        connections = right[1].split(', '); connections[0] = connections[0][1:]
        valve = left[1]
        flow = int(left[-1][5:])

        if flow != 0: possible += 1
        
        valves[valve] = {
            'flow': flow, 
            'connections': connections
        }

    print('Part 1 -', part1(valves)) # NOT SOLVED YET
    print('Part 2 -', part2())       # NOT SOLVED YET

# Start
main()