#!/bin/python3
# Script: Ops 301 Class 11 Ops Challenges 10: Python File Handling
# Author: Alexander Echols.    
# Date of creation: 27 Mar 2023                
# Date of latest revision: 27 Mar 2023
# Purpose: create a Python script to fetch info using psutil:

# Main
# we have to start by importing psutil library
import psutil

# next we start getting the information requested
# Time spent in user mode doing normal processes
User_process = psutil.cpu_times().user
# Time spent in kernel mode doing normal processes
System_process = psutil.cpu_times().system
# System Idle time
Idle_time = psutil.cpu_times().idle
# user mode priority processes time
PriPro = psutil.cpu_times().nice
# I/O completion time
IOwait = psutil.cpu_times().iowait
# Hardware service interruption time
Hardfix = psutil.cpu_times().irq
# Software service interruption time
Softfix = psutil.cpu_times().softirq
# Time spent by other operating systems running in a virtualized environment
OtherVM = psutil.cpu_times().steal
# Virtual CPU OS for guest
GuestOS = psutil.cpu_times().guest

# now we create a list with all those options
TimeList = ["User_process", "System_process", "Idle_time", "PriPro", "IOwait", "Hardfix", "Softfix", "OtherVM", "guestOS"]

# ask the user which one they want to see
print("What do you wish to look at?")
for i, option in enumerate(TimeList):
    print(f"{i+1}. {option}")

# get user input and print their choice
choice = input("Enter the number of your choice: ")
choice = int(choice)

# print the information for the chosen option
if choice == 1:
    print(f"{User_process}")
elif choice == 2:
    print(f"{System_process}")
elif choice == 3:
    print(f"{Idle_time}")
elif choice == 4:
    print(f"{PriPro}")
elif choice == 5:
    print(f"{IOwait}")
elif choice == 6:
    print(f"{Hardfix}")
elif choice == 7:
    print(f"{Softfix}")
elif choice == 8:
    print(f"{OtherVM}")
elif choice == 9:
    print(f"{GuestOS}")
else:
    print("Cmon, Chose an avalible option please.")
# End