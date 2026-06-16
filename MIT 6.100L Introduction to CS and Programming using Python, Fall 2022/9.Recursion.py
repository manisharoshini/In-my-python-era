# -- Iterative ALgorithm -- 

# -- Multiplication in other way to understand loops and iterations

# -- Using For loop --
# def mult(a,b):
#     total = 0
#     for i in range(b):
#         total += a
#     return total
# print(f"The multiplication is {mult(6,7)}")

# # --Using While loop -- 
# def mult(a,b):
#     result = 0
#     while b > 0:
#         result = result + a 
#         b -= 1 # here the counter starts from zera and decreses way down to 0
#     return result
# print(mult(6,7))

# here the recursive step is a + a*(b-1) 

# -- Recursive addition : Run on python tutor for clearity 
# def mult_recur(a,b):
#     if b == 1:
#         return a 
#     else:
#         return a + mult_recur(a,b-1) # function is called inside body itself 
# print(mult_recur(4,5))
# this will create chains of function call.. 
# here we created loop by just calling function inside function body - this is called Recursion 

"""
What (Exaclty) is Recursion ?
Algorithmically: its a way to desgin solutions for problems by Divide and conquer method or we can also call it as
Decrease and conquer mehtod
-- means reduce the problem to simpler versions of same problem or problem that can be solved directly

Semantically: A programming technique where a function calls itself (with different parameter same parameter can lead to infinite recursion 

"""

# # -- Try it yourself: calculate n to the power p for variables n and p (2 base cases included one for zero and another for 1)
# def power_recur(n,p):
#     if p == 0:
#         return 1
#     elif p == 1: # not importanat this is just to show we can add 2 base functions
#         return n 
#     else: 
#         return n * power_recur(n,p-1)

# print(power_recur(6,2))

# # --  Recurisve factorial:
# def rec_fac(n):
#     if n == 1:
#         return 1
#     else:
#         return n * rec_fac(n-1)
    
# print(rec_fac(6))

"""
Each function call has its own environment.. they dont interfere in other env and even though they have same name (diff parameters)
they'll considered as different function (env)
Using same variables but they have different objects in differnt scope 
FLow control -- when we make a function call all we know is the function that we call next and who we need to give the value back upto
--
Recursion is efficient from programmer POV but not from computer POV
--
When to use recursion?
when we need to do repeated task for we dont know how deep we want to go - in this case recursive are used
Since it calls itself again and again until we reach base case 
-- 
Case: where we use recusrion
Eg: we can use it in file system for file search (here we dont know how deep the file is saved.. so we use recurisve)

Eg: Experssions - when we create our own calculator(in code) we dont know how many operations using paranthesis. 
Here we hv to go through each paranthesis until we reach base operations

"""
# ==========================================================================================================================

# -----------------------------------------------------------
# -- Lecture 16: Recursion on non numerics
# -----------------------------------------------------------

# -- fibonacci series -- 

# def fib(x):
#     if x == 1 or x == 2:
#         return 1
#     else:
#         return fib(x-1) + fib(x-2) # it calls itself twice 
    
# print(fib(6))

"""
Since in this we are recalculating the value again and agin we use more efficinet way.
We have to keep track of the data and numbers.. So we use dictionaries for that to store values
"""

def fib_efficient(n,d):
    if n in d:
        return d[n]
    else:
        
    

d = {1:1, 2:1}