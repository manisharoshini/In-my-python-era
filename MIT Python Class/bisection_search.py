"""
========================================
⚡ Square Root Approximation Methods
========================================
Includes:
1. Approximation Method (Incremental Guessing)
2. Bisection Search (Efficient Method)
3. Handling Edge Case (x < 1)
4. Combined Final Solution
========================================
"""


# --------------------------------------
# 🔹 Approximation Method   
# --------------------------------------

# x = 54321

# epsilon = 0.01
# we took 0.01 coz thats the level of significance we want.
# (lets change it to 1 --> we got a perfect answer which is 233.0
# but we want to get the answer which is close to the square root of x
# and not the perfect answer. so we will take 0.01 as our epsilon value.)

# num_guess = 0
# guess = 0.0

# increment = 0.0001
# this is 0.0001 beacuse we do not want to skip the best answer.
# if we take 0.01 then we will skip the answer which is 232.9089
# and we will get 232.91 which is not correct.

# while abs(guess**2 - x) >= epsilon and guess**2 <= x:
#     guess += increment
#     num_guess += 1

# print("Number of guesses = " , num_guess)
# print(f'the last guess is {guess} and the square of the last guess is {guess**2}')

# if abs(guess**2 - x) >= epsilon:
#     # exited the loop beacuse making further guesses are unreasonable.
#     print("Failed on square root of x: ", x)
# else:
#     # guess is close enough to the square root of x.
#     print(guess, "is close to square root of x: ", x)

# NOTE:
# here we can also change the increement to 0.00001
# it will take longer time
# 1 step from old = 10 steps from new,
# code didnt failed it got a perfect answer !!
# but the issue here is optimization


# --------------------------------------
# 🔹 Bisection Search (Fast Square Root)
# --------------------------------------

# x = 54321

# if we tried 0.5 we will enter an infinite loop
# because the square of 0.5 is 0.25 which is less than 0.01
# and we will never exit the loop.

# epsilon = 0.01
# num_guesses = 0
# low = 0
# high = x
# guess = (high + low)/2.0

# while abs(guess ** 2 - x) >= epsilon:
#     if guess ** 2 < x:
#         low = guess
#     else:
#         high = guess
#     guess = (high + low)/2.0
#     num_guesses += 1

# print("Number of guesses = ", num_guesses)
# print(guess, "is close to square root of ", x)


# --------------------------------------
# 🔹 Fix for Case: x < 1
# --------------------------------------

# we need to fix the code so that it can handle the case when x is less than 1.

# x = 0.5
# epsilon = 0.01

# low = x
# high = 1.0

# guess = (high + low)/2.0

# while abs(guess ** 2 - x) >= epsilon:
#     if guess ** 2 < x:
#         low = guess
#     else:
#         high = guess
#     guess = (high + low)/2.0

# print(guess, "is close to square root of ", x)


# --------------------------------------
# 🔹 Final Combined Solution ✅
# --------------------------------------

# x = float(input("Enter a number: "))
# epsilon = 0.01

# if x >= 1:
#     low = 1.0
#     high = x
# else:
#     # here we can also take low = 0.0
#     # but we will take low = x because we know that
#     # the square root of x will be greater than x if x is less than 1.
#     low = x
#     high = 1.0

# guess = (high + low)/2.0

# while abs(guess ** 2 - x) >= epsilon:
#     print(f'low = {low}, high = {high}, guess = {guess}')
#     if guess ** 2 < x:
#         low = guess
#     else:
#         high = guess
#     guess = (high + low)/2.0

# print(guess, "is close to square root of ", x)

# # Bisection on cube roots (you try it yourself !!)

# cube = 27
# epsilon = 0.01
# low = 0
# high = cube
# guess = (high + low)/2.0

# while abs(guess**3 -cube) >= epsilon:
#     if guess**3 < cube:
#         low = guess
#     else:
#         high = guess
#     guess = (high + low)/2.0 # if we dont do this this will get into an infinite loop.  
# print(f'{guess} is close to the cube root of {cube}')

# Newton - Raphson method 
# epsilon = 0.01
# k = 24.0 # try 54321
# num_guesses = 0
# guess = k/2.0 # we can start with any guess but we will start with k/2.0 because we know that the square root of k will be less than k/2.0 if k is greater than 1.

# while abs(guess ** 2 -k) >= epsilon:
#     num_guesses += 1
#     guess = guess - (((guess ** 2) - k)/(2 * guess)) # (guess ** 2) - k) -> f(guess) and (2 * guess) -> f'(guess)
# print(f'{guess} is close to the square root of {k}')
# print(f'number of guesses = {num_guesses}')

# Assume you are given an integer 0 <= N <= 1000. Write a piece of Python code that uses bisection search to
# guess N. the code prints two lines: count: with how many guesses it took to find N, and answer: with the
# value of N. Hints: If the halfway value is exactly in between two integers, choose the smaller one

epsilon = 0.01
N = int(input("Enter an integer between 0 and 1000: "))
low = 0
high = 1000
guess = (high + low) /2
guesses = 0
while abs(guess - N) >= epsilon:
    guesses +=1
    if guess < N:
        low = guess
    else:
        high = 1000
print(f'{guess} is close to the square root of {k}')
print(f'number of guesses = {guesses}')