# Naod Philemon
# 12/11/2022

class Monkey():
    def __init__(self, active, items, op, val, test, T, F) -> None:
        self.active = int(active)
        self.items = items
        self.op = op
        self.val = val
        self.test = int(test)
        self.T = int(T)
        self.F = int(F)

def part1():
    file = open('day11-input.txt')
    monkeys = []
    top, top2 = 0, 0
    
    for i in range(8):
        items = [int(x) for x in file.readline().split(' ')]
        op, val = file.readline().strip().split(' ')
        test = file.readline().strip()
        T = file.readline().strip()
        F = file.readline().strip()
        monkeys.append(Monkey(0, items, op, val, test, T, F))

    for i in range(20):
        for j in range(8):
            while monkeys[j].items:
                current = int(monkeys[j].items.pop(0))
                if monkeys[j].op == '+': 
                    if monkeys[j].val == 'old': current += current
                    else: current += int(monkeys[j].val)
                elif monkeys[j].op == '*':
                    if monkeys[j].val == 'old': current *= current
                    else: current *= int(monkeys[j].val)
                current = int(current/3) # Part 1
                if current % int(monkeys[j].test) == 0: monkeys[int(monkeys[j].T)].items.append(current)
                else: monkeys[int(monkeys[j].F)].items.append(current)
                monkeys[j].active += 1
    for monkey in monkeys:
        if monkey.active > top:
            top2 = top
            top = monkey.active
        elif monkey.active > top2:
            top2 = monkey.active

    return top * top2

def part2():
    file = open('day11-input.txt')
    monkeys = []
    superMod = 1
    top, top2 = 0, 0
    
    for i in range(8):
        items = [int(x) for x in file.readline().split(' ')]
        op, val = file.readline().strip().split(' ')
        test = file.readline().strip()
        T = file.readline().strip()
        F = file.readline().strip()
        monkeys.append(Monkey(0, items, op, val, test, T, F))
        superMod *= int(test)

    for i in range(10000):
        for j in range(8):
            while monkeys[j].items:
                current = int(monkeys[j].items.pop(0))
                if monkeys[j].op == '+': 
                    if monkeys[j].val == 'old': current += current
                    else: current += int(monkeys[j].val)
                elif monkeys[j].op == '*':
                    if monkeys[j].val == 'old': current *= current
                    else: current *= int(monkeys[j].val)
                current = current % superMod # Part 2
                if current % int(monkeys[j].test) == 0: monkeys[int(monkeys[j].T)].items.append(current)
                else: monkeys[int(monkeys[j].F)].items.append(current)
                monkeys[j].active += 1

    for monkey in monkeys:
        if monkey.active > top:
            top2 = top
            top = monkey.active
        elif monkey.active > top2:
            top2 = monkey.active
    
    return top * top2

print('Part 1 -', part1())
print('Part 2 -', part2())