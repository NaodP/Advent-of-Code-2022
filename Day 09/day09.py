# Naod Philemon
# 12/09/2022

import os
import time

def plot(rope):
  positions = {}
  for i,pos in enumerate(rope):
    temp = (pos[0], pos[1])
    positions[temp] = i
  for i in range(-25,25):
    for j in range(-25,25):
      if ((i,j)) not in rope:
        print('.', end=' ')
      else:
        print(positions[(i,j)], end=' ')
    print('')
    
def part1():
    file = open('day09-input.txt')
    H = (0, 0)
    T = (0, 0)
    T_Has_Been = set()
    T_Has_Been.add((0, 0))
    order = []

    for line in file:
      line = line.strip().split()
      for i in range(int(line[1])):
          order.append(line[0])

    for dir in order:
        if dir == 'U':
            H = (H[0], H[1] + 1)
        if dir == 'D':
            H = (H[0], H[1] - 1)
        if dir == 'L':
            H = (H[0] - 1, H[1])
        if dir == 'R':
            H = (H[0] + 1, H[1])

        # DIRECT
        # Right by 2
        if (H[0] - T[0] == 2 and H[1] - T[1] == 0):
            T = (H[0] - 1, T[1])
        # Left by 2
        if (T[0] - H[0] == 2 and H[1] - T[1] == 0):
            T = (H[0] + 1, T[1])
        # Up by 2
        if (H[1] - T[1] == 2 and H[0] - T[0] == 0):
            T = (T[0], H[1] - 1)
        # Down by 2
        if (T[1] - H[1] == 2 and H[0] - T[0] == 0):
            T = (T[0], H[1] + 1)

        # HORSE
        # Up 2 Right 1
        if (H[0] - T[0] == 1 and H[1] - T[1] == 2):
            T = (H[0], H[1] - 1)
        # Up 2 Left 1
        if (T[0] - H[0] == 1 and H[1] - T[1] == 2):
            T = (H[0], H[1] - 1)
        # Down 2 Right 1
        if (H[0] - T[0] == 1 and T[1] - H[1] == 2):
            T = (H[0], H[1] + 1)
        # Down 2 Left 1
        if (T[0] - H[0] == 1 and T[1] - H[1] == 2):
            T = (H[0], H[1] + 1)

        # Right 2 Up 1
        if (H[0] - T[0] == 2 and H[1] - T[1] == 1):
            T = (H[0] - 1, H[1])
        # Left 2 Up 1
        if (T[0] - H[0] == 2 and H[1] - T[1] == 1):
            T = (H[0] + 1, H[1])
        # Right 2 Down 1
        if (H[0] - T[0] == 2 and T[1] - H[1] == 1):
            T = (H[0] - 1, H[1])
        # Left 2 Down 1
        if (T[0] - H[0] == 2 and T[1] - H[1] == 1):
            T = (H[0] + 1, H[1])

        # Check if that is a new position for T
        if T not in T_Has_Been: T_Has_Been.add(T)

    return len(T_Has_Been)



def part2():
  file = open('day09-input.txt')
  rope = [(0,0)]*10
  T_Has_Been = set()
  T_Has_Been.add((0, 0))
  order = []

  for line in file:
    line = line.strip().split()
    for i in range(int(line[1])):
        order.append(line[0])

  for dir in order:
    H = rope[0]
    if dir == 'U':
        H = (H[0], H[1] + 1)
    if dir == 'D':
        H = (H[0], H[1] - 1)
    if dir == 'L':
        H = (H[0] - 1, H[1])
    if dir == 'R':
        H = (H[0] + 1, H[1])
    rope[0] = H
    
    for i in range(0,9):
      H, T = rope[i], rope[i+1]
      # DIRECT
      # Right by 2
      if (H[0] - T[0] == 2 and H[1] - T[1] == 0):
          T = (H[0] - 1, T[1])
      # Left by 2
      if (T[0] - H[0] == 2 and H[1] - T[1] == 0):
          T = (H[0] + 1, T[1])
      # Up by 2
      if (H[1] - T[1] == 2 and H[0] - T[0] == 0):
          T = (T[0], H[1] - 1)
      # Down by 2
      if (T[1] - H[1] == 2 and H[0] - T[0] == 0):
          T = (T[0], H[1] + 1)

      # Diagonal
      # Right Up
      if (H[0] - T[0] == 2 and H[1] - T[1] == 2):
          T = (H[0]-1, H[1]-1)
      # Right Down
      if (H[0] - T[0] == 2 and T[1] - H[1] == 2):
          T = (H[0]-1, H[1]+1)
      # Left Up
      if (T[0] - H[0] == 2 and H[1] - T[1] == 2):
          T = (H[0]+1, H[1]-1)
      # Left Down
      if (T[0] - H[0] == 2 and T[1] - H[1] == 2):
          T = (H[0]+1, H[1]+1)
  
      # HORSE
      # Up 2 Right 1
      if (H[0] - T[0] == 1 and H[1] - T[1] == 2):
          T = (H[0], H[1] - 1)
      # Up 2 Left 1
      if (T[0] - H[0] == 1 and H[1] - T[1] == 2):
          T = (H[0], H[1] - 1)
      # Down 2 Right 1
      if (H[0] - T[0] == 1 and T[1] - H[1] == 2):
          T = (H[0], H[1] + 1)
      # Down 2 Left 1
      if (T[0] - H[0] == 1 and T[1] - H[1] == 2):
          T = (H[0], H[1] + 1)
  
      # Right 2 Up 1
      if (H[0] - T[0] == 2 and H[1] - T[1] == 1):
          T = (H[0] - 1, H[1])
      # Left 2 Up 1
      if (T[0] - H[0] == 2 and H[1] - T[1] == 1):
          T = (H[0] + 1, H[1])
      # Right 2 Down 1
      if (H[0] - T[0] == 2 and T[1] - H[1] == 1):
          T = (H[0] - 1, H[1])
      # Left 2 Down 1
      if (T[0] - H[0] == 2 and T[1] - H[1] == 1):
          T = (H[0] + 1, H[1])
      rope[i] = H
      rope[i+1] = T

    # Check if that is a new position for T
    if rope[9] not in T_Has_Been: T_Has_Been.add(rope[9])
  # print(rope)
  # plot(rope)
  # time.sleep(0.1)
  return len(T_Has_Been)


print('Part #1 -', part1())
print('Part #2 -', part2())