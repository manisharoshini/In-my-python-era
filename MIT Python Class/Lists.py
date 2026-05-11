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

# total = 0
# for i in L:
#     total +=1
# print(total)

# # we can enhance it and reuse it using functions:
# def list_sum(L):
#     total = 0
#     for i in L: # i is 1 then 2 then 3 then 4 ... etc till 9 
#         total += i
#     return total

# print(list_sum([1,2,3,4,5,6,7,8,9]))

# # if in case our function takes the value of strings too

# def len_sum(L):
#     total = 0
#     for e in L: # first iterates 'ab' then 'cdef' then 'hijk'
#         total += len(e) # first it becomes 2 coz len of 'ab' is 2.. then 4 coz 'cdef' then 4 coz 'hijk'
#     return total

# print(len_sum({'ab','cdef','hijk'})) #gives 10 as a output 

# # Try it yourself: return a Tuple which has a sum of all numbers and product of all numbers

# def sum_and_prod(L):
#     (sum, prod) = (0,1)
#     for i in L:
#         sum += i
#         prod = prod * i
#     return (sum,prod)

# print(sum_and_prod([12,36,69,78,45,96,47,52,63,78,89]))