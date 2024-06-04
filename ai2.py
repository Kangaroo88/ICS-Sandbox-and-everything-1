# Input
# (int) piles: a list of integers >= 0.  The integer indicatates how many objects remain in that pile
# 
# Output
# (int) pile: which pile objects should be removed from
# (int) objects_to_remove: number of objects to remove from the pile specified above


def my_turn(piles): 
 # return 1,1
  # piles = [1, 2, 3, 4, 3, 2, 1]

  # Deal with any pile >= 3
  # if any pile >= 3 has > 0 sticks, take all of them
 
  for sticks in range(0, len(piles)):
    print(sticks)
    if sticks > 0:
      stick_take_away = 3
      random_1 = 3
      return random_1, stick_take_away