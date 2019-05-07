#! /usr/bin/env python

# Based on the single word translator.

print "Welcome to the pyg Latin translator!"
blank=""
vowels = "aeiou"
ending = "ay"
character = "qwertyuiopasdfghjklzxcvbnm1234567890"
unchanged = ["as", "to", "is", "it", "on", "and", "the", "my"]
consonants = "bcdfghjklmnpqrstvwxyz"
result = ""

def punc(i): # for punctuation errors
    global result
    if i[-1] not in character:
        first=i[0]
        restofword=i[1:len(i)-1]
        pyg_word = restofword + str("-") + first + str("ay") + str(i[-1])
        result = result + pyg_word + " "

def vow(i): # for words starting with a vowel
    global result
    if i[0] in vowels:
        result = result + i + str("-y") + ending + " "

def consonant_pair(i): # for words with 2 consonants at start
    global result, consonants
    start = i[0:2]
    rest = i[2:len(i)]
    new_word = rest + str("-") + start + ending
    result = result + new_word + " "

def others(i): # for all others
    global result
    first=i[0]
    restofword=i[1:len(i)]
    pyg_word = restofword + str("-") + first + str("ay")
    result = result + pyg_word + " "

def user(): # user interface
    phrase = raw_input("Input your phrase: ")
    phrase = phrase.lower()
    if phrase != blank:
        words = phrase.split()
        for i in words:
            if i[-1] not in character:
                punc(i)
            elif i[0] in vowels:
                vow(i)
            elif i[0] in consonants and i[1] in consonants:
                consonant_pair(i)
            else:
                others(i)
    else:
        print "You must enter a real word"
    final_result = result.replace("i-yay", "I-yay")
    print final_result # Capitalises the personal pronoun before printing

user()

# def converter():
#     phrase = raw_input("Input your phrase: ")
#     phrase = phrase.lower()
#     vowels = "aeiou"
#     ending = "ay"
#     character = "qwertyuiopasdfghjklzxcvbnm1234567890"
#     unchanged = ["as", "to", "is", "it", "on", "and", "the", "my"]
#     consonants = "bcdfghjklmnpqrstvwxyz"
#     if phrase != blank:
#         words = phrase.split()
#         result = ""
#         for i in words:
#             if i[-1] not in character:
#                 first=i[0]
#                 restofword=i[1:len(i)-1]
#                 pyg_word = restofword + str("-") + first + str("ay") + str(i[-1])
#                 result += pyg_word + " "
#             else:
#                 if i[0] in vowels:  # for words starting with a vowel
#                     result += i + str("-y") + ending + " "
#                 elif i[0] in consonants and i[1] in consonants: # consonant switch
#                     start = i[0:2]
#                     rest = i[2:len(i)]
#                     new_word = rest + str("-") + start + ending
#                     result += new_word + " "
#                 else: # for all other words
#                     first=i[0]
#                     restofword=i[1:len(i)]
#                     pyg_word = restofword + str("-") + first + str("ay")
#                     result += pyg_word + " "
#             print result
#         else:
#             print "You must enter a real word"
