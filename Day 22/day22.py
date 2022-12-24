# Naod Philemon
# 12/22/2022

def part1(world, path):
    # Find leftmost open tile of the top row of tiles
    x = 0
    for i, val in enumerate(world[0]):
        if val != ' ':
            x = i
            break
    current = (x, 0)
    facing = 0

    for move in path:
        try: 
            move = int(move)
            for _ in range(move):

                # Moving Right
                if facing == 0:
                    # print('Right')
                    # Wrap Around
                    if current[0] + 1 > len(world[current[1]])-1 or world[current[1]][current[0]+1] == ' ':
                        # print('Wrap')
                        # Get New Point
                        index = 0
                        for i, x in enumerate(world[current[1]]):
                            if x != ' ':
                                index = i
                                break
                        
                        # If Not Wall 
                        if world[current[1]][index] != '#':
                            current = (index, current[1])
                        
                    # If Run Into Wall (normally)
                    elif world[current[1]][current[0]+1] == '#': 
                        # print('Wall')
                        break
                    else:
                        # print('Move')
                        current = (current[0]+1, current[1])

                # Moving Left
                if facing == 2:
                    # print('Left')
                    # Wrap Around
                    if current[0] - 1 < 0 or world[current[1]][current[0]-1] == ' ':
                        # print('Wrap')
                        # Get New Point
                        index = 0
                        for i in range(len(world[current[1]])-1, -1, -1):
                            x = world[current[1]][i]
                            if x != ' ':
                                index = i
                                break
                        
                        # If Not Wall 
                        if world[current[1]][index] != '#':
                            current = (index, current[1])
                        
                    # If Run Into Wall (normally)
                    elif world[current[1]][current[0]-1] == '#':
                        # print('Wall')
                        break
                    else: 
                        # print('Move')
                        current = (current[0]-1, current[1])

                # Moving Down
                if facing == 1:
                    # print('Down')
                    # Wrap Around
                    # Get Y Lim Point
                    Y_Down = 0
                    for i in range(len(world)-1, -1, -1):
                        if len(world[i]) <= current[0]: continue
                        x = world[i][current[0]]
                        Y_Down = i
                        break

                    if current[1] + 1 > Y_Down or world[current[1]+1][current[0]] == ' ':
                        # print('Wrap')
                        # Get New Point
                        index = 0
                        for i in range(len(world)):
                            x = world[i][current[0]]
                            if x != ' ':
                                index = i
                                break
                        
                        # If Not Wall 
                        if world[index][current[0]] != '#':
                            current = (current[0], index)

                    # Run Into Wall
                    elif world[current[1]+1][current[0]] == '#': 
                        # print('Wall')
                        break
                    else: 
                        # print('Move')
                        current = (current[0], current[1]+1)

                # Moving Up
                if facing == 3:
                    # print('Up')
                    # Wrap Around
                    # Get Y Lim Point
                    Y_Up = 0
                    for i in range(len(world)):
                        if len(world[i]) < current[0]: continue
                        x = world[i][current[0]]
                        if x != ' ':
                            Y_Up = i
                            break

                    if current[1] - 1 < Y_Up or world[current[1]-1][current[0]] == ' ':
                        # print('Wrap')
                        # Get New Point
                        index = 0
                        for i in range(len(world)-1, -1, -1):
                            if len(world[i]) <= current[0]: continue
                            x = world[i][current[0]]
                            if x != ' ':
                                index = i
                                break
                        
                        # If Not Wall 
                        if world[index][current[0]] != '#':
                            current = (current[0], index)

                    # Run Into Wall
                    elif world[current[1]-1][current[0]] == '#': 
                        # print('Wall')
                        break
                    else: 
                        # print('Move')
                        current = (current[0], current[1]-1)

        except:
            if move == 'R': facing = (facing + 1) % 4
            if move == 'L': facing = (facing - 1) % 4

        # print(current)
        
    # return current
    return ((current[1]+1) * 1000) + ((current[0]+1) * 4) + facing

def part2():
    pass

def main():
    worldF = open('Day 22/day22-input-map.txt')
    path = open('Day 22/day22-input-path.txt', 'r').read()
    i = 0

    while i < len(path):
        if path[i] == 'R' or path[i] == 'L':
            path = path[:i] + ' ' + path[i] + ' ' + path[i+1:]
            i += 1
        i += 1
    path = path.split(' ')

    world = []
    for line in worldF:
        line = list(line.strip('\n'))
        world.append(line)
    
    print('Part 1 -', part1(world, path))
    print('Part 2 -', part2()) # I'm too lazy to do this lol

# Start
main()