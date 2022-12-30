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
    def dfs(valve1, valve2, seen, ogMinFirst, ogMinSecond, maxPres):
        # Base Case
        if ogMinFirst <= 0 and ogMinSecond <= 0: return maxPres
        if len(seen) == len(valid): return maxPres

        ogPres = maxPres

        # If Neither Of Us Are Finished
        if ogMinFirst > 0 and ogMinSecond > 0:
            for conn1 in valves[valve1]:
                for conn2 in valves[valve2]:
                    if conn1 == conn2: continue
                    if conn1 in seen and conn2 in seen: continue
                    first = conn1; second = conn2
                    newSeen = seen.copy()
                    minFirst = ogMinFirst - (valves[valve1][conn1]) - 1
                    minSecond = ogMinSecond - (valves[valve2][conn2]) - 1
                    newPres = ogPres
                    if minFirst > 0 and conn1 not in seen: 
                        newPres += (oldValves[conn1][0] * minFirst)
                        newSeen.add(conn1)
                    else: first = valve1
                    if minSecond > 0 and conn2 not in seen: 
                        newPres += (oldValves[conn2][0] * minSecond)
                        newSeen.add(conn2)
                    else: second = valve2
                    maxPres = max(maxPres, dfs(first, second, newSeen, minFirst, minSecond, newPres))

        # If Elephant Is Finished But I'm Not
        elif ogMinFirst > 0:
            for conn in valves[valve1]:
                if conn not in seen:
                    newSeen = seen.copy(); newSeen.add(conn)
                    minFirst = ogMinFirst - (valves[valve1][conn]) - 1
                    newPres = (oldValves[conn][0] * minFirst) + ogPres
                    maxPres = max(maxPres, dfs(conn, valve2, newSeen, minFirst, ogMinSecond, newPres))

        # If I'm Finished But Elephant Isn't
        elif ogMinSecond > 0:
            for conn in valves[valve2]:
                if conn not in seen:
                    newSeen = seen.copy(); newSeen.add(conn)
                    minSecond = ogMinSecond - (valves[valve2][conn]) - 1
                    newPres = (oldValves[conn][0] * minSecond) + ogPres
                    maxPres = max(maxPres, dfs(valve1, conn, newSeen, ogMinFirst, minSecond, newPres))
     
        return maxPres

    valves = setup(oldValves, valid)
    pressure = 0
    startingConnections = [x for x in valves['AA']]

    for i in range(len(startingConnections)):
        for j in range(i+1, len(startingConnections)):
            minFirst = 26 - (valves['AA'][startingConnections[i]]) - 1
            minSecond = 26 - (valves['AA'][startingConnections[j]]) - 1
            newPressure = (oldValves[startingConnections[i]][0] * minFirst) + (oldValves[startingConnections[j]][0] * minFirst)
            pressure = max(pressure, dfs(startingConnections[i], startingConnections[j], {'AA', startingConnections[i], startingConnections[j]}, minFirst, minSecond, maxPres=newPressure))

    return pressure

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