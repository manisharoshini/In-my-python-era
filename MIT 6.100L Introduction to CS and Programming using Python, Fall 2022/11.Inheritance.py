"""
Why use OOP and classes of Objects?
 - Mimic Real Life 
 - Group different objects part of same type

"""

# # here we create animal class - will tell age and name and as per that we have to classify which animal it is. 
# class Animal(object):
#     def __init__(self,age):
#         self.age = age
#         self.name = None # later we'll create methods that we use to give names 
#  # 2nd Step: We are adding __str__ to the method to change how the way we print: 
#  # if we dont initialize __str__ method it will bydefault print the memory location of the object that we have created. 
#     def __str__(self):
#         return "Animal:" + str(self.name) + ":" + str(self.age)
#  # adding getters and setters
#    # -- Getters --> simple functions that will return the values of the Data attributes that this object has 
#     def get_age(self):
#         return self.age
#     def get_name(self):
#         return self.name
#    # -- Setters --> same idea but here we are allowing someone using our class to set the values of these data 
#     def set_age(self,newage):
#         self.age = newage
#     def set_name(self,newname = ""):
#         self.name = newname

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
------------------------

Python is not good at hiding things:
a.age --> access data outside the class
a.age = 'infinte' --> modify it to the any type from outside the class. (we can set it to any data type which can cause risk) 
     if we give age = "twenty four" and outside people will give age = 24 it will create a major risk 
a.sise --> allow u to create attribute for an instance from outside the class..
BECAUSE OF ALL THIS WE CAN RISK THE CODE 

"""

# # --------------------------------------------------------------------------------------------------------------------
"""
Create a new class it should be the dictionary of any kind of elements and will select only non negative ints
and the dictionary should map each one of these numbers (ie keys) to the Animal objects with the ages ie Animal(6) or Animal(7)

here the dictionary should have keys that is ints and values should be Animal object like 

2:Animal(2) --> in this way 

"""
# class Animal(object):
#     def __init__(self,age):
#         self.age = age
#         self.name = None # later we'll create methods that we use to give names 
#  # 2nd Step: We are adding __str__ to the method to change how the way we print: 
#  # if we dont initialize __str__ method it will bydefault print the memory location of the object that we have created. 
#     def __str__(self):
#         return "Animal:" + str(self.name) + ":" + str(self.age)
#  # adding getters and setters
#    # -- Getters --> simple functions that will return the values of the Data attributes that this object has 
#     def get_age(self):
#         return self.age
#     def get_name(self):
#         return self.name
#    # -- Setters --> same idea but here we are allowing someone using our class to set the values of these data 
#     def set_age(self,newage):
#         self.age = newage
#     def set_name(self,newname = ""):
#         self.name = newname

# # here we are checking if the list has only int values (no negative or string values are allowed)
# # -- Adding it to "d" dictionary
# def animal_dict(L):
#     d = {}
#     for n in L:
#         if type(n) == int and n >= 0:
#             d[n] = Animal(n)
#             # here means d[0] -- means the key of dict 
#             # animal[0] -- means the value of dic
#     return d

# L = [2,3,-5,'a',0]
# animals = animal_dict(L)
# # print(animals) # -- this doesnt print recursively it just prints the top level thing (knows to print integers doesnt know to print the dictionaries)
# for n,a in animals.items():
#     print(f"Key {n} and the value {a}")
#     # -- here we are running print on key and value seperately..  

# # -- Try it Yourself -- 
# # L1 --> list of ints and L2 --> list of str.. L1 and L2 are of same length. Creates a list of Animals of same length as L1 and L2
# # An animal object at index i has the age and name correspondingly to same index in L1 and L2, respectively

# def make_animals(l1,l2):
#     l3 = []
#     for i in range(len(l1)):
#         # i is 0,1,2,3.. prolly the index (not values)
#         age = l1[i]
#         name = l2[i]
#         a = Animal(age)
#         a.set_name(name)
#         l3.append(a)

#     return l3

# l1 = [2,3,4]
# l2 = ["blobfish","jellyfish","goldfish"]
# fish = make_animals(l1,l2)

# for i in fish:
#     print(f"{i}")

# # --------------------------------------------------------------------------------------------------------------------
"""
INHERITANCE: 
This will have a base class Animal and 3 subclass - Rabbit, cat, person (with different behaviour and information)
and Person class will have overriding behavior (aka subclass) named Student 
"(All Students are persons but not all persons are students)"
Student will say "i have homeowrk" or "My fav subject is Maths" but not all persons have Homework.. 
Only the category of students have HOMEWORKS

person will have 
more info --> list of friends (whereas other class ie.Cat and rabbit don't have friends )
more behaviour --> Ability to speak (Cat and Human has but rabbit doesn't)
Ability to speak for differnt class: 
    Human --> "Hello"
    Cat --> "Meow"

"""

class Animal(object):
    def __init__(self,age):
        self.age = age
        self.name = None
    
    def get_age(self):
        return self.age
    def set_age(self,newage):
        self.age = newage
    
    def get_name(self):
        return self.name
    def set_name(self,newname = ""):
        self.name = newname
    
    def __str__(self):
        return "animal: "+ str(self.name)+ " : " + str(self.age)
    
class Cat(Animal): # -- inherits all the attributes(behaviors) of parent class Animal
    def speak(self):
        print("meow")
    def __str__(self):
        return "Cat:" + str(self.name)+ ":" + str(self.age)
    # here like python goes into animal class --> copying everything thats in animal class --> pasting it in the cat class 
    # here we dont have any __init__ inside the class so it uses parentclass init method
    # parent class is a python object so the child class is also an python object 
    # the parent class has age and name attributes --> all these attributes are passed to cat class also

# print("------cat animal test----------")
# c = Cat(5)
# c.set_name("Fluffy")
# print(c) #--> Cat:Fluffy:5
# c.speak() # --> "meow" as output

# print(c.get_age()) # --> will print 5
# a = Animal(4)
# a.speak() # --> This will throw an error coz we dont have speak() method in cat class not in animal class 

class Person(Animal):
    def __init__(self,name,age):
        Animal.__init__(self,age) # -- line means "Initialize everything that belongs to an Animal."
        # this goes to animal class and calls self.age = age from parent class instead of doing it on children's class 
        # instead of rewriting we simply called it from parent class.. if we made any chnages in parent class it will be easy !! or else we have to 
        # change it again in children class
        self.set_name(name)
        self.friends = []
    
    def get_friends(self):
        return self.friends.copy()
    def add_friends(self,fname):
        if fname not in self.friends:
            self.friends.append(fname)
    def speak(self):
        print(f"Hello !!!! I'm {self.name}")
    def age_diff(self,other):
        diff = self.age - other.age
        print(f"Year Difference is {abs(diff)}")
    def __str__(self):
        return "person:" + str(self.name) + ":" + str(self.age)

"""Rule to remember
self.age = age → initializes only one attribute.
Animal.__init__(self, age) → runs all the initialization code inside the parent class."""

# -- Testers --
p1 = Person("Jack",23)
p2 = Person("Jill", 22)

print(p1)

print(p1.get_name())
print(p1.get_age())
print(p2.get_name())
print(p2.get_age())

p1.speak() # if i add print statement i'll get the output as well as the None value 
p2.speak() 

p1.age_diff(p2)

p1.add_friends('Bobby')
p1.add_friends('Brianna')
p2.add_friends('Brianna')
p2.add_friends('Bobby')

print(p1.get_friends())
print(p2.get_friends()) # we can have mutual friends too in this 
