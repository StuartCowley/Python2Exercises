#! /usr/bin/env python

# code modded from original code academy course to accomodate for non numeric characters being inputted by mistake

def rgb_hex():
  invalid_msg = "Please input an RGB value in the correct format"

  red = raw_input("Input a value for red: ")
  if red.isalpha():
    print invalid_msg
    red = raw_input("Input a value for red: ")
  red = int(red)
  if red < 0 or red > 255:
    print invalid_msg
    return red

  green = raw_input("Input a value for green: ")
  if green.isalpha():
    print invalid_msg
    green = raw_input("Input a value for green: ")
  green = int(green)
  if green < 0 or green > 255:
    print invalid_msg
    return green
  
  blue = raw_input("Input a value for blue: ")
  if blue.isalpha():
    print invalid_msg
    blue = raw_input("Input a value for blue: ")
  blue = int(blue)
  if blue < 0 or blue > 255:
    print invalid_msg
    return blue

  val = (red << 16) + (green << 8) + blue
  print (hex(val)[2:]).upper()

# Code modded to give error message in case of non HEX characters being inputted by user, also different error message if the input is the wrong length

def hex_rgb():
  hex_val = raw_input("Enter a hexadecimal value: ")
  for char in hex_val:
    if char not in "0123456789abcdefABCDEF":
       print "Please enter a valid 6 digit hexadecimal value using digits 0-9 and characters A-F"
       return
    elif len(hex_val) != 6:
      print "Hexadecimal number must be 6 digits long. "
      return 

  hex_val = int(hex_val,16)

  two_hex_digits = 2**8  

  blue = hex_val % two_hex_digits
  hex_val = hex_val >> 8
  
  green = hex_val % two_hex_digits
  hex_val = hex_val >> 8

  red = hex_val % two_hex_digits
  hex_val = hex_val << 8
  
  print red,green,blue
  
def convert():
  while True:
    option = raw_input("Enter 1 to convert RGB to HEX. Enter 2 to convert HEX to RGB. Enter X to exit:")
    if option == "1":
      print "RGB to HEX..."
      rgb_hex()
    elif option == "2":
      print "HEX to RGB..."
      hex_rgb()
    elif option == "x" or option == "X":
      break
    else:
      print "Please enter either 1, 2 or x"
      
  
convert()
