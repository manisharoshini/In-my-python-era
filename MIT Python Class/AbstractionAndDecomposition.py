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

# even function without remainder 
# def is_even_without_remiander(i):
#     print("without remainder")
#     remainder = i % 2
#     has_rem = (remainder == 0)
#     print(has_rem)
    
# print(is_even_without_remiander(4))

# you Try it

# def add(x,y):
#     return x + y

# def mult(x,y):
#     print(x*y)

# print(add(3,4))
# mult(3,4) # since the print statement is in the function itself 
# print(mult(4,5))# print 20 and NONE here entire function calls become none !! so it will become print(None) --> mult(4,5) becomes None 
# # return only has value inside the function 

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


# Bisection search using Functions:
def bisection_root(x):
    epsilon = 0.01
    low = 0
    high = x
    ans = (high + low)/2
    while abs(ans**2 - x) > epsilon:
        if ans**2 < x:
            low = ans
        else:
            high = ans
        ans = (high + low)/2
    return ans 

# print(bisection_root(4))
# print(bisection_root(123))

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

def count_nums_with_sqr_root_close_to(n, epsilon):
    count = 0
    for i in range(n ** 3): # This means ur checking from n to 1000 
        sqrt = bisection_root(i) # take the square root 
        if abs(n - sqrt) < epsilon:
            count += 1
            print(i, sqrt)
    return count

print(count_nums_with_sqr_root_close_to(10, 0.1))