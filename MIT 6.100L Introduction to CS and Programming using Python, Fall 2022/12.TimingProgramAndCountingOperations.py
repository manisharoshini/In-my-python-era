"""
Why we care about this topic ?

Since we have to work on large data and all..
The program we write have to be correct as well as the program need to be fast. 
So -- if a program takes a year to analyze the bunch of youtube videos  -  nobody waits that long 


we are going to determine the efficincy of the program --
 
-- EFFICIENCY IS IMPORTANT --
- we can talk about time efficiency and space efficiency of the program
- There's a tradeoff between them - its very rare the program is both time and space efficient.
- Eg: We have Fibonacci Recursive. V/s Fibonacci Series Memorization
- Recursive - it wook 3M recrusion(loops) to get the output of 30. 
- In memorization - here as we calculate them we store them in memory. Here we hace given up some memory to process and store them 
- So here's a tradeoff - Program is fast and uses memory and on otherhand program is slow and not uses any memory. 

Here we are going to calculate how efficient our programs are: 
- TIme them 
- And count number of operations this programs have taken. 
- We dont calculate efficiency of implementation
- We are going to see how ro evaluate the algorithms using different implemenatation 

EVALUATING PROGRAMS
- Measure with Timer
- Count the operations
- Abstract notion of order of growth


-- ASIDE on MODULES --
A module is a set of python definations in a file
- Python provides a many useful modules: math, ploting/graphing, random sampling for probability, stats tools , many others 

You need to import module into your environment
import random 
import time 
import dateutil
import math

Call functions from inside the module uisng module name and dot notation
math.sin(math.pi/2)

"""

# TIMING A PROGRAM:
import time

def cel_to_far(c):
    return c*9.0/5 + 32

def mysum(x):
    total = 0
    for i in range(x+1):
        total += i
    return total

def square(n):
    sqsum = 0
    for i in range(n):
        for j in range(n):
            sqsum += 1
    return sqsum

# tstart = time.time() 
# cel_to_far(37)
# dt = time.time() - tstart # this gives the time from start time - end time 
# print(dt,"s,")

# Wrapper Function: 
def time_wrapper(f,L):
    print("Timing: ",f.__name__)
    for i in L:
        t = time.time()
        f(i)
        dt = time.time() - t
        print(f"{f.__name__}({i}) took {dt} seconds.. ")

L_N = [1]
for i in range(8):
    L_N.append(L_N[-1]*10)

time_wrapper(cel_to_far,L_N)
time_wrapper(mysum,L_N)
# time_wrapper(square,L_N) # this takes a lot of time to execute