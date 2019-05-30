#! /usr/bin/env python

# This translator only works for single words. See pyglatin_phrase for improved version

print("Welcome to the pyg Latin translator!")
blank = ""
word = input("Give me a word: ")

if word != blank and word.isalpha():
    first = word[0]
    restofword = word[1:len(word)]
    print(restofword+first+str("ay"))
else:
    print("You must enter a real word")
