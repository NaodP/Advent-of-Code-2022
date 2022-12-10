# Naod Philemon
# 12/10/2022

def part1():
    file = open('day10-input.txt')
    X, cycle, sum, check = 1, 0, 0, 20

    for line in file:
        if cycle > 220: break
        line = line.strip()

        cycle += 1
        if cycle % check == 0: 
            sum += cycle * X
            check += 40

        if line != 'noop':
            line = line.split()
            cycle += 1
            if cycle % check == 0: 
                sum += cycle * X
                check += 40
            X += int(line[1])
            
    return sum

def draw(cycle, X):
    if (cycle%40-1) <= X+1 and (cycle%40-1) >= X-1: 
        print('#', end='')
    else: print('.', end='')
    if cycle % 40 == 0: print()

def part2():
    print('Part 2')
    file = open('day10-input.txt')
    X, cycle = 1, 0
    
    for line in file:
        line = line.strip()
        cycle += 1
        draw(cycle, X)

        if line != 'noop':
            line = line.split()
            cycle += 1
            draw(cycle, X)
            X += int(line[1])
            
print('Part 1', part1())
print(part2())