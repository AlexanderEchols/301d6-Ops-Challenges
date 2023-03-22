#!/usr/bin/python3
# Script: Ops 301 Class 05 Ops Challenges: Creating Directory.
# Author: Alexander Echols.    
# Date of creation: 21 Mar 2023                
# Date of latest revision: 21 Mar 2023.
# Purpose: Create a script 

# Main
# import os library
import os

# first we create a function to fetch and print all the directories,
# sub-directories, and files for a given directory path
def fetch(path):
    # create a for loop that will use the os.walk() method to iterate
    # over all the needed files.
    for dirpath, dirnames, filenames in os.walk(path):
        # we are going to use a directed for loop to create all the directories
        for dirname in dirnames:
            # here we actually create said directories
            os.makedirs(os.path.join(dirpath, dirname))

        # we liked it before. we are gonna use it again.
        # here is another nested for loop 
        for filename in filenames:
            # command to create an empty file for each file name. 
            open(os.path.join(dirpath, filename), 'w').close()
    # lets print a varification of success
    print("Good News! your directory structure was successfully created")


# Lets prompt the user to select their directory path
path = input("What directory path do you wish to see? ")

# we are going to use an if statement here to check if the chosen directory exists
if not os.path.exists(path):
    # if it doesn't exist, we need to let them know.
    print("Invalid directory path.")
else:
    # call the fetch function we created on line 14.
    fetch(path)