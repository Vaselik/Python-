# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 14:26:00 2021

@author: vasiliki
"""

import random

with open("words.txt", "r") as f:
    word = random.choice(f.readlines()).rstrip()

tries = 5
letters = []

def hide():
    hidden = "" 
    for letter in word:
        if letter in letters:  
            hidden += letter
        else:
            hidden += "-"
    return hidden

# hidden = hide()
# print(hidden)
# letter = input("Which one? ")
# letters.append(letter)
# hidden = hide()
# print(hidden)

while tries > 0:
    hidden_word = hide()
    if hidden_word == word:
        print("Congrats")
        exit()
    
    print(hidden_word)
    letter = input("Which one? ")
    
    if letter in letters:
        print("You have tried this letter")
        continue
    letters.append(letter)
    
    if letter in word:
        print("It exists")
    else:
        print("Nope")
        tries -= 1
    letters.append(letter)

    print(f"You've got {tries} tries")
    


print("You have lost")
print(f"The word was: {word}")



