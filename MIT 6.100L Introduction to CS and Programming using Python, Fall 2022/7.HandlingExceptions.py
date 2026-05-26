# # --- Normal code ---
# def sum_digits(s):
#     total = 0
#     for char in s:
#         if char in '0123456789':
#             val = int(char)
#             total += val
#     return total

# print(sum_digits("1234"))
# print(sum_digits("abcd9082j"))

# # -- using Try and Except block -- 
# def sum_digits_except(s):
#     total = 0
#     for char in s:
#         try:
#             val = int(char)
#             total += val
#         except:
#             print("Cant convert ",char)
#     return total

# print(sum_digits_except("1234"))
# print(sum_digits_except("1234abcdefg"))

# # ------------------------------------------------------------------------------------------------------------
# # --- Another Example ---
# a = int(input("Enter a Number: "))
# b = int(input("Enter another number: "))
# print(a/b) # when we take inputs from user.. its very unpredicatble so for that we can use try and except block 

# # -- With Try and Except --
# try:
#     a = int(input("Enter a Number: "))
#     b = int(input("Enter another number: "))
#     print(a/b)
# except:
#     print("Assole can't you follow the rules properly !!")

# # ----------------------------------------------------------------------------------------------------------------
# # Handling Specific Exceptions
# try:
#     a = int(input("Enter a number: "))
#     b = int(input("Enter a number: "))
#     print("a/b = ",a/b)
#     print("a+b = ", a+b)
# except ValueError: # executes only if this error occurs
#     print("Dont behave like a dumb ass !! ")
# except ZeroDivisionError: # executes only if this error occurs
#     print("You cant be this dumbbb.. coz even kid knows anything divide by 0 is infinity")
#     print("a+b = ", a+b)
# except: # executes for all kind of errors 
#     print("Wtf is wrong with u !!!!")
# else:  # executes when try block sucessfully gets executed
#     print("Sucess")
# finally: # executes even though the code runs except ot anyother block 
#     print("Everything is perfect !!")

# # ----------------------------------------------------------------------------------------------------------------
# # -- to raise our own errors or exceptions --
# def sum_digits(s):
#     total = 0
#     for char in s:
#         try:
#             val = int(char)
#             total += val
#         except:
#             raise ValueError("String has Charecter ") # we can raise eour own ValueError and halt the execution
#     return total

# print(sum_digits("123abcdef"))  

# # -- Try it yourself --
"""
2 list Lnom and Ldeno of equal lengths -- returns new list whose elements are pairwise 
division of an Lnum by an element in Ldeom -- 
-- Raise Value error if Ldeno contains zero
"""

# def pairwise_div(Lnum,Ldeno):
#     L = []
#     # other way
#     if 0 in Ldeno:
#         raise ValueError("Zeroo ! wtf !! dont be dumbass !!!")
#     try:
#         for i in range(len(Lnum)): # here i is the index i is 0,1,2,3..
#             L.append(Lnum[i]/Ldeno[i])
#     except:
#         raise ValueError("Are u aware of the rule right then why the fuck are u doing the same man !!!")
#     return L 

# # L1 = [1,2,3]
# # L2 = [4,5,6]
# # print(pairwise_div(L1,L2))

# L1 = [1,2,3]
# L2 = [4,0,6]
# print(pairwise_div(L1,L2))

# ============================================================================================
# -- Assertions -- (Defensive Programming Tool)

"""
A contract between the one who uses the function and the one who creates the function
assert <statement that should be True>, "message if not True" 

"""
# -- Example: --
def sum_digits(s):
    assert len(s) != 0, "s is empty"
    total = 0
    for char in s:
        try:
            val = int(char)
            total += val
        except:
            raise ValueError ("String contained a Charecter.. ")
    return total

print(sum_digits("1234abcd")) # ValueError: String contained a Charecter.. 
# print(sum_digits("")) # AssertionError: s is empty
