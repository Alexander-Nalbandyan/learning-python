# There is no main method in python it runs the code from top to bottom


# from $module_name import $submodule_name
import datetime

# Returns today date in triple format where components can be accessed by .day,.month, .year
today_date = datetime.date.today()

# Also we can get it formatted in yyyy-mm-dd using datetime.date.isoformat() function.


# os module provides system independent functions to interact with underlying operating system
# related functions makeup a module, there are many modules in standard library e.g. os, datetime, json, random etc.
from os import getcwd

# in case if we are going to use just attributes from module them we can write import $module_name, or we can import the whole module
# this way and then access needed functions by os.getcwd
# sys module provides platform information e.g. platform i.e. linux, macos etc. or version(which version of python we are running).
import sys

# os.environ returns all environment variables of underlying operating system.


import time

# converts time to string with provided formatting if the second argument is not provided then localTime() gets formatted.
time.strftime('%H:%M')

import html

# html module contains some utility functions for working with html like escape() and unescape()

# this is a diffinition of a list in python.
# usually statements in python are one line but there are some exceptions from this.
# in case of list python interpreter will look for matching ] for end of list so list can cover multi line.
# so to define list all you need to do is put x = [y, z, u, ....] that's it.
# all operations which can be done with lists will be covered later.
odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21,
        23, 25, 27, 29, 31, 33, 35, 37, 39,
        41, 43, 45, 47, 49, 51, 53, 55, 57, 59]

# variables in python are dinamically assigned so there is no specific variable definition it starts existing after assigning value
# to a variable and the type it gets is from the value it gets assigned.
# also variable can get different values during execution of the program.


# The below statement calls today() method which returns time object and then we access specific time attribute with dot notation.
right_this_minute = datetime.datetime.today().minute

print(right_this_minute)

# returns working directory path.
print(getcwd())

# In operator checks whether item given on the left is from the list given in the right and returns True in such case otherwise returns False.
# if operator execute the block after it if the predicate returns true otherwise executes else block if it is False
# if predicate:
#    block of code with identation
# else:
#    block of code.
# block is also refered by Suite which more commonly used Term among Python developers.
# So blocks use identation and they usual start with colon(:)
if right_this_minute in odds:
# if don't put identation for Suite then python gives an error.
    print("This minute seems little odd")
else:
    print("Not an odd minute")

today = "Saturday"
condition = "headache"
if today == "Saturday":
    print("Party")
# We can have as many elif's as we want but they should stand after if and before else.
# identation levels are counted from left to right starting from 0. The no idetation is level 0 then goes 1, 2, 3 ...
elif today == "Sunday":
    if condition == "headache":
        print("Recover")
    else:
        print("Rest")
elif today == "Friday":
    print("Ban Chmnac")
else:
    print("Work work work !!!")
