"""
Practice Problem: Write a script to perform the following three operations on given list

Access the third element of a list
List Length: Print the total number of items
Check if the list is empty

"""
# numbers = [10, 20, 30, 40, 50]
# print(f"Third Element: {numbers[3]}")
# print(f"Length of the list: {len(numbers)}")
# is_empty = len(numbers) ==0
# print(f"IS the list is empty? {is_empty}")

"""
Exercise 2. Perform List Manipulation
Practice Problem: Take a given list and modify it through five specific actions:

Change Element: Change the second element of a list to 200 and print the updated list.
Append Element: Add 600 o the end of a list and print the new list.
Insert Element: Insert 300 at the third position (index 2) of a list and print the result.
Remove Element (by value): Remove 600 from the list and print the list.
Remove Element (by index): Remove the element at index 0 from the list print the list.
Exercise Purpose: Python lists are mutable, meaning they can be changed after they are created. This exercise demonstrates the various ways to “reshape” your data dynamically during execution.
"""

# Initial_list =[100, 50, 400, 500]
# Initial_list[1] = 200
# print(f"Updated List at 2nd place {Initial_list}")
# Initial_list.append(600)
# print(f"Appended List = {Initial_list}")
# Initial_list.insert(2,300)  
# print(f"Updated Insert: {Initial_list}")
# Initial_list.remove(600)
# print(f"Initial List: {Initial_list}")
# Initial_list.pop(4)
# print(f"Initial List: {Initial_list}")

"""
Exercise 3. Sum and Average of All Numbers in a List
Practice Problem: Calculate the total sum of all integers in a list and find the arithmetic mean (average).

Exercise Purpose: Aggregation is the heart of data science. 
This exercise teaches you how to reduce a collection of multiple data points into a single, meaningful summary statistic.

"""

# Numbers = [10, 20, 30, 40, 50]
# total = sum(Numbers)
# avg = total / len(Numbers)
# print(f"Sum of Numbers: {total} and Average of Numbers: {avg}")


"""
Exercise 4. Find Maximum and Minimum from List
Practice Problem: Identify the largest and smallest numerical values within a provided list.

Exercise Purpose: Finding extremes is vital for tasks like identifying the “best” price, the “highest” score, 
or detecting “outlier” data points in a dataset.

"""

# Data = [45, 12, 89, 2, 67]
# print(f"Maximumu {max(Data)} and Minimum {min(Data)}")


"""
Calculate the Product of All Elements
Practice Problem: Multiply every number in a list together to find the total product.

"""
# Factors = [2, 3, 5, 7]
# product = 1

# for i in Factors:
#     product *= i
# print(f"Products = {product}")

"""
Count Even and Odd Numbers
Practice Problem: Given a list of integers, iterate through the items and count how many are even and how many are odd.

Exercise Purpose: This introduces Flow Control and the Modulo Operator. 
It is a classic “Filtering” pattern where you categorize data based on a mathematical property. 
In real-world apps, this is the foundation for things like alternating row colors in a table or batching jobs into two different queues.

"""

# Numbers = [10, 21, 4, 45, 66, 93, 11]
# even_count = 0
# odd_count = 0
# for i in Numbers:
#     if i % 2 == 0:
#         even_count += 1
#     else:
#         odd_count += 1
# print(f"Even Count = {even_count} and Odd Count = {odd_count}")

"""
Practice Problem: Take a list and reverse the order of its elements.

Exercise Purpose: Reversal is a fundamental operation in data structures (like reversing a string or a linked list). 
Python provides multiple ways to do this, and understanding the difference between In-place Reversal 
(changing the original) and Slicing (creating a new one) is crucial for memory management.

Given Input: List: [100, 200, 300, 400, 500]
Expected Output: Reversed List: [500, 400, 300, 200, 100]

"""
# List = [100, 200, 300, 400, 500]
# reversed_list = List[::-1]
# print(f"Reversed List = {reversed_list}")

"""
Sort a List of Numbers
Practice Problem: Sort a list of numbers in ascending order (lowest to highest).

Exercise Purpose: Sorting is perhaps the most studied topic in Computer Science. It turns chaotic data into organized data, which is a prerequisite for high-speed search algorithms like Binary Search. Python uses Timsort, an efficient, hybrid sorting algorithm.

Given Input: Unsorted: [56, 12, 89, 3, 22]
Expected Output: Sorted List: [3, 12, 22, 56, 89]

"""
# Unsorted = [56, 12, 89, 3, 22]
# Unsorted.sort()
# print(f"Sorted list = {Unsorted}")

"""
Create a Copy of a List
Practice Problem: Create a copy of an existing list so that modifying the copy does not change the original.

"""
# Original = ["Apple", "Banana", "Cherry"]
# Copy = Original.copy()
# print(f"Original List: {Original} and Copy of the list {Copy}")

"""
Exercise 10. Combine Two Lists
Practice Problem: Merge two separate lists into a single, unified list.

Exercise Purpose: Data often arrives in fragments from different sources (e.g., two different database queries). Combining or “Concatenating” them is the first step in data aggregation.

Given Input:

List A: ["Physics", "Chemistry"]
List B: ["Maths", "Biology"]
Expected Output: Combined List: ['Physics', 'Chemistry', 'Maths', 'Biology']

"""

