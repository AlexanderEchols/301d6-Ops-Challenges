#!/bin/bash

# Script: Ops 301 Challenge 02: File Permissions
# Author: Alexander Echols
# Date of Creation 16 Mar 2023
# Date of last revision: 16 Mar 2023
# purpose: This Script will alter file permissions of everything in its directory

# main
# First we Prompt the user for an input directory path
echo "What path do you wish to alter?"
# Then we create a varible named "path" that holds the users anser on with input directory path they wish to alter
read path
# Here is where we will navigate to the path that the user gave us
cd $path
# At this stage we need to change the permissions of the files in the directory
# we will do that with the "chmod" command and the -R flag, which will make it recursive
chmod -R $newper ./
# Finally, we wil want to print the contents of the directory to the terminal in long form
# That is achieved with the "ls" command to list, then the "-l" flag to uptain long form
ls -l
# End