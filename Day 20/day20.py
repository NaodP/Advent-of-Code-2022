# Naod Philemon
# 12/20/2022

def part1(original):
    length = len(original)
    variable = original.copy()
    positions = [x for x in range(length)]
    
    for i in range(length):
        index = 0
        current = original[i]

        # Find Current Position
        for j, var in enumerate(variable):
            if var == current and positions[j] == i:
                index = j
                break
        
        # Find New Position
        move = (index + original[i]) % length

        # Move It
        variable.pop(index)    
        positions.pop(index)
        
        if index + original[i] < 0: 
            dif = int((index + original[i]) / length)
            variable.insert(move-dif, current)
            positions.insert(move-dif, i)
        else: 
            dif = int((index + original[i]) / length)
            variable.insert(move+dif, current)
            positions.insert(move+dif, i)
        
        
    # Find 0
    for j, var in enumerate(variable):
        if var == 0:
            index = j
            break

    # Sum Values
    val = variable[(1000+index)%length] + variable[(2000+index)%length] + variable[(3000+index)%length]

    return val # Wrong Answer

def part2():
    pass

def main():
    file = open('Day 20/day20-input.txt')
    coordinates = []

    for line in file: coordinates.append(int(line))
        
    print('Part 1 -', part1(coordinates))
    print('Part 2 -', part2())

# Start
main()