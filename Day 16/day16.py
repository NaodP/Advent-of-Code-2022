# Naod Philemon
# 12/16/2022

# Find All Non-Zero Valve Connections
def setup(valves, valid):
    newValves = {}
    
    for valve in valid:
        queue = [(valve,0)]
        seen = {valve}
        finalDistance = {}

        while queue:
            current, dist = queue.pop(0)
            
            for connection in valves[current][1]:
                if connection not in seen:
                    seen.add(connection)
                    queue.append((connection, dist+1))
                    if connection == 'AA' or valves[connection][0] > 0:
                        finalDistance[connection] = dist+1

        newValves[valve] = finalDistance

    return newValves

def part1(oldValves, valid):
    def dfs(valve, seen, minutes, maxPres):
        # Base Case
        if minutes <= 0: return maxPres
        if len(seen) == len(valid): return maxPres

        seenHere = seen.copy()
        seenHere.add(valve)
        ogPres = maxPres
        for connection in valves[valve]:
            if connection in seenHere: continue
            newMins = (minutes-(valves[valve][connection])-1)
            possible = oldValves[connection][0] * newMins

            maxPres = max(maxPres, dfs(connection, seenHere, newMins, ogPres+possible))

        return maxPres

    valves = setup(oldValves, valid)
    pressure = dfs('AA', set(), minutes=30, maxPres=0)
    
    return pressure

def part2(oldValves, valid):
    pass

def main():
    file = open('Day 16/day16-input.txt')
    valves = {}
    valid = ['AA']

    for line in file:
        line = line.strip().split(';')
        left = line[0].split(' '); right = line[1].split('valves')

        connections = right[1].split(', '); connections[0] = connections[0][1:]
        valve = left[1]
        flow = int(left[-1][5:])

        if flow > 0: valid.append(valve)

        valves[valve] = (flow, connections)

    print('Part 1 -', part1(valves, valid)) # 1728 (No Idea What I Did lol)
    print('Part 2 -', part2(valves, valid)) # NOT SOLVED YET

# Start
main()