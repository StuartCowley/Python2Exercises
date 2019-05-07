#! /usr/bin/env python

"""
This is a rock paper scissors game
"""
from random import randint

options = ["ROCK", "PAPER", "SCISSORS"]
message = {"tie": "Yawn it's a tie!", "won":"Yay you won!", "lost":"Aww you lost!"}

# Added an option to quit if losing multiple rounds

def decide_winner(user_choice,computer_choice):
  print "You chose %s" % user_choice
  print "Computer chose %s" % computer_choice
  if user_choice == computer_choice:
    print
    print message["tie"]
    quit = raw_input("Had enough? Press X to quit, any other key to keep playing ").upper()
    if quit == "X":
      print "Another time then"
      print
    else:
      play_RPS()
  elif user_choice == options[0] and computer_choice == options[2]:
    print
    print message["won"]
  elif user_choice == options[1] and computer_choice[0]:
    print
    print message["won"]
  elif user_choice == options[2] and computer_choice[1]:
    print
    print message["won"]
  else:
    print
    print message["lost"]
    quit = raw_input("Had enough? Press X to quit, any other key to keep playing ").upper()
    if quit == "X":
      print
      print "Another time then"
    else:
      play_RPS()
      
def play_RPS():
  user_choice = raw_input("Enter Rock, Paper, or Scissors: ").upper()
  print user_choice
  computer_choice = options[randint(0,2)]
  decide_winner(user_choice, computer_choice)

play_RPS()

