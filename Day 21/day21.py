# Naod Philemon
# 12/21/2022

def part1(numMonkeys, opMonkeys):
    def find(monkey):
        if monkey in numMonkeys: return numMonkeys[monkey]

        one = find(opMonkeys[monkey][0])
        op = opMonkeys[monkey][1]
        two = find(opMonkeys[monkey][2])

        if op == '+': return one + two
        if op == '-': return one - two
        if op == '/': return one / two
        if op == '*': return one * two

    return int(find('root'))

def part2(numMonkeys, opMonkeys):
    def find(monkey):
        if monkey == 'humn': return 'x'
        if monkey in numMonkeys: return numMonkeys[monkey]

        one = find(opMonkeys[monkey][0])
        op = '=' if monkey == 'root' else opMonkeys[monkey][1]
        two = find(opMonkeys[monkey][2])

        return f'({one} {op} {two})'

    return find('root') 

def main():
    file = open('Day 21/day21-input.txt')
    numMonkeys = {}
    opMonkeys = {}

    for line in file:
        monkey, job = line.strip().split(': ')
        try: numMonkeys[monkey] = int(job)
        except: opMonkeys[monkey] = job.split(' ')

    print('Part 1 -', part1(numMonkeys, opMonkeys))
    print('Part 2 -', part2(numMonkeys, opMonkeys))
    # I Put The Returned Formula Into https://www.mathpapa.com/algebra-calculator.html
    # I Think You Could Also Solve With SymPy

# Start
main()