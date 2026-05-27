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
# # -- Example: --
# def sum_digits(s):
#     assert len(s) != 0, "s is empty"
#     total = 0
#     for char in s:
#         try:
#             val = int(char)
#             total += val
#         except:
#             raise ValueError ("String contained a Charecter.. ")
#     return total

# print(sum_digits("1234abcd")) # ValueError: String contained a Charecter.. 
# # print(sum_digits("")) # AssertionError: s is empty

# # -- Try it Yourself --

# def pairwise(Lnom, Ldeno):
#     assert len(Lnom) == len(Ldeno),'Differnt Lengths'
#     assert len(Lnom) != 0 and len(Ldeno) != 0 , 'There should be no empty List'
#     L = []
#     try:
#         for e in range(len(Lnom)):
#             L.append(Lnom[e]/Ldeno[e])
#     except:
#         raise ValueError ("There's a string in the element")
#     return L

# # -- Uncomment one by one to get the correct answer or else the program will halt --
# # L1 = [1,2,3,4,6]
# # L2 = [1,5,6,7]
# # print(pairwise(L1,L2)) # AssertionError: Differnt Lengths

# # L1 = []
# # L2 = []
# # print(pairwise(L1,L2)) # AssertionError: There should be no empty List

# # L1 = [1,2,'a']
# # L2 = [0,5,4]
# # print(pairwise(L1,L2)) # ValueError: There's a string in the element

# # L1 = [1,2,3]
# # L2 = [4,5,6]
# # print(pairwise(L1,L2)) # [0.25, 0.4, 0.5]

# ---------------------------------------------------------------------------------------------------
# -- Another Example --
def get_stats(class_list):
    new_stats =[]
    for stu in class_list:
        new_stats.append([stu[0],stu[1],avg(stu[1])]) # here the avg is another function 
    return new_stats

def avg(grades):
    try:
        return sum(grades)/len(grades)
    except ZeroDivisionError: # if the code enters Except block there's no return statement so it will return None. 
        print("Warning No Grade Data")
        return 0.0 # if we want answer in the form of number we can return 0.0 

print(get_stats([[['peter','parker'],[80.0,70.0,56.0]], 
                 [['Bruce','Wayne'],[75.0,100.0,78.0]],
                 [['Juliana','Paulius'],[100.0,90.0,95.0]],
                 [['Blacky'],[]]
                 ]))
"""
This is the output of above Code 

Warning No Grade Data
[[['peter', 'parker'], [80.0, 70.0, 56.0], 68.66666666666667], 
[['Bruce', 'Wayne'], [75.0, 100.0, 78.0], 84.33333333333333], 
[['Juliana', 'Paulius'], [100.0, 90.0, 95.0], 95.0], [['Blacky'], [], None]]
"""

# -- Same Example - Another Method 

def get_stats(class_list):
    new_stats =[]
    for stu in class_list:
        new_stats.append([stu[0],stu[1],avg(stu[1])]) # here the avg is another function 
    return new_stats

def avg(grades):
    assert len(grades) != 0, "no Grades data"

print(get_stats([[['peter','parker'],[80.0,70.0,56.0]], 
                 [['Bruce','Wayne'],[75.0,100.0,78.0]],
                 [['Juliana','Paulius'],[100.0,90.0,95.0]],
                 [['Blacky'],[]]
                 ]))

# ---------------------------------------------------------------------------------------------------
