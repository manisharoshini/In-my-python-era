"""
Why use OOP and classes of Objects?
 - Mimic Real Life 
 - Group different objects part of same type

"""

# here we create animal class - will tell age and name and as per that we have to classify which animal it is. 
class Animal(object):
    def __init__(self,age):
        self.age = age
        self.name = None # later we'll create methods that we use to give names 
 # 2nd Step: We are adding __str__ to the method to change how the way we print: 
 # if we dont initialize __str__ method it will bydefault print the memory location of the object that we have created. 
    def __str__(self):
        return "Animal:" + str(self.name) + ":" + str(self.age)
 # adding getters and setters
   # -- Getters --> simple functions that will return the values of the Data attributes that this object has 
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
   # -- Setters --> same idea but here we are allowing someone using our class to set the values of these data 
    def set_age(self,newage):
        self.age = newage
    def set_name(self,newname = ""):
        self.name = newname

# Testing the objects that we create: 


# myanimal = Animal(3)
# print(myanimal)

# # -- If we do: print(myanimal.age) and print(myanimal.get_age()) both will give me same output 
# print(myanimal.age)
# print(myanimal.get_age())

# # -- setname: we have set the name using setter function and get tha using getter functions 
# myanimal.set_name("Paul")
# print(myanimal.name)
# print(myanimal.get_name())
# print(myanimal) # -- this will print all the values like Age and Name 

# # -- if we set name as an empty ones like
# myanimal.set_name()
# print(myanimal) # -- Animal::3 --> is the output coz we havent gave any name here 


"""
why do we use getters and setters? for Abstraction like --
if someone changed 
def __init__(self,age):
        self.age = age to self.years = age 
        self.name = None 
AND
def get_age(self):
        return self.age to self.years
    def get_name(self):
        return self.name

This internal changes are hidden from the outside user... so for that reason.. 
a.age --> access directly to attributes(variables) means it touches internal data directly
a.get_age()--> access only methods of the class 

-- for this reason we use getter and setter rather than accessing attributes directly -- 

CHATGPT Explanation:

So... why didn't they just write
myanimal.age = 10
Because this example is teaching encapsulation.
OOP has four major ideas:

Objects
Classes
Inheritance
Encapsulation ← This is where getters and setters come in.

Encapsulation means:
Don't let everyone directly touch your object's internal data. Instead, provide controlled methods to read or modify it.

"""