#!/bin/bash

# Script: Ops 301 Challenge 02: Copy & Append
# Author: Alexander Echols
# Date of Creation 15 Mar 2023
# Date of last revision: 15 Mar 2023
# purpose: This Script will copy the /var/log/syslog files to the current working directory

# main
# I will start by creating a variable to hold the date & time data.
DAT=$(date + "%m-%d-%y_%H-%M-%S")
# Next we will Copy the system log file to our current working directory
cp /var/log/syslog.
# finally we will append the date and time to the system log file.
mv syslog syslog$DAT
# End