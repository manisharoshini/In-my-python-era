# # Functions:

# def is_even(i):
#     # Input I --> Takes the int Value
#     # Returns True if Even else False
#     if i % 2 == 0:
#         return True
#     else:
#         return False
    
# print(is_even(3))
# print(is_even1(6))
#---------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------
# # Try it yourself 
# def div_by(n,d):
#     r = n/d
#     return r

# print(div_by(10,5))

# def div_by(n,d):
#     if n%d == 0:
#         return True
#     else:
#         return False
# print(div_by(10,5))
#---------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------
# Use of functions in a complex code 
# This will print Numbers between 1 to 10 and tell us whether its even or odd

# # improved version of above code is:
# def is_even1(i):
#     return i % 2 == 0

# for i in range(1,101):
#     if is_even1(i):
#         print(i, "even")
#     else:
#         print(i, "odd")
#---------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------
# Suppose we want to add all the odd integers between a and b including a and b 

# # using for loop 

# def sum_odd(a,b):
#     sum_of_odd = 0
#     for i in range(a, b+1):
#         if i % 2 != 0:
#             sum_of_odd += i   # here we added the number instead of increementing, if we want the count we use += 1 or if we want the total of all we use +=i the value itself
#             print(i, sum_of_odd)
#     return sum_of_odd

# print(sum_odd(2,4))
#---------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------
# Using while loop

# def sum_odd(a,b):
#     sum_of_odd = 0
#     i = a
#     while i <= b :
#         if i%2 != 0:
#             sum_of_odd += i # here we added the number instead of increementing, if we want the count we use += 1 or if we want the total of all we use +=i the value itself
#             print(i,sum_of_odd)
#         i+=1
#     return sum_of_odd
# print(sum_odd(2,1000))
#---------------------------------------------------------------------------------------------------

# Try it Yourslef

# Ques: Write a code that satisfies the following specs:
# s is a string returns TRUE if palindrome else return FALSE eg: 2222 - TRUE Eg: abc - FALSE


# ------------------------------------------
# Functions as Objects
# ------------------------------------------

# even fuction that has return statement 
# def is_even_with_return(i):
#     print("with return")
#     remainder = i % 2
#     return remainder == 0

# print(is_even_with_return(5))
#---------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------
# even function without remainder 
# def is_even_without_remiander(i):
#     print("without remainder")
#     remainder = i % 2
#     has_rem = (remainder == 0)
#     print(has_rem)
    
# print(is_even_without_remiander(4))
#---------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------
# you Try it

# def add(x,y):
#     return x + y

# def mult(x,y):
#     print(x*y)

# print(add(3,4))
# mult(3,4) # since the print statement is in the function itself 
# print(mult(4,5))# print 20 and NONE here entire function calls become none !! so it will become print(None) --> mult(4,5) becomes None 
# # return only has value inside the function 
#---------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------
# Try it yourself: Triangular Number 

# def is_triangular(n):
#     total = 0
#     for i in range(n + 1):
#         total += i
#         if total == n:
#             return True
#     return False
                   
#     #         print(True) ] trial and error.. 
#     # print(False)        ]  initially used print frunction then used return function
            
# print(is_triangular(4))
#---------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------
# # Bisection search using Functions:
# def bisection_root(x):
#     epsilon = 0.01
#     low = 0
#     high = x
#     ans = (high + low)/2
#     while abs(ans**2 - x) > epsilon:
#         if ans**2 < x:
#             low = ans
#         else:
#             high = ans
#         ans = (high + low)/2
#     return ans 

# print(bisection_root(4))
# print(bisection_root(123))
#---------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------
# epsilon is the level of error whuch is acceotable or else it goes to infinite loop    
# ---------------------------------------------------------------------------------------------
# Try it Yourself
# calculate all the values which is close to the the n and epsilon
# Eg:
# 1. sqrt 99 is 9.94969401
# 2. sqrt of 100 is 9.9998474
# 3. sqrt of 101 is 10.0497589111
# 4. sqrt of 102 is 10.0994567871
# ---------------------------------------------------------------------------------------------

# def count_nums_with_sqr_root_close_to(n, epsilon):
#     count = 0
#     for i in range(n ** 3): # This means ur checking from n to 1000 
#         sqrt = bisection_root(i) # take the square root 
#         if abs(n - sqrt) < epsilon:
#             count += 1
#             print(i, sqrt)
#     return count

# print(count_nums_with_sqr_root_close_to(10, 0.1))

# ---------------------------------------
# Function Scope
# ---------------------------------------
#---------------------------------------------------------------------------------------------------
# Example 1: 

# def f(y):
#     x = 1
#     x+=1
#     print(x)

# x = 5
# f(x) # this will create new environment called function envrionment and runs the opertaions in the function 
# # since there is no return value it will return None 
# print(x) # will print the x-> value in the global environment
#---------------------------------------------------------------------------------------------------
# # Example 2:
# def g(x):
#     print(x) # since there is no x in the function we can cehck outside the function scope if it has x value we can use it.
#     print(x + 1) # this will simply calculate and print it and doesnt modify any value 
    
# x = 5
# g(x)
# print(x)
#---------------------------------------------------------------------------------------------------
# # Example 3: Error or Faulty code
# def h(y):
#     x += 1 # it thinks you are trying to create x inside h and add 1 to x 
#     # we have not assigned anything "x=" inside the 
#     # Thats y we get error "local variable is referenced before assignment"
    
# x = 5
# h(x)
# print(x)

# THIS TELLS THAT YOU CAN ACCESS VARIABLE OUTSEIDE THE FUNC BUT YOU CANT CHANGE THE VARIBALE
#---------------------------------------------------------------------------------------------------
# ---------------------------------------------
# Functions as Arguments
# ---------------------------------------------

# def is_even(i):
#     return i % 2 == 0

# my_func = is_even # here giving another name to same function.. its not a function call
# # in memory both my_func and is_even refer to the same code (by diff names)
# a = my_func(4)
# b = is_even(6)
# print(a,b)

# --------------------------------
#Function as parameter
# ---------------------------------

# def calc(op, x, y):
#     return op(x,y)

# def add(a,b):
#     return a + b

# def div(a,b):
#     if b!=0:
#         return a/b 
#     print("Denominator is 0")


# print(calc(add,2,2))
#---------------------------------------------------------------------------------------------------
# Try it Yourself 

# def calc(op,x,y):
#     return op(x,y)

# def div(a,b):
#     if b!=0:
#         return a/b
#     print("Denominator cant be Zero")
    
# res = calc(div,4,0) # here it will return None !! 
# print(res) 
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------
# Another Example of Function to understand the workings of function
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
# def func_a():
#     print("Inside Function A")
    
# def func_b(y):
#     print("Inside function B")
#     return y

# def func_c(f,z):
#     print("Inside Function c")
#     return f(z)

# print(func_a())
# print(5 + func_b(2))
# print(func_c(func_b, 3)) # here func_c(f,c) --> func_c(func_b,3)
# # return f(z) --> f-> func_b and z-> 3 so it becomes func_b(3)
#---------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------
# Try it Yourself 
# def apply(crieteria,n): # here one of the parameter(crieteria) is function and another one is an integer from this we conclude that functions are objects
#     count = 0
#     for i in range(n+1):
#         if crieteria(i): count +=1
#     return count
        
# def is_even(x):
#     return x%2 == 0

# def is_five(x):
#     return x%5 == 0

# how_many = apply(is_even,10) # here we just replaced crieteria with is_even function 
# print(how_many)
# # here crieteria is just a rule i apply to a function... the thing is we can add any crieteris to it.

# print(apply(is_five,10)) # another one just for Trail sake 

# # -------------------------------------------------------------
# # Lambda Functions (Anonymus Function):
# # -------------------------------------------------------------
# def apply(crieteria,n): # here one of the parameter(crieteria) is function and another one is an integer from this we conclude that functions are objects
#     count = 0
#     for i in range(n+1):
#         if crieteria(i): count +=1
#     return count

# how_many_evens = apply(lambda x: x % 2==0,10)# here we used Lambda function instead of actual Function 
# how_many_fives = apply(lambda x: x % 5==0,50)

# print("Divisible of 2:",how_many_evens)
# print("Divisible of 5:",how_many_fives)
#---------------------------------------------------------------------------------------------------

# # Also we can do
# print((lambda x:x%2 == 0)(258)) # this will return "True" 
# #if we want to reuse it we have to copy Paste it to new line (lambda function is just for one time use)
#---------------------------------------------------------------------------------------------------
# #Try yourself:
# def do_twice(n,fn):
#     return fn(fn(n))

# print(do_twice(3, lambda x:x**2))
# # initially fn(fn(n)) --> fn(fn(3)) --> fn(3) is 9 (returns 9)--> fn(9) --> returns 81 
# # this returns 81 to the main function and ends the func envirnoment

#---------------------------------------------------------------------------------------------------