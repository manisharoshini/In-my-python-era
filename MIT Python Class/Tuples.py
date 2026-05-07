# --------------------------------------------------------------
# INTRODUCTION TO TUPLES
# --------------------------------------------------------------

# tuple = () # Empty Tuple
# tuple1 = (2,)# it will consider ) as a tuple 
# # Above code tells python that this is sequence of object but there is just one object in my sequence
# print(type(tuple1)) # type of this is an tuple not the integer 

# # Multiple element tuples:
# tup1 = (2, "mit", 3)
# print(tup1[0])
# # [] -> is used to index in tuple 

# print(tup1[1:3]) # in this way we can slice tuples
# print(tup1[1:2])
# print(len(tup1)) # this gives the length of the Tuple
# print(max(2,4,7,9,3,5,8)) # this tells the maximum of the int tuples 
# tup1[1] = 4 # This is impossible coz once the tuple is created we can't modify the tuples but its differnt with lists


# tup2 = (1, "mit",3) + (6,7) # we use + sign to add extra elemnets to tuples
# print(tup2) 

# tup3 = tup1 + (4,5) # we can add extra elemnets and tuples to this in this way too
# print(tup3)

# tup4 = tup1 + tup2 + tup3 # IN this way we acn concatenate multipe tuples
# print(tup4)

