# Naod Philemon
# 12/25/2022

def toDecimal(num):
    SNAFU, val = 1, 0
    for i in range(len(num)-1, -1, -1):
        if num[i] == '2': val += 2 * SNAFU
        if num[i] == '1': val += 1 * SNAFU
        if num[i] == '0': val += 0
        if num[i] == '-': val += -1 * SNAFU
        if num[i] == '=': val += -2 * SNAFU
        SNAFU *= 5
    return val

def toSNAFU(num):
    SNAFU = ['=','-','0','1','2']
    val = ''
    while num > 0:
        i = (num + 2) % 5
        num = (num + 2) // 5
        val += SNAFU[i]

    return val[::-1]

def part1(numbers):
    val = 0
    for num in numbers: val += toDecimal(num)
    return toSNAFU(val)

def main():
    file = open('Day 25/day25-input.txt')
    numbers = []

    for line in file: 
        numbers.append(line.strip())

    print('Part 1 -', part1(numbers))

# Start
main()