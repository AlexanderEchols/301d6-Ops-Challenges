#!/bin/python3
# Script: Ops 301 Class 05 Ops Challenges: Bash in Python
# Author: Alexander Echols.    
# Date of creation: 20 Mar 2023                
# Date of latest revision: 20 Mar 2023.      
# Purpose: Write a Python script that will execute some bash commands.

# we start by import os
import os
# then we create a welcome message
print("Hey there, Hi there, Ho there!!!")

# we must create variable to hold the name of the PC we are using.
weare = 'whoami'
# now we are going to print the name to the screen, 
# we use the "+" symbol to combine these two together
print("my name is ") 
os.system (weare)

# here we will create a variable to hold the ip address of the PC
ourip = 'ip a'
print("I  can be found at ")
os.system (ourip)

# the final bit of info we want is a short list of the hardware configurations,
# we can do that by creating a variable to the command "lshw -short" lshw will 
# get us the info and the "-short flag" will shorten it so as not to overwhelm us
short = 'sudo lshw -short'
print("Here is all the info")
os.system (short)