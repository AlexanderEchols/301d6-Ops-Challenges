#!/bin/python3
# Script: Ops 301 Class 09 Ops Challenges: Python Conditions Statements
# Author: Alexander Echols.    
# Date of creation: 23 Mar 2023                
# Date of latest revision: 23 Mar 2023.      
# Purpose: Write a Python script that uses logical statements to create a guessing game.
# Edit: the requirments are below and commented out. I am trying to create a guessing 
# game using the parameters of the ops challange

# Main
# Set age for alex
Alex = 34

# Guessing game intro
print("Hello there, I'm Alex. Want to play a game?")

# we are going to create a while true loop to play the game
while True:
    # Lets start by asking for their guess and storing it in a variable called Guess
    Guess = int(input("How old do you think I am?"))
    # create an if statement that uses Equals
    if Guess == Alex:
        print("Wow, you got it!!! Are you a Carny?")
        # we use a "break" statement to leave the loop.
        break
    # create an if statemet that uses Not Equals:
    if Guess != Alex:
        print("Bad luck, try again")
    # create an if statement that uses Less than:
    if Guess < Alex:
        print("Too low, Thank you though")
    # create an if statement that uses Less than or equal to:
    if Guess <= Alex:
        print("yes and no, Try again but try higher")

# # Define variables
# a = 55
# b = 86

# # Equals
# if a == b:
#     print("a is equal to b")
    
# # Not Equals
# if a != b:
#     print("a is not equal to b")
    
# # Less than
# if a < b:
#     print("a is less than b")
    
# # Less than or equal to
# if a <= b:
#     print("a is less than or equal to b")
    
# # Greater than
# if a > b:
#     print("a is greater than b")
    
# # Greater than or equal to
# if a >= b:
#     print("a is greater than or equal to b")
    
# # If statement using logical conditional of your choice with elif
# if a < b:
#     print("a is less than b")
# elif a > b:
#     print("a is greater than b")
# else:
#     print("a is equal to b")
    
# # If statement with both elif and else
# if a < b:
#     print("a is less than b")
# elif a > b:
#     print("a is greater than b")
# else:
#     print("a is equal to b")
