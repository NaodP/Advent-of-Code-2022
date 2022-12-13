# Naod Philemon
# 12/13/2022

def compare(first, second):
    # If both int
    if type(first) == int and type(second) == int:
        if first < second: return True
        if first > second: return False

    # If both list
    if type(first) == list and type(second) == list:
        for x, y in zip(first, second):
            compared = compare(x, y)
            if compared == True: return True
            elif compared == False: return False
        if len(first) < len(second): return True
        if len(first) > len(second): return False
    
    # If one int other list
    if type(first) == int and type(second) == list:
        return compare([first],second)
    if type(first) == list and type(second) == int:
        return compare(first,[second])

    return

def part1(pairs):
    sum, i = 0, 1
    for pair in pairs:
        if compare(pair[0],pair[1]):
            sum += i
        i += 1
    
    return sum


def part2():
    pass

def main():
    file = open('day13-input.txt')
    pairs = []
    for _ in range(150):
        first = eval(file.readline().strip())
        second = eval(file.readline().strip())
        pairs.append((first,second))
        file.readline()

    print('Part 1 -', part1(pairs))
    print('Part 2 -', part2())

# Start
main()