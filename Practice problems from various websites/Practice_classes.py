"""
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
#     def __init__(self,)