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

No_of_ships = 2
hits = 0
moves = 0

# Assign values to the ships coordinates:
ship1_row = random_row(board)
ship1_col = random_col(board)

ship2_row = random_row(board)
ship2_col = random_col(board)

# Removing possibility of duplicate ships:
if ship1_row == ship2_row and ship2_col == ship2_col:
  ship2_row = random_row(board)
  ship2_col = random_col(board)


# For debugging purposes only
# print (ship1_row + 1)
# print (ship1_col + 1)
# print (ship2_row + 1)
# print (ship2_col + 1)

# Inform user of number of ships
print "There are %s ships one square in size somewhere in this grid..." % (No_of_ships)

def strikes():
  global hits
  for line in board:
    for char in line:
      if char == "B":
        hits += 1
  return hits

def play_game():
    global moves
    for turn in range(moves,(moves+4)):
      print ""
      print "Turn", turn + 1
      guess_col = (int(raw_input("Guess Column: "))-1)
      guess_row = (int(raw_input("Guess Row: "))-1)
      if ((guess_col == ship1_col and guess_row == ship1_row) or (guess_col == ship2_col and guess_row == ship2_row)) and board[guess_row][guess_col] != "B":
        print ""
        print "Congratulations! You sank 1 battleship!"
        board[guess_row][guess_col] = "B"
        print_board(board)
        strikes()
        if hits > 2:
          print "Congratulations, you have defeated my fleet! \n"
          print_board(board)
          print ""
          break
      elif guess_row not in range(5) or guess_col not in range(5):
        print "Oops, that's not even in the ocean."
      elif board[guess_row][guess_col] == "B":
        print "You already sank a ship there, try again"
        print_board(board)
      elif board[guess_row][guess_col] == "X":
        print( "You guessed that one already." )
      else:
        if turn == 7:
          print ""
          print "Game Over!"
          print "Ships were in the squares marked B. Better luck next time!"
          board[guess_row][guess_col] = "X"
          board[ship1_row][ship1_col] = "B"
          board[ship2_row][ship2_col] = "B"
          print_board(board)
          print ""
        else:
          print ""
          print "You missed my battleship!"
          board[guess_row][guess_col] = "X"
          print_board(board)

# Perform the function twice to enable the user to quit during the game

def complete():
  global moves
  strikes()
  moves = 0
  play_game()
  if hits < 2:
    quit = raw_input("Had enough yet? Press q to quit or any other key to continue: ")
    if quit == "Q" or quit == "q":
      print "Okay, till next time... \n"
    else:
      moves = 4
      play_game()
      strikes()


complete()
