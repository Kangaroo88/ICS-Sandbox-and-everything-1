import random

# Input
# (int) piles: a list of integers >= 0.  The integer indicatates how many objects remain in that pile
# 
# Output
# (int) pile: which pile objects should be removed from
# (int) objects_to_remove: number of objects to remove from the pile specified above

def my_turn(piles):
  while True:
    pile_number = random.randint(0, (len(piles)-1))
    number_remove = random.randint(1, 5)
    if number_remove <= piles[pile_number]:
      break
  
  return pile_number, number_remove