# Naod Philemon
# 12/08/2022

def visible(trees,x,y):
  length = len(trees)
  vis = True

  # Top
  for i in range(x-1, -1, -1):
    if trees[i][y] >= trees[x][y]: 
      vis = False
      break
  if vis: return True
  vis = True

  # Bottom
  for i in range(x+1, length):
    if trees[i][y] >= trees[x][y]: 
      vis = False
      break
  if vis: return True
  vis = True

  # Left
  for i in range(y-1, -1, -1):
    if trees[x][i] >= trees[x][y]: 
      vis = False
      break
  if vis: return True
  vis = True

  # Right
  for i in range(y+1, length):
    if trees[x][i] >= trees[x][y]: 
      vis = False
      break
  if vis: return True
  
  return False

def number(trees):
  count = 0

  for i in range(0,len(trees)):
    for j in range(0, len(trees)):
      if(visible(trees,i,j)):
        count += 1
  
  return count

def scenic(trees,x,y):
  length = len(trees)
  score = 1
  count = 0
  # Top
  for i in range(x-1, -1, -1):
    if trees[i][y] >= trees[x][y]:
      count += 1
      break
    elif trees[i][y] < trees[x][y]: count += 1
    else: break

  score *= count
  count = 0
  
  # Bottom
  for i in range(x+1, length):
    if trees[i][y] >= trees[x][y]:
      count += 1
      break
    elif trees[i][y] < trees[x][y]: count += 1
    else: break
  score *= count
  count = 0
  
  # Left
  for i in range(y-1, -1, -1):
    if trees[x][i] >= trees[x][y]:
      count += 1
      break
    elif trees[x][i] < trees[x][y]: count += 1
    else: break
  score *= count
  count = 0
  
  # Right
  for i in range(y+1, length):
    if trees[x][i] >= trees[x][y]:
      count += 1
      break
    elif trees[x][i] < trees[x][y]: count += 1
    else: break
  score *= count
  
  return score

def number2(trees):
  maxScenic = 0
  for i in range(1,len(trees)):
    for j in range(1, len(trees)):
      new = scenic(trees,i,j)
      
      if new > maxScenic: maxScenic = new

  return maxScenic



def main():
  file = open('day08-input.txt')
  trees = []
  for line in file:
    trees.append(line.strip())

  # Part 1
  print('Part 1', number(trees))

  # Part 2
  print('Part 2', number2(trees))

main()