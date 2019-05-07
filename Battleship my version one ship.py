#! /usr/bin/env python
from random import randint

# Initialise the board
board = []

# Use a loop to create a row and append it to the board
for x in range(0,5):
  board.append(["O"] * 5)

# Make the board look more presentable
def print_board(board):
  for row in board:
    print " ".join(row)

print ""
print_board(board)

# Generate a random number for the row
def random_row(board):
  return randint(0, len(board) - 1)

# Generate a random number for the column
def random_col(board):
  return randint(0, len(board[0]) - 1)

# Assign these values to a ship coordinate
ship_row = random_row(board)
ship_col = random_col(board)

# For debugging purposes only
# print (ship_row + 1)
# print (ship_col + 1)

# Inform user of number of ships
print "There is a single ship one square in size somewhere in this grid..."


def play_game():
    for turn in range(moves,(moves+4)):
      print ""
      print "Turn", turn + 1
      guess_col = (int(raw_input("Guess Column: "))-1)
      guess_row = (int(raw_input("Guess Row: "))-1)
      if guess_col == ship_col and guess_row == ship_row:
        print ""
        print "Congratulations! You sank my battleship!"
        break
      elif guess_row not in range(5) or guess_col not in range(5):
        print "Oops, that's not even in the ocean."
      elif board[guess_row][guess_col] == "X":
        print( "You guessed that one already." )
      else:
        if turn == 7:
          print ""
          print "Game Over!"
          print "Ship was in the square marked B"
          board[guess_row][guess_col] = "X"
          board[ship_row][ship_col] = "B"
          print_board(board)
          print ""
          play = False
        else:
          print ""
          print "You missed my battleship!"
          board[guess_row][guess_col] = "X"
          print_board(board)

# Perform the function twice to enable the user to quit during the game
moves = 0
play_game()
quit = raw_input("Had enough yet? Press q to quit or any other key to continue: ")
if quit == "Q" or quit == "q":
  print "Okay, till next time... \n"  
else:
  moves = 4
  play_game()



