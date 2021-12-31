# -*- coding: utf-8 -*-
"""
Created on Fri Dec 31 22:15:18 2021

@author: SamaSamrin
"""

import random

print("GUESS THE NUMBER!!")
number = random.randint(1,10)

guess = 0;
for i in range(11):
    guess = int(input("Enter your guess:"))
    print(10-i, "tries left")
    if guess==number:
        print("Congrats! You guessed it right!")
        break
if i==10:
    print("The number was", number)