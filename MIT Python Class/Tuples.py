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

# Eg of a Tuple
# seq = (2,'a',4,(1,2)) # here (1,2) is cinsidered as tuple. we can also create tuple inside tuple 
# print(len(seq))
# print(seq[3]) # will print (1,2) since its the last element and it will consider (1,2) as a single element
# print(seq[-1]) # reverse location 
# print(seq[3][0])# this is fetching elements from subtuple.. index 3 of tuple i.e(1,2) and index 0 of subtuple 0 i.e. 1 

# --------------------------------------------------------------
# Slicing of Tuple
# --------------------------------------------------------------
# seq = (2,'a',4,(1,2))
# print(seq[1])
# print(seq[-2:])
# print(seq[1:4:2])
# print(seq[:-1])
# print(seq[1:3]) # this will print from a till 4 last number is avoided

# ---------------------------------------------------------------
# Iterating over a tuple just like we iterate over string
# ----------------------------------------------------------------
seq = (2,'a',4,(1,2))
for e in seq:
    print(e) # we can iterate diredctly on indices rather than over a indeces 
    
# ============================================================
# DIFFERENCE BETWEEN STRINGS AND TUPLES IN PYTHON
# ============================================================

# ------------------------------------------------------------
# STRING
# ------------------------------------------------------------

# Definition:
# A string is an immutable sequence of characters.

# Examples:
# "Hello"
# "Python"

# Characteristics of Strings:
# 1. Ordered collection
# 2. Immutable
# 3. Supports indexing and slicing
# 4. Stores characters only
# 5. Mainly used for text processing

# ------------------------------------------------------------
# TUPLE
# ------------------------------------------------------------

# Definition:
# A tuple is an immutable ordered collection
# that can store multiple data types.

# Examples:
# (1, 2, 3)
# ("Manisha", 20, 95.5)

# Characteristics of Tuples:
# 1. Ordered collection
# 2. Immutable
# 3. Supports indexing and slicing
# 4. Can store heterogeneous data types
# 5. Used for grouped/fixed data storage

# ============================================================
# SIMILARITIES BETWEEN STRINGS AND TUPLES
# ============================================================

# 1. Both are ordered sequences
# 2. Both are immutable
# 3. Both support indexing
# 4. Both support slicing
# 5. Both are iterable
# 6. Both work with len()
# 7. Both support the 'in' operator

# ============================================================
# DIFFERENCES BETWEEN STRINGS AND TUPLES
# ============================================================

# STRING:
# - Stores characters only
# - Mainly used for text handling
# - Written inside quotes

# TUPLE:
# - Stores multiple data types
# - Used for grouping data
# - Written inside parentheses

# ============================================================
# IMPORTANT INTERVIEW POINTS
# ============================================================

# Why are strings immutable?
# - Better memory optimization
# - Faster performance
# - More secure

# Why are tuples immutable?
# - Safer for fixed data
# - Faster than lists
# - Can be used as dictionary keys

# ============================================================
# INTERVIEW DEFINITIONS
# ============================================================

# String:
# "A string is an immutable ordered sequence
# of characters used for text processing."

# Tuple:
# "A tuple is an immutable ordered collection
# capable of storing heterogeneous data types."

# ============================================================
# ONE-LINE DIFFERENCE
# ============================================================

# String  -> Immutable sequence of characters
# Tuple   -> Immutable sequence of elements/data types