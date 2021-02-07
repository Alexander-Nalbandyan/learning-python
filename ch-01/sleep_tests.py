# imports specific named function from module so that we don't need to use dot syntax for calling it.
# from time import sleep

# the other more common format is to just import module without importing specific function in such case we need to use
# module.functionName to call a function.
import time

# Sleeps current thread for given number of second. It is floating number to be able to specify subsecond part.
time.sleep(0.900)
