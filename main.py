#  Code tracing: ---------------------------------------------------

# def pythag(num1, num2):
#   a = num1 * num1
#   b = num2 * num2

#   c = a + b
#   c = c**(1/2)
#   return c



# print(pythag(3, 4))
# print(pythag(0, 0))
# print(pythag(0, 4))
# print(pythag(-3, -4))
# print(pythag(-3, 4))
# print(pythag(3.2, 4.6))
# Code tracing Binary Numbers-----------------------------------------
# # find a target number in a list of numbers by splitting the list in two and searching one half at a time
# def binary_search(numbers, low_index, high_index, target):
#   # target doesn't exist in our list of numbers
#   if low_index > high_index:
#     return -1
    
#   # search the list of numbers for our target
#   else:
#     # find the middle of the list
#     middle_index = high_index + low_index // 2

#     # target is right at the middle
#     if target == numbers[middle_index]:
#       return middle_index

#     # target is smaller than the middle element
#     # so check the smaller half
#     elif target < numbers[middle_index]:
#       return binary_search(numbers, low_index, middle_index - 1, target)

#     # target is larger than the middle element
#     # so check the larger half
#     elif target > numbers[middle_index]:
#       return binary_search(numbers, middle_index + 1, high_index, target)
   



      
# # Test our search function

      
# numbers_to_search = [2, 3, 4, 10, 15, 17, 23, 24, 40, 52, 66, 79, 99]
# number_to_find = 66

# location = binary_search(numbers_to_search, 0, len(numbers_to_search) - 1, number_to_find)

# print(number_to_find, 'can be found in', numbers_to_search, 'at index', location)
# Debugging-----------------------------------------------
# # This function takes a list of numbers as input,
# # and returns the sum of all of the even numbers in that list
# def add_evens(numbers):
#   sum = 1
#   for number in numbers:
#     if number % 2:
#       sum = number=
#   return sum


# while True:
#   # get some numbers from the user
#   print('--- Let\'s create a list of numbers ---')
#   user_numbers = []

#   list_complete = False
#   while not list_complete:
#     try:
#       user_input = input('Enter a number, or press enter to finish your list: ')
#       if user_input == '':
#         list_complete = True
#       else:
#         user_numbers.append(int(user_input))
#         list_complete = False
#     except ValueError:
#       print('I was expecting a number.  Let\'s try that again')

#   # get the total of the even numbers in the list
#   sum_of_evens = add_evens(user_numbers)
#   print('The even numbers add up to', sum_of_evens)
# Debugging (& Testing)

# The `add_evens()` function and main code that makes use of it has been hastily written by a careless programmer, and now it's up to you to fix this mess.

# Use your intuition and expertise to debug the code:
# - WHAT is the code supposed to do?
# - HOW did the programmer intend to make this happen?
# - What does the code ACTUALLY do?
# - How can you change what the code CURRENTLY does to make it do what it SHOULD?
# - What sort of testing will you do to ENSURE that the code behaves as expected?

# When you have fixed the code, update the `tests.md` file to include the tests that you used to ensure the code works.  Feel free to add as many tests as you need.
# User input:

# Expected output:

# Actual output:


# ---
# User input:

# Expected output:

# Actual output:


# ---
# User input:

# Expected output:

# Actual output:


# ---

# Debugging Primes---------------------------------------------------
# # determine the first 20 prime numbers

# primes_found = 0
# current_number = 1

# while (primes_found < 50):
#   number_is_prime = True
#   for i in range(2, (current_number - 1)):
    
#     # If current_number can be divided cleanly, it is not prime
#     if current_number % i == 0:
#       number_is_prime = False

#   # Prime number has been found
#   if number_is_prime:
#     primes_found += 1
#     print('prime found:', current_number)
#   current_number += 1 


# # x % y
# # x / y --> remainder?

# # 11 % 2
# # 11 % 3
# # 11 % 4
# # 11 % 5
# # 11 % 6
# # 11 % 7
# # 11 % 8
# # 11 % 9
# # 11 % 10

# ########################
# # DEBUGGING STRATEGIES #
# ########################
# # 1) What is the code SUPPOSED to do?
# # 2) What does the code ACTUALLY do?
# # 3) How do I go from ACTUALLY to SUPPOSED?
# # :(
# # :/
# # 4) Use print() to output a behind-the-scenes look at variable values
# # 5) Trim the problem down
# # 6) Comment out, don't delete until your're done
# # 7) Add comments for new understanding of logic


# Efficiency Sorting----------------------------------------
# # Sort a list of numbers from low to high
# # Input: a list of numbers
# # Returns: the same numbers, sorted from low to high
# def custom_sort(numbers_list):
#   # we will count how many times we check whether we should swap two numbers
#   swap_check_count = 0
  
#   # len(numbers_list) will return a count of how many items are in numbers_list
#   # range(0, len(numbers_list)) will give us a list of indexes to refer to locations in numbers_list
#   for i in range(0, len(numbers_list)):
#     for j in range(0, len(numbers_list)):
#       swap_check_count += 1
#       if i < j and numbers_list[i] > numbers_list[j]:
#         temporary_number_holder = numbers_list[i]
#         numbers_list[i] = numbers_list[j]
#         numbers_list[j] = temporary_number_holder
#   print(swap_check_count, 'swap checks performed')
#   return numbers_list
# # reduce comparisions!!!!!!! is what you have to do


# # sort a list of numbers, in order to test our function
# unsorted_numbers = [11, 6, 2, 9, 14, 1, 2, 19, 7, 3]
#                   # 0   1  2  3   4  5  6  7   8  9
# sorted_numbers = custom_sort(unsorted_numbers)

# print(sorted_numbers)

# # Do I need to check every single item in the list ?
# # Do I need to start checking at the beginning each time?


# Nim development-----------------------------------------------------------

# import random

# # >>> Be sure to add any other ai files that you want to test
# import ai1 as player1
# import ai2 as player2
# import ai3 as player3


# def choose_first_player(players):
#     return random.choice(players)


# def play_nim(players, piles):
#     print('---', players[0].__name__, 'vs.', players[1].__name__, '---')
#     current_player = choose_first_player(players)
#     winner = None
#     # players take one turn at a time
#     while not winner:
#         # show the current board
#         print_piles(piles)

#         # get the current player's move
#         try:
#             selected_pile, to_remove = current_player.my_turn(piles)
#             selected_pile = int(selected_pile)
#             to_remove = int(to_remove)

#             # ensure that the player's move was valid
#             if (selected_pile < 0 or selected_pile > len(piles) - 1
#                     or to_remove < 1 or piles[selected_pile] < to_remove):
#                 print('Invalid move -', current_player.__name__,
#                       'tried to remove', to_remove, 'from pile #',
#                       selected_pile)
#                 winner = players[(players.index(current_player) + 1) % 2]
#             else:
#                 print(current_player.__name__, 'removed', to_remove,
#                       'from pile #', selected_pile)

#                 # remove the amount chosen
#                 piles[selected_pile] -= to_remove

#                 # check the board after the player's move
#                 winner = current_player
#                 for pile in piles:
#                     if pile != 0:
#                         winner = None
#                         break

#         except TypeError:
#             print(
#                 'Invalid move input by',
#                 current_player.__name__,
#             )

#         # switch to the other player
#         if not winner:
#             current_player = players[(players.index(current_player) + 1) % 2]
#     print(winner.__name__, 'wins!!!')


# def print_piles(piles):
#     print(' | '.join([str(pile) for pile in piles]))


# def set_piles(difficulty=0):
#     return [[1, 2, 3], [3, 5, 7], [2, 3, 4, 5], [1, 3, 5, 3, 1],
#             [3, 5, 3, 5, 3], [7, 3, 6, 3, 2, 4, 5, 9, 1, 9]][difficulty]


# def select_players(all_players):
#     print('Player options:')
#     for i in range(len(all_players)):
#         print(i, '-', all_players[i].__name__)
#     return (all_players[int(input('Select first player > '))],
#             all_players[int(input('Select second player > '))])


# # >>> add more player names if you've added more AIs
# player1.__name__ = '✨Nimble Nimbus 2000🧹✨'
# player2.__name__ = 'AI 2'
# player3.__name__ = 'AI 3'

# # >>> and add the new ai player to thi1s list
# play_nim(
#     select_players([player1, player2, player3]),
#     # >>> Update the set_piles input from 0 to 5 in order to change the difficulty
#     set_piles(0))


# # -Nim Tournament edition-----------------------------------

# import random, time

# import ai1 as player1
# import ai2 as player2
# import ai3 as player3
# import ai4 as player4
# import ai5 as player5

# SLEEP = 1

# def choose_first_player(players):
#   return random.choice(players)

# def play_nim(players, piles):
#   print(
#     '---', 
#     players[0].__name__,
#     'vs.',
#     players[1].__name__,
#     '---'
#   )
#   input('- Press any key to proceed -')
#   current_player = choose_first_player(players)
#   winner = None
#   # players take one turn at a time
#   while not winner:
#     # show the current board
#     print_piles(piles)
#     time.sleep(SLEEP)
#     # get the current player's move
#     try:
#       selected_pile, to_remove = current_player.my_turn(piles)
#       selected_pile = int(selected_pile)
#       to_remove = int(to_remove)

#       # ensure that the player's move was valid
#       if (
#         selected_pile < 0 or 
#         selected_pile > len(piles) - 1 or
#         to_remove < 1 or 
#         piles[selected_pile] < to_remove
#       ):
#         print(
#           'Invalid move -', current_player.__name__,
#           'tried to remove',
#           to_remove,
#           'from pile #',
#           selected_pile
#         )
#         winner = players[
#           (players.index(current_player) + 1) % 2
#         ]
#       else:
#         print(
#           current_player.__name__,
#           'removed',
#           to_remove,
#           'from pile #',
#           selected_pile
#         )

#         # remove the amount chosen
#         piles[selected_pile] -= to_remove

#         # check the board after the player's move
#         winner = current_player
#         for pile in piles:
#           if pile != 0:
#             winner = None
#             break
    
#     except TypeError:
#       print(
#         'Invalid move input by', current_player.__name__,
#       )
    
#     # switch to the other player
#     if not winner:
#       current_player = players[
#         (players.index(current_player) + 1) % 2
#       ]
#   print(winner.__name__, 'wins!!!')
#   return winner


# def print_piles(piles):
#   print(' | '.join([str(pile) for pile in piles]))

# def set_piles(difficulty = 0):
#   return [
#     [1, 2, 3],
#     [3, 5, 7],
#     [2, 3, 4, 5],
#     [1, 3, 5, 3, 1],
#     [3, 5, 3, 5, 3],
#     [7,3,6,3,2,4,5,9,1,9]
#   ][difficulty]

# def select_players(all_players):
#   print('Player options:')
#   for i in range(len(all_players)):
#     print(i,'-', all_players[i].__name__)
#   return (
#     all_players[int(input('Select first player > '))],
#     all_players[int(input('Select second player > '))]
#   )

# def round_robin(players):
#   for first in players:
#     for second in players:
#       if first.__name__ != second.__name__:
#         winner = play_nim([first, second],
#                           set_piles(random.randint(0, 2)))
#         winner.__wins__ += 1
        
  

# player1.__name__ = 'AngelaIshaanSaaynaVanessa'
# player2.__name__ = 'AliAmberFaryalKamran'
# player3.__name__ = '✨Nimble Nimbus 2000🧹✨'
# player4.__name__ = 'AydinColinDhruv'
# player5.__name__ = 'GabeLauraNandish'

# all_players = [player1, player2, player3, player4, player5]

# # Initialize win count
# for player in all_players:
#   player.__wins__ = 0
#   player.__tiebreaker_wins__ = 0

# # Carry out round robin phase of the tournament
# round_robin(all_players)
# input('- Press any key to view the round robin results -')
# for player in all_players:
#   print(player.__name__, '-', player.__wins__)

# # Resolve any ties coming out of the round robin phase
# ties_to_resolve = input('Are there ties to resolve? (Y or N) > ') == 'Y'
# while ties_to_resolve:
#   winner = play_nim(
#     select_players(all_players),    
#     set_piles(random.randint(0, 2))
#   )
#   winner.__tiebreaker_wins__ += 1
#   print('--- Updated Standings ---')
#   for player in all_players:
#     print(player.__name__, '-',
#           player.__wins__, '-',
#           player.__tiebreaker_wins__)
#   ties_to_resolve = input('Are there more ties to resolve? (Y or N) > ') == 'Y'

# # Finals - best of 3
# print('==============================')
# print('=== FINAL ROUND: BEST OF 3 ===')
# print('==============================')
# finalists = select_players(all_players)
# finalists[0].__finals_wins__ = 0
# finalists[1].__finals_wins__ = 0
# print('=== Round 1 ===')
# winner = play_nim(finalists, set_piles(3))
# winner.__finals_wins__ += 1

# print('=== Round 2 ===')
# winner = play_nim(finalists, set_piles(4))
# winner.__finals_wins__ += 1

# if(finalists[0].__finals_wins__ == 2):
#   print('!!!!!!!!!!!!!!!!!!!!!!!', )
#   print('!!! Congratulations !!!')
#   print('!!!!!!!!!!!!!!!!!!!!!!!', )
#   print(finalists[0].__name__, 'is the grand champion of the Nim world!')
# elif(finalists[1].__finals_wins__ == 2):
#   print('!!!!!!!!!!!!!!!!!!!!!!!', )
#   print('!!! Congratulations !!!')
#   print('!!!!!!!!!!!!!!!!!!!!!!!', )
#   print(finalists[1].__name__, 'is the grand champion of the Nim world')
# else:
#   print('!!!!!!!!!!!!!!!!!!!', )
#   print('!!! FINAL ROUND !!!')
#   print('!!!!!!!!!!!!!!!!!!!', )
#   winner = play_nim(finalists, 
#                     set_piles(5))
#   winner.__finals_wins__ += 1
#   if(finalists[0].__finals_wins__ == 3):
#     print('!!!!!!!!!!!!!!!!!!!!!!!', )
#     print('!!! Congratulations !!!')
#     print('!!!!!!!!!!!!!!!!!!!!!!!', )
#     print(finalists[0].__name__, 'is the grand champion of the Nim world')
#   elif(finalists[1].__finals_wins__ == 3):
#     print('!!!!!!!!!!!!!!!!!!!!!!!', )
#     print('!!! Congratulations !!!')
#     print('!!!!!!!!!!!!!!!!!!!!!!!', )
#     print(finalists[1].__name__, 'is the grand champion of the Nim world')




# ====================================================================
# ====================================================================
# ====================================================================
# My Sandbox------------------------------------

 # welcome to my code
# print ("Hello world!👋")
# name = input('What is your name, traveler? ')
# print("Hello", name, "!")
# favourite_animal = input('What is your favourite animal? ')
# favourite_food = input('And what is your favourite food? ')
# print ('Ooh... how interesting!')
# print ('Processing information...')
# print ('Complete! User profile made!')
# print('Name:', name)
# print('Favourite animal:', favourite_animal)
# print('Favourite food:', favourite_food)

# number1 = int(input('Pick a number: '))
# number2 = int(input('Pick another number: '))
# sum = number1 + number2
# print("The sum of these numbers is: ", sum)

#Review of Day 1:

# print: command that allows you to print a message (sometimes text) to the user. Followed by the message surrounded by brackets, and either single or double quotations.
# anything = anything (Variable): A command that allows you to create a variable. Makes things efficient by not having to type it out repeatedly. Can be printed. Can be followed by input.
#input() : Lets the user insert an input that will allow you to have a sense of interactivity. It normally is used to make a variable.

#age = int(input('How old are you? '))
#if age > 12 and age <= 19:
 # print('You are older than age 12.')
  #print('Congratulations on being a teenager.')
#elif age <= 12:
#  print('You are still a tween!')
#else:
 # print('Any age is cool though.')

# Review of Day 2

#Operators:

# age = int(input("How old are you? "))
# # if age > 12 and age <=19:
# #   print('You are old!')

# numbers = (1, 2, 3, 4, 5,)
# print(numbers)

# name1 = 'Azka'
# name2 = 'Alishba'
# names = ['Mr.M, Someone, Someone else']
# print(name1, name2, names)

# for loop_name in names:
#   print('Hello', loop_name)
# course_name = 'Computer Science'
# for letter in course_name:
# print('The next letter is:', letter)

# # while loop
# i = 0
# while i <= 10
# if i != 3:
#   print('i=', i)
# 1 = 1 + 1

# def say_hello(person_name):
#   print('Hello', person_name)
#   age = input('How old are you? ')
#   print('You are', age, 'years old')

# names = ['Colin', 'Azka', 'Lorenzo']
# for name in names:
#   say_hello(name)


# # print("I'm done saying hi")

# # def find_slope(first_y, first_x, second_y, second_x):
# #   new_slope = (first_y - second_y) / (first_x - second_x)
# #   return new_slope



# # try:
# #   y1 = 5
# #   x1 = 8
# #   y2 = int(input('give me a y2'))
# #   x2 = int(input('give me an x2'))
# #   my_slope = find_slope(y1, x1, y2, x2)
# #   print(my_slope)
# # except:
# #   print('Something went wrong.')
# ===================================================
# # BOOLEAN OPERATORS
# # "and", "or", "not"

# boolean_values = [True, False]

# for boolean_value in boolean_values:
#   a = boolean_value
  
#   for boolean_value2 in boolean_values:
#     b = boolean_value2
#     print('a:', a)
#     print('b:', b)
#     print('---------')
#     print('a and b:',
#       a and b
#     )
    
#     print('a or b:',
#       a or b
#     )
    
#     print('not a:',
#       not a
#     )
    
#     print('not b:',
#       not b
#     )

#     print('not(a and b):',
#       not(a and b)
#     )
    
#     print('
# #=======================================================
# age = 15
# favourite_course = 'Computer science'
# if (13 <= age <= 19) and (favourite_course == 'Computer science'):
#   #      false     and          true
#   #               false
#   print('Smart teenager alert')
# else:
#   print("Don't care, you don't belong here")
# #=======================================================
# # Truthiness
# 0 behaves like False
# all other numbers behave like True
# strings behave like True
# empty strings behave like False

# name = 'Lorenzo'
# age = 15

# if name:
#   print('name detected')
# else:
#   print('no name?!?!')

# if age:
#   print('you have been born')
# else:
#   print('you have not been born yet')
# determine the first 20 prime numbers

# range --- counts the numbers between the range set like (1,10) so it will only count the numbers from 1 to 9 no less or no more then that 
# determine the first 20 prime numbers

# primes_found = 0
# current_number = 1

# while (primes_found < 50):
#   number_is_prime = True
#   for i in range(2, current_number - 1):
    
#     # If current_number can be divided cleanly, it is not prime
#     if current_number % i == 0:
#       number_is_prime = False
#   if number_is_prime:
#     primes_found += 1
#     print('prime found:', current_number)
#   current_number += 1 
# Function in a function ---------------
# Count up from 1 to 100
# def count_up(current_number):
#   print(current_number)
#   if current_number < 100:
#     count_up(current_number + 1)



# count_up(1)
# # -----------
# print('--------- Recursive Function ----------')
# def add_up(current_number):
#   print('-------------')
#   # End / Break case
#   if current_number == 10:
#     # Total sum of [10]
#     print('Break case - just return 10')
#     return 10
#   # Otherwise, we need to add our current number to what we know
#   else:    
#     print('current_number:', current_number)
#     print('find the sum of everything from', current_number + 1 , 'to 10')
#     sum_of_higher_numbers = add_up(current_number + 1)

# print('--------- Recursive Function ----------')
# def add_up(current_number):
#   print('-------------')
#   # End / Break case
#   if current_number == 10:
#     # Total sum of [10]
#     print('Break case - just return 10')
#     return 10
#   # Otherwise, we need to add our current number to what we know
#   else:    
#     print('current_number:', current_number)
#     print('find the sum of everything from', current_number + 1 , 'to 10')
#     sum_of_higher_numbers = add_up(current_number + 1)
#     print('the sum of higher numbers is', sum_of_higher_numbers)

#     print('add', current_number, 'to', sum_of_higher_numbers)
#     new_sum = current_number + sum_of_higher_numbers

#     print('return our new sum either to get used by one level up, or by the main code')
#     return new_sum
# print('Sum from recursive function:', add_up(0))
#--------------------------------------------
# word = 'abcdefg'
# first_letter = for letter in word:
#   if letter = 'a':
#   'a'=first_letter
#   else try last_letter
# last_letter = for letter in word:
#   if letter = 'g'
#   'g' = last_letter
# middle = 'bcdefg'
# print(first_letter, last_letter, middle)
#--------------------------------------------
# from math import sqrt, ceil
# from time import time

# primes_found = 0
# current_number = 1
# primes_to_find = 10000

# start_time = time.time()
# while (primes_found <= primes_to_find):
#   number_is_prime = True  
#   for i in range(2, ceil(sqrt(current_number + 1))):
#     # If current_number can be divided cleanly, it is not prime
#     if current_number % i == 0:
#       number_is_prime = False
      
#   if number_is_prime:
#     primes_found += 1
#     print('prime found:', current_number)
#   current_number += 1 
#   current_number += 1 
# end_time = time.time()
# efficient_time_elapsed = end_time - start_time 



# primes_found = 0
# current_number = 1

# start_time = time.time()
# while (primes_found < primes_to_find):
#   number_is_prime = True
  
#   for i in range(2, current_number):
#     # If current_number can be divided cleanly, it is not prime
#     if current_number % i == 0:
#       number_is_prime = False
      
#   if number_is_prime:
#     primes_found += 1
#     print('prime found:', current_number)
#   current_number += 1
# end_time = time.time()
# inefficient_time_elapsed = end_time - start_time 

# print("Efficient:", efficient_time_elapsed)
# print("Inefficient:", inefficient_time_elapsed)
#---------------------------------------------
## Get a word to check from user
# word_to_check = input
# if is_palindrome(word_to_check)
#  print a positive message to user
# else
#  print a negative message to user


# function is_palindrome(word_to_check)
  # Count number of letters in the word
  # letter_count = length(word_to_check)
  
  # if letter_count == 0 or 1
  #   return true
  
  # else 
  #  if first letter == last letter
  #    word_to_check = word, but remove first letter & last letter
  #    return is_palindrome(word_to_check
  #    return is_palindrome(word_to_check)
  #  else
  #    return false
#==============
# count = 0
# for a in range(1,10):
#   for b in range(1,10):
#     for c in range(1,10):
#       for d in range(1,10):
#         for e in range(1,10):
#           for f in range(1,10):
#             if a + b + c + d + e + f == 51:
#               count +=1
# print(count)


# # Constant
# NUMBER_OF_STUDENTS = 20

# SECONDS_IN_ONE_DAY = 60 * 60 * 24


# for i in range(SECONDS_IN_ONE_DAY):
#   print(i)


# print('I have 20 students in my class')
# #============================================

# ## Variable types ##
# number = 20
# character_or_string = '3'
# my_list = [20, 3, 5, '3', 'abc', 'a']
# #          0   1  2   3     4     5
# my_list[3]

# DICTIONARY #
# classes = ['math', 'chemistry', 'history', 'english']

# favourite_teacher = 'Mr McKinley Evans'
# all_classes = [
#   {
#     'name': 'Math',
#     'room': 123,
#     'teacher': favourite_teacher,
#     'period': 3,
#     'homework': ''
#   },
#   {
#     'name': 'Chem',
#     'room': 456,
#     'teacher': 'Ms Skirrow',
#     'period': 2,
#     'homework': ''
#   },
#   {
#     'name': 'History',
#     'room': 456,
#     'teacher': 'Ms X',
#     'period': 1,
#     'homework': ''
#   },
#   {
#     'name': 'English',
#     'room': 456,
#     'teacher': 'Ms Vodicka',
#     'period': 4,
#     'homework': ''    
#   }
# ]

# print(all_classes)

# for one_class in all_classes:
#   print('Who is the teacher for,', one_class['name'])
#   one_class['teacher'] = input('>')
  
# print(all_classes)

# user_input = input('Some text: ')
# print(user_input)
# print(user_input.lower())
# print(user_input.upper())
# print(user_input.capitalize())


# my_video_games = {
#   "skyrim": {
#     "studio": "Bethesda",
#     "rate": 9.5,
#     "complete": False,
#     "genre": "RPG",
#     "rank": "1"
#   },
#   "fallout": {
#     "studio": "Bethesda",
#     "rate": 8,
#     "complete": True,
#     "genre": "RPG",
#     "rank": "3"
#   },
#   "nba2k":{
#     "studio": "2k Studios",
#     "rate": "8.5",
#     "complete": False,
#     "genre": "Sports",
#     "rank": 2
#   },
# }

# # print(my_video_games.keys())
# # print(my_video_games.values())

# for game in my_video_games:  
#   current_game = my_video_games[game]
#   print(game, '-', current_game['rank'])
# =========================================
# # Set up the positions of the pirates
# pirates = []
# for i in range(15):
#   pirates.append(i)
# print(pirates)

# # Remove one at a time until only 1 pirate remains
# current_position = 0
# while(len(pirates) > 1):
#   print(pirates)
#   pirates.pop(current_position)
#   # del(pirates[current_position])
#   current_position = (current_position + 1) % len(pirates)

# print(pirates)
# ===========================================
# from random import shuffle
# positions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # 0 1 2 3
# # 4     5
# # 6 7 8 9
# top = positions[0] + positions[1] + positions[2] + positions[3]
# left = positions[0] + positions[4] + positions[6]
# right = positions[3] + positions[5] + positions[9]
# bottom = positions[6] + positions[7] + positions[8] + positions[9]

# while top != left or top != right or top != bottom:
#   shuffle(positions)
#   top = positions[0] + positions[1] + positions[2] + positions[3]
# left = positions[0] + positions[4] + positions[6]
#   right = positions[3] + positions[5] + positions[9]
#   bottom = positions[6] + positions[7] + positions[8] + positions[9]
#   #print(positions)
#   print(top, left, right, bottom)

# print(positions[0], positions[1], positions[2], positions[3])
# print(positions[4], '   ', positions[5])
# print(positions[6], positions[7], positions[8], positions[9])


# -------------------------------------------------
# something funny
# # use print() to make text appear in the console

# # print(Hello world)
# print('Hey.')
# print('Yeah you, Shawaal.')
# input(print('Do you want to see something cool? '))
# print('Well then. Just watch.')
# x=1
# while x == 1:
#   print('Something cool')
# ====================================================================
# ====================================================================
# ====================================================================
# ====================================================================



# Commenting----------------------------------------------------
# Anything after a # is a comment, and will be ignored

# This will not run

# Print---------------------------------------------------

# # use print() to make text appear in the console

# # print(Hello world)
# print('Hey.')

# Variables-----------------------------------------
# # use variables to store & reference values

# our_class = 'ICS3U'
# print(our_class)

# our_class = 'Computer Studies'

# print(our_class)

# Variable names------------------------------------------

# # variables should be written in lowercase, with underscores between words
# # this is often referred to as "snakecase"
# # variables should be descriptive of their purpose

# teacher_name = 'Mr McKinley Evans'
# print(teacher_name)

# Variable Types-----------------------------------------

# # variables come in different types
# # mostly, you'll use integers, floats, and strings

# some_int = 12345
# some_float = 12345.6789
# some_str = '12345'

# print(type(some_int))
# print(type(some_float))
# print(type(some_str))

# product = some_int * some_float
# print(type(product))

# Input--------------------------------------------

# # use input() to collect input from the user
# # use input('Some text') to give the user a prompt before getting their input

# user_text = input('Enter some text > ')

# print(user_text)

# Operators------------------------------------------

# We use operators to make two values or variables interact with each other

# # assignment 
# my_variable = 1234

# # math
# sum = 2 + 2
# product = 2 * 2
# exponent = 2 ** 2
# division = 4 / 2

# # what is the remainder from division?
# modulus = 5 % 2 

# # divide, then round down
# floor_division = 5 // 2

# # comparison
# greater = 3 > 2
# less_than = 2 < 3
# greater_or_equal = 3 >= 2
# less_or_equal = 2 <= 3
# equal = 2 == 3
# not_equal = 2 != 3

# Conditionals (if/elif/else)----------------------------------------

# # Conditionals, or if-statements let us choose whether or not to execute a block of code

# if 3 < 2:
#   print('Sometimes')
#   print('More code')
# elif 4 > 5:
#   print('Something else')
# else:
#   print('Catch all')

# print('All the time')

# Recursion (while)------------------------------------------

# # We use a loop when we want to run the same code over and over again
# # A "while loop" will run repeatedly as long as its opening condition is true

# letters = 'i'
# while letters != 'iiiii':
#   print (letters)
#   letters = letters + 'i'
  

# Recursion with break-------------------------------------------

# # use break to get out of the loop early
# counter = 0

# early = input('Number to stop early: ')

# while counter < 10:
#   print(counter)
#   if counter == int(early):
#     break
#   counter = counter + 1

# print('I am done counting')

# Lists----------------------------------------

# # Lists (often casually called arrays) let us hold a set of values in a single variable
# # We use [ ] to show an array

# dogs = ['Carl', 'Tony', 'Etta', 'Carl']
# print(dogs)
# print(type(dogs))
# print(len(dogs))
# print(dogs[0])
# print(dogs[1])
# print(dogs[2])

# ---------------------------------------------------
# ---------------------------------------------------
# ---------------------------------------------------
# ---------------------------------------------------
# ---------------------------------------------------
# ---------------------------------------------------
# ---------------------------------------------------
