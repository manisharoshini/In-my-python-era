"""

Link: https://pynative.com/python-object-oriented-programming-oop-exercise/

Exercise 1: Define an Empty Vehicle Class
Problem Statement: Write a Python program to create a class named Vehicle that has no variables or methods defined inside it.

"""
# class Vehicle:
#     pass


"""
Exercise 2: Vehicle Class with Instance Attributes
Problem Statement: Write a Python program to create a Vehicle class with two instance attributes: max_speed and mileage. 
Create an object of the class and print both attributes.

Purpose: Learn to define instance attributes using the __init__ constructor method. 
Instance attributes are unique to each object, meaning different Vehicle objects can hold different values for speed and mileage. 
This is a foundational concept in object-oriented programming.

"""
# class Vehicle(object):
#     def __init__(self,name,max_speed,mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage


# vehicle1 = Vehicle("Tesla Model S", 250, 18)
# print(f"Vehicle Name: {vehicle1.name}, its maximum speed is {vehicle1.max_speed} and its mileage is {vehicle1.mileage} ")


"""
Exercise 3: Rectangle Class with Area & Perimeter
Problem Statement: Write a Python program to create a Rectangle class with length and width as instance attributes, 
and two methods: area() that returns the area and perimeter() that returns the perimeter.

Purpose: Learn how to add instance methods to a class. Methods allow objects to perform operations using their own data, 
which is a key principle of encapsulation in OOP. Calculating geometric properties is a clean, 
practical context for understanding how self connects methods to instance data.

Given Input: rect = Rectangle(10, 4)
Expected Output: Area = 40 and Perimeter = 28

"""

# class rectangle(object):
#     def __init__(self,length,breadth):
#         self.length = length
#         self.breadth = breadth
#     def area(self):
#         return (self.length * self.breadth)
#     def perimeter(self):
#         return 2*(self.length + self.breadth)
    
# rect = rectangle(10,4)
# print(f"Area = {rect.area()} and Perimeter = {rect.perimeter()}")

# # here rect.area() --> Rectangle.area(rect)


"""
Exercise 4: Student Class with Average Grade

Problem Statement: Write a Python program to create a Student class that stores a student's name 
and a list of marks. Add a method average() that calculates and returns the average of all marks.

Purpose: This exercise shows how instance attributes can store complex data types such as lists, 
not just simple values. It also practices combining OOP with list operations and arithmetic, 
a pattern common in gradebooks, dashboards, and reporting tools.

Given Input: s1 = Student("Alice", [85, 90, 78, 92, 88])
Expected Output: Alice's Average Grade: 86.6

"""

# class Student(object):
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
#     def average(self):
#         return sum(self.marks)/len(self.marks)
    
# s1 = Student("Alice", [85, 90, 78, 92, 88])
# print(f"The name of Student is {s1.name} and the average marks of students is {s1.average()}")

"""
Exercise 5: Product Class with Stock Value Calculator
Problem Statement: Write a Python program to create a Product class with three instance attributes: name, price, and quantity. 
Add a method total_value() that returns the total stock value by multiplying price by quantity.

Purpose: This exercise models a real-world business scenario using OOP. 
It reinforces how instance methods can derive new information from existing attributes, a pattern widely 
used in inventory management, e-commerce, and financial applications.

Given Input: p1 = Product("Laptop", 899.99, 5)
Expected Output: Total stock value of Laptop: $4499.95

"""

# class Stock_calculator(object):
#     def __init__(self,name,price,quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#     def total(self):
#         return (self.price * self.quantity)

# p1 = Stock_calculator("Laptop", 899.99, 5)
# print(f"The name of the product{p1.name} and the total stock value ${p1.total()}")

"""
Exercise 6: Bank Account with Deposit & Overdraw Protection

Problem Statement: Write a Python program to create a BankAccount class with a balance attribute 
and two methods: deposit(amount) that adds funds to the balance, and withdraw(amount) that deducts 
funds but prevents the balance from going below zero.

Purpose: Learn data validation and conditional logic inside instance methods. 
Preventing overdraw is a real-world business rule, and implementing it here teaches you 
how classes can enforce constraints on their own data, a core idea behind encapsulation in OOP.

Given Input: Starting balance of 1000, deposit 500, withdraw 200, then attempt to withdraw 2000.

Expected Output:
Balance after deposit: 1500
Balance after withdrawal: 1300
Insufficient funds. Current balance: 1300

"""

# class Bank(object):
#     def __init__(self,balance):
#         self.balance = balance

#     def deposit(self,amount):
#         self.balance += amount
#         print(f"balance amount {self.balance}")

#     def withdraw(self,amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             print(f"Balance after withdrawal: {self.balance}")
#         else:
#             print(f"Insufficient funds. Current Balance: {self.balance}")
    
# account = Bank(1000)
# account.deposit(500)
# account.withdraw(200)
# account.withdraw(200)


"""
Light Class with On/Off State Toggle
Problem Statement: Write a Python program to create a Light class with three methods: 
turn_on() that switches the light on, turn_off() that switches it off, and status() 
that reports whether the light is currently on or off.

Purpose: This exercise models a simple stateful object, where the object 
remembers and changes its own condition over time. It introduces the concept 
of state management within a class, a pattern found everywhere from UI components a
nd IoT devices to game objects and workflow engines.

Given Input: Create a Light object, call turn_on(), check status(), call turn_off(), and check status() again.

Expected Output:
Light is ON
Current status: ON
Light is OFF
Current status: OFF

"""

# class Light(object):
#     def __init__(self):
#         self.is_on = False
    
#     def turn_on(self):
#         self.is_on = True
#         print("light is on !!!")

#     def turn_off(self):
#         self.is_on == False
#         print("Light is off !!")
    
#     def check_status(self):
#         if self.is_on == True:
#             state = "ON"
#         else:
#             state = "OFF"
#         print(f"Current Status {state}")


# light = Light()
# light.turn_on()
# light.check_status()
# light.turn_off()
# light.check_status()


"""
Exercise 8: User Class with Password Validation
Problem Statement: Write a Python program to create a User class that stores a username and a password. 
Add a check_password(input_password) method that returns True if the input matches the stored password,
and False otherwise.

Purpose: This exercise introduces the idea of controlled access to sensitive data inside a class. Rather
 than exposing the password directly, the class provides a dedicated method to verify it. This pattern 
 reflects a core principle of encapsulation in OOP, where internal data is protected and accessed only 
 through defined interfaces.

Given Input: u1 = User("alice", "secure123")

Expected Output:
True
False

"""

# class User(object):
#     def __init__(self,username, password):
#         self.username = username
#         self.password = password

#     def password_Validation(self,usern,passw):
#         return usern == self.username and passw == self.password

# u1 = User("alice", "secure123")
# print(u1.password_Validation("alice","secure123")) # True
# print(u1.password_Validation("alice","wrongpass")) # False
# print(u1.password_Validation("Alice","secure123")) # False

"""
Problem Statement: Write a Python program to create a Temperature class that stores a temperature in Celsius. 
Add two methods: to_fahrenheit() that converts and returns the value in Fahrenheit, and to_kelvin() that converts 
and returns the value in Kelvin.

Purpose: This exercise demonstrates how a class can act as a data container with built-in conversion logic. 
It reinforces writing multiple methods that all operate on the same instance attribute, and applies straightforward 
mathematical formulas in a practical scientific context.

Given Input: t = Temperature(100)

Expected Output:
Celsius: 100
Fahrenheit: 212.0
Kelvin: 373.15

"""
# class Temperature(object):
#     def __init__(self,celcius):
#         self.celcius = celcius
    
#     def to_kelvin(self):
#         return self.celcius + 273.15
    
#     def to_farenheit(self):
#         return (self.celcius*9/5) + 32
    
# t = Temperature(100)
# print("Celsius:", t.celcius)
# print("Fahrenheit:", t.to_farenheit())
# print("Kelvin:", t.to_kelvin())


"""
Exercise 10: Notebook Class with Add & Display Notes
Problem Statement: Write a Python program to create a Notebook class that maintains an internal list of notes. 
Add an add_note(note) method that appends a new note to the list, and a show_notes() method that prints all stored notes.

Purpose: This exercise shows how a class can manage a growing collection of data over its lifetime. 
It practices initializing a mutable data structure inside __init__ and writing methods that both modify 
and read that structure, a pattern that appears in todo lists, message queues, logs, and many other applications.

Given Input: Add three notes: "Buy groceries", "Read a book", "Call the doctor".

Expected Output:
1. Buy groceries
2. Read a book
3. Call the doctor

"""