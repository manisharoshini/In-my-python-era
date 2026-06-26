# # ---------------------------------------------------------------------------------------------------------------
"""
*** OBJECT ORIENTED PROGRAMMING ***

the idea of OOP since everything in python is objects we use object oriented programming. 
We can CREATE, MANIPULATE and even DESTROY objects in python

Data Absrtaction - captures internal representations and interface for interacting with objects. 
1. through methods and 
2. defines behavior and hides implementation. 

How lists are represented internally ? -- inside the notes --

How to interface with lists, manipulate lists ? 
-- L[i]m L[i:j],
len(), max(), min(), del(), 
append(), extend(), count(), index(), insert(), pop(), remove(), reverse(), sort()

Real life Examples: 

1. Elevator - changes floors
2. Employee - a person who works in a company
3. Queue at Store - First customer to arrive is the first person to serve (FIFO)
4. Stack of Pancakes - first pancake made is last one to be eaten (LIFO)

The idea of OOP -- here we are bundelling the data and the behavior in one thing 
They are going to be consistent in data we represent them and consistent in the way that we use them

YPU WRITE CLASS BEACUSE YOU MAKE DESIGN DECISIONS. - here we decide what data represents the class and you decide 
what behaviors represent the class.

"""
# # refer notebook notes for more clear notes.
# class Cordinate:
#     def __init__(self,xval,yval):
#         self.x = xval
#         self.y = yval

# c = Cordinate(3,4) # here 3 is xval and 4 is yval and the self becomes Cordinate(3,4) we have created (also this becomes an object)
# origin = Cordinate(0,0)

# print(c.x) # this will grab the value of x from the "c" variable. 
# print(origin.x)  # this will grab the value of x from the "origin" variable.

# a = 1
# orig = Cordinate(a,a)
# print(orig.x)

"""
Note: (c.x) is possible if we declare self.x and self.y in the function or else it will just be the variables that will soon 
becomes useless (or just variables) as soon as the function gets terminated 

To persist x and y throughout the object we define self.x and self.y

Suppose you write:
p1 = Coordinate(3,5)

Python secretly does:
self = p1
xval = 3
yval = 5

Then executes:
self.x = xval
self.y = yval

which becomes:
p1.x = 3
p1.y = 5


"""
# # ---------------------------------------------------------------------------------------------------------------

"""
What is method ?
method is just a function that works with this class (or we can say its own class or we can say object of its type).

To create method in python we just pass the 'self' as first parameter 

self - is the one whoever called the method.

"""
# Define a method for coordinate class and going to calculate the distance

class Cordinate:
    def __init__(self,xval,yval):
        self.x = xval
        self.y = yval
    def distance(self,other): # works only with the class type cordinate we use 'self' here
        x_diff_sq = (self.x - other.x) ** 2
        y_diff_sq = (self.y - other.y) ** 2
        return (x_diff_sq+y_diff_sq) ** 0.5
    
c = Cordinate(3,4)
orig = Cordinate(0,0)

print(Cordinate.distance(c,orig))
print(c.distance(orig)) # similar to mylist.append(5)
