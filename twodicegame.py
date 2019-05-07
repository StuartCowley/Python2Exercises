"""
This program rolls two dice, adds the result together and asks the user for to guess the total. If right, the user wins, if not the computer wins
"""
from random import randint
from time import sleep
def get_user_guess():
  guess = int(raw_input("Whats your guess?"))
  return guess

def roll_dice(number_of_sides):
  first_roll = randint(1, number_of_sides)
  second_roll = randint(1, number_of_sides)
  max_val = number_of_sides * 2
  guess = get_user_guess()
  if guess > max_val:
    print "No guesses higher than %d are possible!" % max_val
  else:
    print "Rolling..."
    sleep(2)
    print "The first roll is %d" % first_roll
    sleep (1)
    print "The second roll is %d" % second_roll
    sleep (1)
    total_roll = first_roll + second_roll
    print "Result %d" % total_roll
    sleep (1)
    if guess == total_roll:
      print "You won!"
    else:
      print "You lose!"

roll_dice(6)
