# Naod Philemon
# 12/07/2022

dict = {
  ('/', '/') : {'dir': [],
        'files': [],
        'parent': ('/', '/'),
        'sum': 0
       }
}
current = ('/', '/')
listing = False

def getSum():
  return recurse(('/', '/'))

def recurse(dir):
  me = dict[dir]
  sum = 0
  for file in me['files']:
    sum += int(file[0])

  for di in me['dir']:
    num = recurse(di)
    sum += num
    
  dict[dir]['sum'] = sum
  return sum
#############################################

file = open('input.txt')
i = 0
for line in file:
  line = line.strip().split(' ')
  
  if line[0] == '$':
    if line[1] == 'cd':
      listing = False
      new = line[2]
      if new == '..':
        current = dict[current]['parent']
        continue
      current = (new, current[0])
      
    elif line[1] == 'ls':
      listing = True
      continue

  if listing:
    if line[0] == 'dir':
      new = (line[1], current[0])
      if new not in dict[current]['dir']:
        dict[current]['dir'].append(new)
        dict[new] = {'dir': [], 'files': [], 'parent': current, 'sum': 0}
      
    else:
      if((line[0], line[1])) not in dict[current]['files']:
        dict[current]['files'].append((line[0], line[1]))
    

sum = getSum() * 0
outermost = dict[('/', '/')]['sum']
unused = 70000000 - outermost
need = 30000000 - unused
min = outermost

for dir in dict:
  check = dict[dir]['sum']
  if check > 70000 and check < 75000: print(check)
  if check < min and check > need:
    min = check

print(outermost, unused, need, min)



from collections import defaultdict

# Dictionary with all directories

# Directory
# - Name of parent
# - List of directories inside of it
# - List of files inside of it