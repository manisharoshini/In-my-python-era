# # Want more accurate answer for square root 

# def bisection_root(x):
#     epsilon = 0.01
#     high = x
#     low = 0
#     guess = (low + high)/2
#     while abs(guess ** 2 - x) >= epsilon:
#         if guess**2 < x:
#             low = guess
#         else:
#             high = guess
#         guess = (low + high)/2
#     return guess
# print(bisection_root(123))

# # Making cnages in global variable is bad.
# def bisection_root(x,epsilon):
#     high = x
#     low = 0
#     guess = (low + high)/2
#     while abs(guess ** 2 - x) >= epsilon:
#         if guess**2 < x:
#             low = guess
#         else:
#             high = guess
#         guess = (low + high)/2
#     return guess
# print(bisection_root(123, 0.01))
# print(bisection_root(144,0.00001))

# # Sometimes user doesnt know what is epsilon and what's the value to put for that we have to set default parameter
# def bisection_search(x,epsilon = 0.01):
#     high = x
#     low = 0
#     guess = (high + low)/2.0
#     while abs(guess ** 2 - x) > epsilon:
#         if guess ** 2 < x:
#             low = guess
#         else:
#             high = guess
#         guess = (low + high)/2.0
#     return guess

# print(bisection_search(123))
# print(bisection_search(144,0.000001)) # here it overwrites my default parameter to the value we have given

# # -- Set of Rules for making function calls --
# print(bisection_search(123,epsilon=0.001)) # --> works fine
# print(bisection_search(x = 123,epsilon=0.001)) # --> works fine
# print(bisection_search(epsilon=0.01,x = 123)) # --> works fine

# # -- will not work --
# # print(bisection_search(epsilon=0.01,123)) # -- syntax error
# # print(bisection_search(0.001,123)) # -- will give the wrong answer

# ========================================================================================================
# # FUNCTIONS RETURNING FUNCTIONS
# def is_even(i):
#     return i % 2 == 0

# r = 2
# pi = 22/7
# my_func = is_even

# a = my_func(3)
# b = is_even(4)

# print(a,b)
# ----------------------------------------------------------

# # Functions can return functions
# def make_prod(a):
#     def g(b):
#         return a*b
#     return g 

# val = make_prod(2)(3) # -- chaining functions together 
# print(val)

# doubler = make_prod(2)
# val = doubler(3)
# print(val) # -- refer notes or screenshots for refernce 