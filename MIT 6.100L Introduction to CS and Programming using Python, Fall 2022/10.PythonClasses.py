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
# # Define a method for coordinate class and going to calculate the distance

# class Cordinate:
#     def __init__(self,xval,yval):
#         self.x = xval
#         self.y = yval
#     def distance(self,other): # works only with the class type cordinate we use 'self' here
#         # Returns eucdian distance between two coord objects 
#         x_diff_sq = (self.x - other.x) ** 2
#         y_diff_sq = (self.y - other.y) ** 2
#         return (x_diff_sq+y_diff_sq) ** 0.5
    
# c = Cordinate(3,4)
# orig = Cordinate(0,0)

# print(Cordinate.distance(c,orig))
# print(c.distance(orig)) # similar to mylist.append(5)

# ===============================================================================================================
# Lec 18: More Python Classes Methods 
# ===============================================================================================================

# class Cordinate:
#     def __init__(self,xval,yval):
#         self.x = xval
#         self.y = yval
#     def distance(self,other): # works only with the class type cordinate we use 'self' here
#         # Returns eucdian distance between two coord objects 
#         x_diff_sq = (self.x - other.x) ** 2
#         y_diff_sq = (self.y - other.y) ** 2
#         return (x_diff_sq+y_diff_sq) ** 0.5
#     def to_origin(self):
#         self.x = 0
#         self.y = 0
# c = Cordinate(3,4)
# origin = Cordinate(0,0)

# print(f"c's x-cord is {c.x} and origin's x-cord is {origin.x}  ")
# print(c.distance(origin))

# c.to_origin()
# print(c.x,c.y)

# # ---------------------------------------------------------------------------------------------------------------
# # USING CLASSES TO BUILD OTHER CLASSES 

# # Example: use coordinates to build cirle 
# # Hint: here the centre is a cordinate so we here make use of cordinate class to make a complex class 

# # -- You try it: 
# # Add a code to init method to check that type of center is obj and type of radius is int if not then raise ValueError 

# class Cordinate:
#     def __init__(self,xval,yval):
#         self.x = xval
#         self.y = yval
#     def distance(self,other): # works only with the class type cordinate we use 'self' here
#         # Returns eucdian distance between two coord objects 
#         x_diff_sq = (self.x - other.x) ** 2
#         y_diff_sq = (self.y - other.y) ** 2
#         return (x_diff_sq+y_diff_sq) ** 0.5
#     def to_origin(self):
#         self.x = 0
#         self.y = 0

# class Circle(object):
#     def __init__(self, center, radius):
#         if type(center) != Cordinate or type(radius) != int:
#             raise ValueError
#         self.center = center
#         self.radius = radius
    
# center = Cordinate(2,2)
# my_circle = Circle(center,2)

# my_circle = Circle(2,2)
# my_circle = Circle(center, 'two')

# # ---------------------------------------------------------------------------------------------------------------
# # Circle Class: defination and instances 

# # This will calculate the distance of point from center of circle, 
# # if its greater than the radius -- the point is outside the circle else its inside the circle

# class Cordinate:
#     def __init__(self,xval,yval):
#         self.x = xval
#         self.y = yval
#     def distance(self,other): # works only with the class type cordinate we use 'self' here
#         # Returns eucdian distance between two coord objects 
#         x_diff_sq = (self.x - other.x) ** 2
#         y_diff_sq = (self.y - other.y) ** 2
#         return (x_diff_sq+y_diff_sq) ** 0.5
#     def to_origin(self):
#         self.x = 0
#         self.y = 0

# class Circle(object):
#     def __init__(self, center, radius):
#         # if type(center) != Cordinate or type(radius) != int:
#         #     raise ValueError
#         self.center = center # here its a cordinate object 
#         self.radius = radius # here its an int 
#     def is_inside(self,point):
#         return point.distance(self.center) < self.radius
#     def is_inside2(self,point):
#         return (self.center).distance(point) <self.radius # -- here this means it doesnt really care in which cordinate it runs on !!
    
# center = Cordinate(2,2)
# my_circle = Circle(center,2)

# p = Cordinate(1,1)
# print(my_circle.is_inside(p))

# # ---------------------------------------------------------------------------------------------------------------
# # Create a new type to represent fraction:
# # Internal representation of two integers Numerator and Denominator 
# # Methods to interact with Fractions are -- Add, Subtract and invert 

# class SimpleFraction(object):
#     def __init__(self,n,d):
#         self.num = n
#         self.denom = d

#     def multiply(self,oth):
#         top = self.num * oth.num
#         bottom = self.denom*oth.denom
#         return top/bottom
    
#     def addition(self,other):
#         top = (self.num*other.denom) + (self.denom*other.num)
#         bottom = self.denom*other.denom
#         return top/bottom
    
#     def get_inverse(self):
#         return 1/(self.num/self.denom)
    
#     def invert(self):
#         # temp = self.num
#         # self.num = self.denom
#         # self.denom = temp
#         # other way:
#         (self.num,self.denom) = (self.denom,self.num)
#         pass

# f1 = SimpleFraction(3,4)
# f2 = SimpleFraction(1,4)

# print(f"The invert of f1 and f2 is {f1.invert()} and {f2.invert()}") # The invert of f1 and f2 is 0.75 and 0.25
# print(f"The inverse value of f1 and f2 is {f1.get_inverse()} and {f2.get_inverse()}") # The inverse value of f1 and f2 is 1.3333333333333333 and 4.0

# print("----Perfrom Invert function: -----")
# print(f"Initially num = {f1.num} and denom = {f1.denom}")
# f1.invert()
# print(f"After Inverting Num and denom, our new num = {f1.num} and new denom = {f1.denom}")

# print(f"the numerator and denominator of F1 fraction is {f1.num} and {f1.denom}") # the numerator and denominator of F1 fraction is 3 and 4
# print(f"the numerator and denominator of F1 fraction is {f2.num} and {f2.denom}") # the numerator and denominator of F1 fraction is 1 and 4

# print(f"Addition of f1 and f2 = {f1.addition(f2)}") # Addition of f1 and f2 = 1.0
# print(f"Multiplication of f1 and f2 = {f1.multiply(f2)}") # Multiplication of f1 and f2 = 0.1875

"""
dunder methods:
* + len() print() all are shorthand methods
behind the scenes the code runs dunder methods as listed to run or perform the operations 
__add__(self, other)      →    self + other
__sub__(self, other)      →    self - other
__mul__(self, other)      →    self * other
__truediv__(self, other)  →    self / other
__eq__(self, other)       →    self == other
__lt__(self, other)       →    self < other
__len__(self)             →    len(self)
__str__(self)             →    print(self)
__float__(self)           →    float(self)  i.e. cast
__pow__(self, other)      →    self ** other

Eg: 
a + b ie

10 + 20
Python secretly does 10.__add__(20) similary for all the shorthand functions  

"""

# # ---------------------------------------------------------------------------------------------------------------
# # -- Defining our own print methods 
# class Cordinate(object):
#     def __init__(self,xval,yval):
#         self.x = xval
#         self.y = yval
#     def distance(self,other):
#         x_diff_sq = (self.x - other.x)**2
#         y_diff_sq = (self.y - other.y)**2
#         return (x_diff_sq + y_diff_sq)*0.5
#     def __str__(self): # __str__ is a name of special method 
#         return "<"+str(self.x)+","+str(self.y)+">"
    
# cor = Cordinate(3,4)
# origin = Cordinate(2,2)
# print(cor.distance(origin))

# # -- check whether __str__ is working or not 
# print(f"This is the way that we wanted python to code the string (manipulating __str__): {cor}")
# print(origin)
# print(f"Here the type of object cor is {type(cor)}, ie the name of the class we have created in")

# print(f"The type of cordinate class is {type(Cordinate)},ie we are defining a new type in the python thats y its type is 'type' ")

# print(isinstance(cor,Cordinate)) # another way to check the type of the class 

# # ---------------------------------------------------------------------------------------------------------------
# # Example: Fractions with Dunder methods (To make better fractions method)
