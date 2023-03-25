#!/bin/python3
# Script: Ops 301 Class 09 Ops Challenges: Python File Handling
# Author: Alexander Echols.    
# Date of creation: 24 Mar 2023                
# Date of latest revision: 25 Mar 2023.      
# Purpose: Write a Python script that uses logical statements to create a guessing game.

# # Main

# we will create a new file in write mode 
Newfile = open("WhoDis.txt", "w")

# Then we need to append three lines to the file
# First
Newfile.write("One is the lonelest number that you'll ever do'\n")
# Second
Newfile.write("Two can be as bad as one, it's the loneliest number sinch the number one\n")
# Third
Newfile.write("And three is just a crowd. There was no line in the song with three\n")

# Now we need to close the file
Newfile.close()

# Re-open it in read mode
Newfile = open("WhoDis.txt", "r")

# Read the first line of the file, then print it to the screen
print(Newfile.readline())

# Close the file
Newfile.close()

# Delete the file
import os
os.remove("WhoDis.txt")
# end