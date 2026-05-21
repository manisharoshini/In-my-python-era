# [] -> for list
# a_list = [] # ---> This is an empty lists

# --------------------------
# Indices and Ordering 
# --------------------------
# L = [2,'a',4,[1,2]]
# print([1,2] + [3,4]) # ---> this evaluates [1,2,3,4]
# print(len(L)) # --> This evaluates 4
# print(L[0]) # ---> evaluates 2 since indexing starts from 0
# print(L[2] + 1) # --> this evaluates 4 + 1 ie 5
# print(L[3]) # --> evaluates [1,2] ie another list
# print(L[4]) # --> this will give an error since its out of range 
# i = 2
# print(L[i - 1]) # this gives an output 'a'. since L[1] --> a 
# print(max([2,3,4,5,6,7]))

# ----------------------------------------------------------------------
# Iterating over Lists
# ----------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------
# total = 0
# for i in L:
#     total +=1
# print(total)
#---------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------
# # we can enhance it and reuse it using functions:
# def list_sum(L):
#     total = 0
#     for i in L: # i is 1 then 2 then 3 then 4 ... etc till 9 
#         total += i
#     return total

# print(list_sum([1,2,3,4,5,6,7,8,9]))
#---------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------
# # if in case our function takes the value of strings too

# def len_sum(L):
#     total = 0
#     for e in L: # first iterates 'ab' then 'cdef' then 'hijk'
#         total += len(e) # first it becomes 2 coz len of 'ab' is 2.. then 4 coz 'cdef' then 4 coz 'hijk'
#     return total

# print(len_sum({'ab','cdef','hijk'})) #gives 10 as a output 
#---------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------
# # Try it yourself: return a Tuple which has a sum of all numbers and product of all numbers

# def sum_and_prod(L):
#     (sum, prod) = (0,1)
#     for i in L:
#         sum += i
#         prod = prod * i
#     return (sum,prod)

# print(sum_and_prod([12,36,69,78,45,96,47,52,63,78,89]))
#---------------------------------------------------------------------------------------------------

# ====================================================================
# IDEA OF MUTABILITY
# ====================================================================

# L = [2,'a',4,[1,2]]
# L[3] = 10 # This will replace the element at indice 3 (ie [1,2]) to 10
# in tuple if we want to replace items we have to create an entire new tuple for that (old tuple still there but we lost the binding)

# --------------------------------
# OPERATIONS ON LISTS
# --------------------------------
# append(element) - used to add the element at end of the list
# l = [2,1,3]
# l.append(5) 
# print(l)
# # if we do l = l.append(5) --> it will return None (in this we do mutation and return result as None)

# # if we want to append L two times . we can do 
# l = [2,1,3]
# l.append(5) 
# l.append(5)
# print(l)

#---------------------------------------------------------------------------------------------------
# # Try it yourself:
# l1 = ['ma']
# l2 = ['ni']
# l3 = ['sha']
# l4 = l1 + l2
# print(l4)
# l3.append(l4)
# print(l3)
# l = l1.append(l3) 
# print(l) # --> this will print None since the data is stored in l1
# print(l1) # l1 will have all the data and L will return None 
#---------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------
# # Try it Yourself 
# def make_ordered_list(n):
#     list_name = []
#     for i in range(0,n+1): # we can also use "for i in range(n+1)" coz loop defaults the zero
#         list_name.append(i)
#     return list_name
# print(make_ordered_list(10))
#---------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------
# # Try it yourself: Remove the element from the list which is equal to e
# def remove_elem(L,e):
#     my_list = []
#     for i in L:
#         if i != e: # if i not in e --> this statement is only used for strings
#             my_list.append(i)
#     return my_list

# L = [1,2,2,2]
# print(remove_elem(L, 2)) # [1]

# L = [1,2,2,2]
# print(remove_elem(L,1)) # [2, 2, 2]

# L = [1,2,2,2]
# print(remove_elem(L,0)) # [1, 2, 2, 2]

# # Expln: i = 1 Loop becomes i != 2 --> TRUE so it will append to new list
# # i = 2 loop becomes 2 != 2 --> FALSE condition becomes false and gets rejected 
# ------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------
# # We can convert String to LIst and vice versa
# s = "Jesus Loves You"
# L = list(s)
# print(L) # ['J', 'e', 's', 'u', 's', ' ', 'L', 'o', 'v', 'e', 's', ' ', 'Y', 'o', 'u']
# ------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------
# # Take an input string and split it to a particular charecter
# s = "Jesus Loves You"
# L1 = s.split(" ")
# print(L1) # ['Jesus', 'Loves', 'You']

# L2 = s.split("L")
# print(L2) # ['Jesus ', 'oves You'] --> will remove L
# ------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------
# # Lists to Strings - Use 'join()' to join the lists

# L = ['J','e','s','u','s']
# A = ''.join(L) # --> This means nothing in between
# print(A)

# B = ' '.join(L) # --> Means Space in between
# print(B)

# C = '_'.join(L) # --> means underscore in between
# print(C)

# # D = ''.join([1,2,3]) # --> This will not work coz join works only on String elements not the int ones
# # print(D)

# E = ''.join(['1','2','3']) # --> here number is in the ''(quotes) it will treat as a string.. and join
# print(E) # --> 123 is the output 
# ------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------
# # My logic(Wothout lists)
# def count_words(sen):
#     space = 0
#     for i in sen:
#         if i == " ":
#             space += 1 
#     return space+1

# print(count_words("Hello its me Hi I'm the problem"))

# # Given code: (with lists)
# def count_words(sen):
#     l1 = sen.split(' ')
#     return len(l1)

# print(count_words("Hello its me Hi I'm the problem"))

# ------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------
#  Few opertions for lists 

# # sort() --> this will sort and mutate(change) the L without storing original ones
# L = [4,2,7]
# L.sort()
# print(L) # L is the list of sorted one the original L is not stored

# # reverse() --> This will reverse the list and muatate(change) the L without storing original ones
# L = [2,5,3,1,8]
# L.reverse() # this will just reverse the list and the original L is replaced with the reverse L
# print(L) # [8, 1, 3, 5, 2]

# # sorted() --> this will maintain the original ones and return the sorted version of L (no mutation or changes)
# L = [5,2,7,8,1]
# L_new = sorted(L)
# print(L_new)
# print(L) # this maintains the original L 
# ------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------
# # Try it Yourself (My Logic)
# def sort_words(sen):
#     s1 = sen.split(" ")
#     sorted_words = sorted(s1)
#     return sorted_words

# print(sort_words("Its me Hii Im the problem"))

# # Given solution
# def sort_words(sen):
#     l = sen.split(" ")
#     l.sort()
#     return l

# print(sort_words("Its me Hii Im the problem"))

# # Other solution (More Precise solution)
# def sort_words(sen):
#     L = sen.split(" ")
#     return sorted(L)

# print(sort_words("Its me Hii Im the problem"))

# ------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------
# Enumerate () --> learn yourself

# # Example - square ervery element in the list, mutating original List
# def square_list(L):
#     for i in range(len(L)): # here we loop over indices rather than elemnets in the list
#         L[i] = L[i] ** 2 # by suing this [] we can get each elements in the list and square it
        
# # here we choose to work on indices rather than element coz if we iterate elements we'll get typeError
# # "'list' object cannot be interpreted as an integer" --> this is the error...
# # here there is no return statement if we use A = sqaure_list(Lin) --> print(A) will become None coz the value returns None 

# Lin = [2,3,4]
# print("Before Function call: ", Lin)
# square_list(Lin)
# print("After Function Call: ", Lin)

# ------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------
# # combining Operations in the list
# L1 = [1,2,3,4]
# L2 = [5,6,7,8,9]
# L3 = L1 + L2

# print(L3) # here L1 and L2 remian unchanged in the memory

# # Extend() operations
# l1 = [1,2,3,4]
# l1.extend([0,6])
# print(l1) # this will mutate l1 and add new elements and extend it by 2 elements at the end 

# l2 = [4,5,6,7]
# l2.extend([[1,2,3],[4,5,6,7]]) # this are the bunch of the parts of elements as list
# print(l2)

# ------------------------------------------------------------------------------------------------------
# L =[1,2,3,4]
# for e in L: # there's no infinity loop coz 'e' binding is still in old L ie L = [1,2,3,4]
#     L = L+L 
#     print(L)
# """
# [1, 2, 3, 4, 1, 2, 3, 4]
# [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
# [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
# [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
# """
# ------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------
# L = [4,5,6]
# print(id(L)) # --> will store in same memory location (just mutated)
# L.append(80)
# print(id(L)) # --> will store in same memory location (just mutated)
# L.clear()
# print(id(L)) # --> will store in same memory location (just mutated)
# L = []
# print(id(L)) # --> will store in new memory location (new list is created here and L lost binfing from old one to new one)
# # id() --> this tells the memory location whether the alterted(mutated) data is stored in same location or different location

# =============================================================================================================================================================================
# LEC 11 :  ALIASING AND CLONING (Lists)

# ------------------------------------------------------------------------------------------------------
# # Copy of a list to new list 
# L = [1,2,3,4]
# Lnew = L[:]
# print(L)
# print(Lnew)
# ------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------
# Try it yourself : mutate to all elements in L that are equals to e returns None
# Here's a twist we hv to store in same memory.. so first make a copy of the original list and then store it 

# def remove_all(L,e):
#     Lcopy = L[:] # here we make a copy of L
#     L.clear() # Clear all the elements in the L
#     for i in Lcopy: # iterate through the Lcopy rather than original L
#         if i != e: # check conditions 
#             L.append(i) # append to original List

# L = [1,2,3,4] # in this there's no need of return function
# remove_all(L,2) 
# print(L)
# ------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------
# # Other Operations on List: Remove
# # here we remove specific functions of List instead of removing the entire list(using clear())
# # 1. delete function

# L = [1,2,3,4,5,6,7,8,9]
# del(L[5]) # will remove the element at specific index 
# print(L) # [1, 2, 3, 4, 5, 7, 8, 9]

# # 2. Using pop() function -  has return value (will return the value that we pop)
# L.pop(3) # will remove element at index 3
# print(L) # [1, 2, 3, 5, 7, 8, 9]

# L.pop() # this will remove last element of the list 
# print(L) # [1, 2, 3, 5, 7, 8]

# # we can save the return value in a variable 
# a = L.pop() # this will mutate L and store the removed value in the variable a.
# print(L) # [1, 2, 3, 5, 7]
# print(a) # 8

# # 3. Remove Function 
# L.remove(2) # this will remove the element L in the list 
# print(L) # [1, 3, 5, 7]

# ------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------
# # Try it yourself : mutate to all elements in L that are equals to e returns None
# # Here's a twist we hv to store in same memory.. so first make a copy of the original list and then store it 
# # (This time use any of above 3 functions)

# # using While loop
# def remove_all(L,e):
#     while e in L:
#         L.remove(e)
    
#     return L

# L = [1,2,2,3] # in this there's no need of return function
# remove_all(L,2) 
# print(L)

# # using For Loop
# def remove_all(L,e):
#     for ele in L:
#         if ele == e:
#             L.remove(e)
    
#     return L

# L = [1,2,2,3] # in this there's no need of return function
# remove_all(L,2) 
# print(L) # Incorrecly prints [1, 2] WHILE LOOP WORKS PROPERLY HERE 

# # Why ? coz if we use remove it will remove and shift towards forward.. and pointer goes ahead 
# # [1,2,2,3] --> it will remove 2 and [2,3] shifts forward and the for loop pointer moves forward to 3 
# # pointer at 1 [1,2,2,3]
# # pointer at 2 removes 2 [1,2,3] 2nd 2 is removed here and indices shift happens here 
# # pointer at 3 for loop will not realize that the shift happened and  points to next element

"""
------------------------------------------------------------
EXAMPLE
------------------------------------------------------------

L = [1,2,2,3]

Expected Output:
[1,3]

Actual Output:
[1,2,3]

------------------------------------------------------------
WHY DOES THIS HAPPEN?
------------------------------------------------------------

The issue happens because:

1. FOR LOOP uses an internal pointer/index
2. remove() changes the list size dynamically
3. Elements shift left after removal
4. FOR LOOP pointer moves forward anyway
5. One element gets skipped accidentally

------------------------------------------------------------
STEP-BY-STEP VISUALIZATION
------------------------------------------------------------

Initial List:

Index:   0   1   2   3
        ----------------
L =     [1,  2,  2,  3]

Pointer starts at index 0

------------------------------------------------------------
ITERATION 1
------------------------------------------------------------

Pointer at:
1

Is 1 == 2 ?
NO

Move pointer forward

------------------------------------------------------------
ITERATION 2
------------------------------------------------------------

Pointer at:
2

Is 2 == 2 ?
YES

remove(2) executes

List becomes:

Index:   0   1   2
        -------------
L =     [1,  2,  3]

IMPORTANT:
The SECOND 2 shifted LEFT

BEFORE:
[1, 2, 2, 3]

AFTER:
[1, 2, 3]
     ↑
shifted here

------------------------------------------------------------
MAIN PROBLEM
------------------------------------------------------------

The FOR LOOP pointer already moves forward automatically.

It now jumps to NEXT index.

Pointer goes to:
3

The shifted 2 gets SKIPPED completely.

------------------------------------------------------------
FINAL RESULT
------------------------------------------------------------

Output becomes:

[1,2,3]

instead of:

[1,3]

------------------------------------------------------------
WHY WHILE LOOP WORKS
------------------------------------------------------------

WHILE LOOP gives manual control over index movement.

You can:

- remove element
- stay at SAME index
- recheck shifted element properly

Therefore:

No elements get skipped.

------------------------------------------------------------
KEY LEARNING
------------------------------------------------------------

NEVER modify a list while iterating over it using:

    for element in list

because:

- list indices shift
- pointer movement becomes incorrect
- elements may get skipped

Safe approaches:

1. Use WHILE LOOP
2. Iterate over COPY of list
3. Create NEW filtered list

============================================================

"""
# ------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------
# TRICKY EXAMPLE
# Mutate L1 to remove any duplicates in L2 