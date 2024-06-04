import random 

def my_turn(piles):
  
  for i in range(len(piles)):
    if piles[i] == 3:
      return i, 2
  for i in range(len(piles)):
    if piles[i] == 5:
      return i, 4
  for i in range(len(piles)):
    if piles[i] == 7:
      return i, 6
  for i in range(len(piles)):
    if piles[i] == 2:
      return i, 1
  for i in range(len(piles)): 
    if piles[i] == 4:
      return i, 3
  for i in range(len(piles)):
    if piles[i] == 6:
      return i, 5
  for i in range(len(piles)):
    if piles[i] == 1:
      return i, 1

  last_number = 1, 2, 3, 4, 5
  if piles == [last_number, 0, 0]:
    return 0, last_number
  elif piles == [0, last_number, 0]:
    return 1, last_number
  elif piles == [0, 0, last_number]:
    return 2, last_number

  

  elif piles == [1, 1, 0]:
    return 0, 1
  elif piles == [1, 0, 1]:
    return 0, 1
  elif piles == [0, 1, 1]:
    return 1, 1
  elif piles == [1, 1, 1]:
    return 0, 1


  # keep doing moves so that it doesn't make an error
  elif piles[0] != 0:
    return 0, 1
  elif piles[1] != 0:
    return 1, 1
  elif piles[2] != 0:
    return 2, 1
  elif piles[3] != 0:
    return 3, 1
  elif piles[4] != 0:
    return 4, 1

  # remove one from a pile that is odd
  for i in range (len(piles)):
    for a in range (len(piles[i])):
      if a % 2 != 0: 
        return a, 1