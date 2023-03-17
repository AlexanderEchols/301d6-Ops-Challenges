#!/bin/bash

# Script: Ops 301 Challenge 03: using condional statments in a meny system
# Author: Alexander Echols
# Date of Creation 16 Mar 2023
# Date of last revision: 16 Mar 2023
# purpose: This script will generate a menu and then output based off the users selection

# main
# First step is to create a meny system with some options to choose
menu="Do any of these meet your fancy? if so please do chose a number. if none of it interests you, please chose number 4"
# now we set the options the user can choose
select choice in Hellow-world Ping-Self IP-info Exit
do
    # Here is where we will build our table of options
    # T
    case $choice in
        Hello-world)
            echo "Hello World"
            ;;
    # Lets set the Ping option
        Ping-Self)
            ping -c5 127.0.0.1
            ;;
    # Now we want to set the IP info choice
        IP-info)
            ip a
            ;;
    # Finally the Exit choice.
        Exit)
            echo "Good Bye, Do come back now"
            break
            ;;
    *)
        echo "Choose a number 1-4"
        ;;
    esac
done
# End