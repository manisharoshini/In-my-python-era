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
def is_even_without_remiander(i):
    print("without remainder")
    remainder = i % 2
    has_rem = (remainder == 0)
    print(has_rem)
    
print(is_even_without_remiander(4))