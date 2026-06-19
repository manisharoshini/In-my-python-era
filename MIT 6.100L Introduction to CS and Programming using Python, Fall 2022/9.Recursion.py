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
# # ==========================================================================================================================

# # -----------------------------------------------------------
# # -- Lecture 16: Recursion on non numerics
# # -----------------------------------------------------------

# # -- fibonacci series -- 

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

# def fib_efficient(n,d): # memorized fibonacci series solution 
#     if n in d:
#         return d[n] 
#     else:
#         ans = fib_efficient(n-1,d) + fib_efficient(n-2,d)
#         d[n] = ans
#         print(d[n]) # for my convenience
#     return ans

# d = {1:1, 2:1}
# print(fib_efficient(7,d))
# print(fib_efficient(34,d)) # -- here in upper code it will make 11 million calls for functions
# # but in efficent one there's only 65 calls made
# # the 1st code stores nothing but it is slow.. BUt efficeint algo stores things uses memory and is fast

# # here it will check for repeated calculations if it found it will use that and there's no need to solve again 
# # mo need to calculate just check the dictionary dict 

# # ---------------------------------------------------------------------------------------------------------------==
# # -- Try It Yourslef: Returns all ways to make a score of x by adding 1,2 and/or 3 together. Order doesnt matter ..

# def score_count(x):
#     if x == 1:
#         return 1
#     elif x == 2:
#         return 2
#     elif x == 3:
#         return 3
#     else:
#         return score_count(x-1) + score_count(x-2) + score_count(x-3)
    
# print(score_count(10)) # try using efiicinet method 

# # ---------------------------------------------------------------------------------------------------------------
# # SUM OF LIST NUMBERS

# # Lists can have other list inside it other lists (nested list can be at any level deep)
# # Iteration is possible only till certain ;evel and its hard
# # Instead we can use recursive method - no matter how deep the nested list goes.. we can work using repeated steps


# #  -- Normal Method 
# def total_iter(L):
#     result = 0
#     for i in L:
#         result += i
#     return result

# print(total_iter([10,20,30,40,50]))

# # -- Recursive Method 
# def total_recur(L):
#     if L == 0:
#         return 0
#     elif len(L) == 1:
#         return L[0]
#     else:
#         return L[0] + total_recur(L[1:])

# print(total_recur([10,20,30,40,50]))

# # -- Try it yourself --
# # Modify the code we wrote to return the total length of all strings in L 

# def total_len_recur(L):
#     if len(L) == 1:
#         return len(L[0])
#     else:
#         return len(L[0]) + total_len_recur(L[1:])
# print(total_len_recur(["ab","cd","efgh"]))
# # the normal one is more efficient as compared to this.. this has repeated fuction calls
# # Uing build in ones are more efficient rather than this one 

# # ---------------------------------------------------------------------------------------------------------------

# # Looking for an element in the list 
# # Base Case - len of element 1 is the same element we are looking for 
# def in_list(L,e):
#     print(e,L) # -- to check exactly whats going on loop 
#     if len(L) == e:
#         return L[0] == e
#     else:
#         if L[0] == e:
#             return True
#         return in_list(L[1:],e)

# test = [2,8,4,1]
# print(in_list(test,1)) # -- returns True

# tes = [2,1,5,8]
# print(in_list(tes,1)) # -- returns False coz the above code is checking only the last element is the element we are looking for 
# # it is not looking the first element or somethinggg only comparing the last element with the element we needed 
# # extracts first element but dosent do anything 

# # -- improved way to write it in more pythonic way:
# def improve_inlist(L,e):
#     if len(L) == e:
#         return False
#     elif L[0] == e:
#         return True
#     else:
#         return improve_inlist(L[1:],e)

# test = [2,8,4,1]
# print(improve_inlist(test,1)) # -- returns True

# tes = [2,1,5,8]
# print(improve_inlist(tes,1)) # --returns True 

