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









# ------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------











# ------------------------------------------------------------------------------------------------------
