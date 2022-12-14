# Naod Philemon
# 12/06/2022

def part1():
  file = open('day06-input.txt')
  for line in file:
    i = 3
    queue = [line[0], line[1], line[2]]
    while i < len(line):
      if line[i] not in queue:
        seen = set()
        good = True
        for let in queue:
          if let not in seen: seen.add(let)
          else: good = False
        if good:
          return i + 1
      queue.pop(0)
      queue.append(line[i])

      i += 1

  return -1

def part2():
  file = open('day06-input.txt')
  for line in file:
    i = 13
    queue = [x for x in line[0:13]]
    
    while i < len(line):
      if line[i] not in queue:
        seen = set()
        good = True
        for let in queue:
          if let not in seen: seen.add(let)
          else: 
            good = False
            break
        if good:
          print(queue)
          return i + 1
      queue.pop(0)
      queue.append(line[i])
      
      i += 1
    
  return -1
  
print('Part 1', part1())
print('Part 2', part2())