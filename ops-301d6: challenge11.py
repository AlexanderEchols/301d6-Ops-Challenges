#!/bin/python3
# Script: Ops 301 Class 12 Ops Challenges 11: Python Requests Library
# Author: Alexander Echols.    
# Date of creation: 28 Mar 2023                
# Date of latest revision: 28 Mar 2023
# Purpose: create a Python script that utilizes HTTP requests

# Main
# first we need to import the requests library
import requests
# Ask the user what url they wish to learn about
Dest = input("where you going, enter the URL: ")
# Ask the user to choose which GET method to use
method = input("What can i GET you? (please choose GET, POST, PUT, DELETE, HEAD, PATCH, OPTIONS)")
# Next we want to let the user know what they chose 
print(f"you chose {method} {Dest}..")
YouSure = input("Sure you wanna do this bra? (y/n)")

# create the dictionary of the top 10 HTTP status codes
StatusCodes = {
           200: 'All gravy, This is what success looks like',
           301: 'we moved, new site who dis',
           302: 'Temp redirect, This is a summer home',
           304: 'Not Modified, we got caching here',
           400: 'Bad Request, maybe check the URL',
           401: 'Unauthorized Error, we lost too',
           403: 'Forbidden, I understand what you want, but that don"t mean you get it',
           404: 'Not Found, are you sure you know what you are looking for?',
           500: 'Internal Server Error, This is on them',
           501: 'Not Implemente, I don"t understand what you want' 
        }
# And and ask them to varify.
if YouSure.lower() == "y":
    confirm = requests.request(method, Dest)
    print("\nResponse Header Info:\n")
    for key, value in confirm.headers.items():
        if key.lower() == 'content-type':
            print(f"{key}: {value}")
        else:
            status_text = StatusCodes.get(confirm.status_code,"Unknown status code, we are working on updating the dictionary.")
            print(f"{key}: {value} ({status_text})")
#END