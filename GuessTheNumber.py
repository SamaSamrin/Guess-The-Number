# -*- coding: utf-8 -*-
"""
Created on Fri Dec 31 22:15:18 2021

@author: SamaSamrin
"""

import random

# computer generates a number and the user tries to guess it correctly
def guess_computer(limit):
    def guess_computer(number):
    guess = 0;
    while guess!=number:
        guess = int(input("Enter your guess:"))
        if guess<number:
            print("Too low")
        elif guess>number:
            print("Too high")
    print("Congrats! That's correct!")

#user provides a number and the computer tries to guess it correctly
def guess_user(number):
    high = 100
    low = 0
    user_feedback = ''
    while user_feedback != 'c':
        computer_guess = random.randint(low, high)
        print("I have guessed", computer_guess)
        print("Enter l if my guess is lower than your number.\nEnter h if my guess is higher than your number.\nEnter c if it is correct.")
        user_feedback = input('Type: ')
        user_feedback = user_feedback.lower()
        #print(user_feedback)
        if user_feedback=='h':
            high=computer_guess
        elif user_feedback=='l':
            low=computer_guess
    print("Correct!")

#Trying to guess the number computer provided
computer_input = random.randint(1, 100)
guess_computer(computer_input)

#Computer trying to guess the number the user provided
user_input = input("Enter a number for the computer to guess\n")
guess_user(user_input)
