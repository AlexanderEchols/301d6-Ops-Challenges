# Open a new file in write mode
file = open("example.txt", "w")

# Append three lines to the file
file.write("This is the first line\n")
file.write("This is the second line\n")
file.write("This is the third line\n")

# Close the file
file.close()

# Open the file in read mode
file = open("example.txt", "r")

# Read the first line of the file and print it to the screen
print(file.readline())

# Close the file
file.close()

# Delete the file
import os
os.remove("example.txt")
