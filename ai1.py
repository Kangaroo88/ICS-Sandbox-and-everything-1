import random

# Input
# (int) piles: a list of integers >= 0.  The integer indicatates how many objects remain in that pile
# 
# Output
# (int) pile: which pile objects should be removed from
# (int) objects_to_remove: number of objects to remove from the pile specified above

def my_turn(piles):
  #[3, 5, 7, 9, 11]
  # 0  1  2  3   4 
  #[3, 0, 2, 0, 0]
  # 0  1  2  3  4 
  
  #length
  pile = random.randint(0,(len(piles) - 1))
  
  #                     0   5
  # 0, 1, 2, 3...
  return pile, random.randint(1, 5)