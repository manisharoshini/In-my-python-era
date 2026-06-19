"""Website Link: https://pynative.com/python-list-exercise-with-solutions/"""

"""
Practice Problem: Write a script to perform the following three operations on given list

Access the third element of a list
List Length: Print the total number of items
Check if the list is empty

"""
numbers = [10, 20, 30, 40, 50]
print(f"Third Element: {numbers[3]}")
print(f"Length of the list: {len(numbers)}")
is_empty = len(numbers) ==0
print(f"IS the list is empty? {is_empty}")

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

Initial_list =[100, 50, 400, 500]
Initial_list[1] = 200
print(f"Updated List at 2nd place {Initial_list}")
Initial_list.append(600)
print(f"Appended List = {Initial_list}")
Initial_list.insert(2,300)  
print(f"Updated Insert: {Initial_list}")
Initial_list.remove(600)
print(f"Initial List: {Initial_list}")
Initial_list.pop(4)
print(f"Initial List: {Initial_list}")

"""
Exercise 3. Sum and Average of All Numbers in a List
Practice Problem: Calculate the total sum of all integers in a list and find the arithmetic mean (average).

Exercise Purpose: Aggregation is the heart of data science. 
This exercise teaches you how to reduce a collection of multiple data points into a single, meaningful summary statistic.

"""

Numbers = [10, 20, 30, 40, 50]
total = sum(Numbers)
avg = total / len(Numbers)
print(f"Sum of Numbers: {total} and Average of Numbers: {avg}")


"""
Exercise 4. Find Maximum and Minimum from List
Practice Problem: Identify the largest and smallest numerical values within a provided list.

Exercise Purpose: Finding extremes is vital for tasks like identifying the “best” price, the “highest” score, 
or detecting “outlier” data points in a dataset.

"""

Data = [45, 12, 89, 2, 67]
print(f"Maximumu {max(Data)} and Minimum {min(Data)}")


"""
Excercise 5: Calculate the Product of All Elements
Practice Problem: Multiply every number in a list together to find the total product.

"""
Factors = [2, 3, 5, 7]
product = 1

for i in Factors:
    product *= i
print(f"Products = {product}")

"""
Excercise 6: Count Even and Odd Numbers
Practice Problem: Given a list of integers, iterate through the items and count how many are even and how many are odd.

Exercise Purpose: This introduces Flow Control and the Modulo Operator. 
It is a classic “Filtering” pattern where you categorize data based on a mathematical property. 
In real-world apps, this is the foundation for things like alternating row colors in a table or batching jobs into two different queues.

"""

Numbers = [10, 21, 4, 45, 66, 93, 11]
even_count = 0
odd_count = 0
for i in Numbers:
    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print(f"Even Count = {even_count} and Odd Count = {odd_count}")

"""
Exercise 7. Reverse a List
Practice Problem: Take a list and reverse the order of its elements.

Exercise Purpose: Reversal is a fundamental operation in data structures (like reversing a string or a linked list). 
Python provides multiple ways to do this, and understanding the difference between In-place Reversal 
(changing the original) and Slicing (creating a new one) is crucial for memory management.

Given Input: List: [100, 200, 300, 400, 500]
Expected Output: Reversed List: [500, 400, 300, 200, 100]

"""
List = [100, 200, 300, 400, 500]
reversed_list = List[::-1]
print(f"Reversed List = {reversed_list}")

"""
Exercise 8. Sort a List of Numbers
Sort a List of Numbers
Practice Problem: Sort a list of numbers in ascending order (lowest to highest).

Exercise Purpose: Sorting is perhaps the most studied topic in Computer Science. It turns chaotic data into organized data, which is a prerequisite for high-speed search algorithms like Binary Search. Python uses Timsort, an efficient, hybrid sorting algorithm.

Given Input: Unsorted: [56, 12, 89, 3, 22]
Expected Output: Sorted List: [3, 12, 22, 56, 89]

"""
Unsorted = [56, 12, 89, 3, 22]
Unsorted.sort()
print(f"Sorted list = {Unsorted}")

"""
Exercise 9. Create a Copy of a List
Create a Copy of a List
Practice Problem: Create a copy of an existing list so that modifying the copy does not change the original.

"""
Original = ["Apple", "Banana", "Cherry"]
Copy = Original.copy()
print(f"Original List: {Original} and Copy of the list {Copy}")

"""
Exercise 10. Combine Two Lists
Practice Problem: Merge two separate lists into a single, unified list.

Exercise Purpose: Data often arrives in fragments from different sources (e.g., two different database queries). Combining or “Concatenating” them is the first step in data aggregation.

Given Input:

List A: ["Physics", "Chemistry"]
List B: ["Maths", "Biology"]
Expected Output: Combined List: ['Physics', 'Chemistry', 'Maths', 'Biology']

"""
ListA = ["Physics", "Chemistry"]
ListB = ["Maths", "Biology"]
CombinedList = ListA + ListB
print(f"Concatinated List is {CombinedList}")

"""
Exercise 11. List Slicing: Extract Middle Elements

Practice Problem: Given a list, extract a “slice” containing the middle three elements.
Exercise Purpose: Slicing is one of Python's most powerful features. Unlike many languages that require manual loops to copy array sub-sections, Python uses [start:stop] syntax. This forms the foundation for data windowing and pagination in web development.

Given Input: List: [10, 20, 30, 40, 50, 60, 70]
Expected Output: Middle Three: [30, 40, 50]

"""

List = [10, 20]
try:
    middle = len(List) // 2
    print(List[middle - 1],List[middle],List[middle +1])
except:
    print("Length is less than 3")


"""
Exercise 12. Swap Two Elements at Given Indices
Practice Problem: Write a script to swap the positions of two elements in a list based on their indices.

Exercise Purpose: Swapping is the heart of every sorting algorithm like Bubble Sort or Quick Sort. 
While other languages require a temporary variable to hold a value during the swap, 
Python offers an elegant, one-line tuple unpacking method that is faster to write and less error-prone.

Given Input:
List: [23, 65, 19, 90]
Indices to Swap: 0 and 2

"""

List = [23, 65, 19, 90]
temp = List[0]
List[0]=List[2]
List[2]=temp
print(List)

"""
Exercise 13. Access Nested Lists (Simple Indexing)
Practice Problem: Given a “list of lists,” access a specific item hidden inside the inner list.

Exercise Purpose: This exercise teaches you to navigate Multi-dimensional Data. 
Think of nested lists like a spreadsheet (Rows and Columns) or a theater seating chart. 
To find a specific seat, you need the row and seat numbers.

Given Input:

Nested List: [[1, 2], [3, 4, 5], [6, 7]]
Goal: Access the number 5.
Expected Output: Accessed Value: 5

"""
Nested_List = [[1, 2], [3, 4, 5], [6, 7]]
print(f"The list: {Nested_List[1][2]}")


"""
Exercise 14. Check if List Contains a Specific Item
Practice Problem: Write a check to see if a certain value exists within a list and print a message based on the result.

Exercise Purpose: This is a Membership Test. It's the logic used for “Is this username taken?” 
or “Is this item in the shopping cart?” Python's in operator makes this incredibly readable, almost like plain English.

Given Input:
Inventory: ["Laptop", "Mouse", "Monitor", "Keyboard"]
Target: "Tablet"

"""

Inventory = ["Laptop", "Mouse", "Monitor", "Keyboard"]
Target = "Tablet"
if Target in Inventory:
    print("Yes")
else:
    print("no")


"""
Exercise 15. Find the Longest String in a List
Practice Problem: In a list of strings, identify which string has the most characters.

Exercise Purpose: This combines Iteration with Comparison.
It teaches you how to evaluate an attribute of an object (its length) rather than just its raw value. 
This is used in text processing, UI layout, and data cleaning.

Given Input:
Words: ["PHP", "Exercises", "Backend", "Python"]
Expected Output: Longest word: Exercises

"""
Words = ["PHP", "Exercises", "Backend", "Python"]
longest = max(Words,key=len) # this will not compare words it will compare length of the each element 
print(f"THe longest ones are: {longest}")



"""
Exercise 16. Turn Every Item of a List into its Square (List Comprehension)
Practice Problem: Given a list of numbers, create a new list where each number is replaced by its square (n2) using a single line of code.

Exercise Purpose: This is your introduction to List Comprehensions. 
In Python, writing a full for loop to build a new list is often considered un-Pythonic. 
List comprehensions execute faster and are cleaner to read, providing a concise way to map a function across a collection.

Given Input: List: [1, 2, 3, 4, 5]
Expected Output: Squared List: [1, 4, 9, 16, 25]

"""
List = [1, 2, 3, 4, 5]
List1 = []
for i in List:
    i = i*i
    List1.append(i)
print(List1)

"""
Exercise 17. Count Occurrences of an Item
Practice Problem: Find out how many times a specific value appears in a list.

Exercise Purpose: This is a basic form of Frequency Analysis. 
Its used in everything from counting word occurrences in a document to verifying 
how many times a specific error code appears in a server log.

Given Input:

List: [10, 20, 30, 10, 40, 10, 50]
Target: 10
Expected Output: The number 10 appears 3 times.

"""
List = [10, 20, 30, 10, 40, 10, 50]
Target = 10
count = 0
for i in List:
    if i == Target:
        count += 1
print(f"The Number {Target} appears {count} times")
        

"""
Exercise 18. Remove All Occurrences of a Specific Item
Practice Problem: Delete every instance of a specific value from a list.

Exercise Purpose: This is a Filtering Operation. 
A common mistake is using .remove(), which deletes only the first occurrence. 
To remove all instances, you need to filter the list. 
This is essential for data scrubbing when you need to purge “bad data” or “flagged entries” entirely.

Given Input:
List: [5, 20, 15, 20, 25, 50, 20]
Item to remove: 20
Expected Output: Cleaned List: [5, 15, 25, 50]

"""

List = [5, 20, 15, 20, 25, 50, 20]
Item_to_remove = 20
Cleaned_List = []
for i in List:
    if i != Item_to_remove:
        Cleaned_List.append(i)
print(f"Cleaned List = {Cleaned_List}")


"""
Exercise 19. Remove Empty Strings from a List of Strings
Practice Problem: Take a list of strings that contains empty entries ("") and remove them to keep only the valid text.

Exercise Purpose: Real-world data is often “noisy.” When you split a paragraph into words or import a CSV, you often end up with empty strings. Learning to “sanitize” your lists is a daily task for developers and data scientists.

Given Input: List: ["Mike", "", "Emma", "Kelly", "", "Brad"]
Expected Output: Cleaned Names: ['Mike', 'Emma', 'Kelly', 'Brad']

"""

# -- Method 1:
List = ["Mike", "", "Emma", "Kelly", "", "Brad"]
Cleaned_names = []
for i in List:
    if len(i) != 0:
        Cleaned_names.append(i)
print(f"CLeaned List = {Cleaned_names}")

# -- Method 2:
List = ["Mike", "", "Emma", "Kelly", "", "Brad"]
for i in List:
    if len(i) == 0:
        List.remove(i)
print(f"Cleaned List = {List}")


"""
Exercise 20. Remove Duplicates from List
Practice Problem: Remove all duplicate values from a list while keeping only one instance of each element.

Exercise Purpose: This exercise introduces Set Theory. In programming, you often need to ensure uniqueness (
e.g., a list of unique email subscribers). 
While there are many ways to do this, using Python's set or dict structures is the fastest way to handle the logic.

Given Input: List: [10, 20, 10, 30, 40, 40, 20, 50]
Expected Output: Unique List: [10, 20, 30, 40, 50]

"""

# -- Method 1
List = [10, 20, 10, 30, 40, 40, 20, 50]
unique_list = []
for i in List:
    if i not in unique_list:
        unique_list.append(i)
print(f"Unique List = {unique_list}")

# -- Method 2: here order of set is not preserved
List = [10, 20, 10, 30, 40, 40, 20, 50]
unique = set(List)
print(f"The Unique List = {unique}")


"""
Exercise 21. List Comprehension for Filtering Numbers
Practice Problem: Given a list of integers, use list comprehension to create a new list 
that contains only the even numbers from the original list.

Exercise Purpose: This is the “Filter” part of the Map-Filter-Reduce paradigm. 
Here we focuses on Conditional Logic within a single line. 
It is the gold standard for creating subsets of data based on specific criteria.

Given Input: List: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Expected Output: Even Numbers: [2, 4, 6, 8, 10]

"""

List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_list = []
for i in List:
    if i % 2 == 0:
        even_list.append(i)
print(f"Even Numbers in the list = {even_list}")


"""
Exercise 22. Concatenate Two Lists Index-wise
Practice Problem: Given two lists of strings, combine them index-by-index to form a single list of concatenated strings.

Exercise Purpose: Data is often stored in parallel lists (e.g., First Names and Last Names). 
This exercise teaches you how to merge parallel data into a usable format, a common need for report generation and UI display.

Given Input:

List 1: ["Py", "is", "awes"]
List 2: ["thon", " ", "ome"]
Expected Output: Merged: ['Python', 'is ', 'awesome']

"""

List1 = ["Py", "is", "awes"]
List2 = ["thon", " ", "ome"]
concatinated_list = []

for i in range(len(List1)):
    concatinated_list.append(List1[i] + List2[i])
print(f"The concatinated List = {concatinated_list}")


"""
Exercise 23. Iterate Both Lists Simultaneously
Practice Problem: Use the zip() function to loop through two lists at once and print their values as pairs.

Exercise Purpose: Iterating through two lists with a single index variable is error-prone 
(you might hit an “Index Out of Range” if lists are different sizes). zip() is the Safe Parallel Iterator.
 It stops automatically at the end of the shortest list, preventing crashes.

Given Input:

List 1: [10, 20, 30]
List 2: [100, 200, 300]
Expected Output:

10 100
20 200
30 300

"""
List1 = [10, 20, 30]
List2 = [100, 200, 300]
for i in range(len(List1)):
    print(List1[i],List2[i])

# note: if we want to iterate through the elements of the list -- we will use for i in List 
# if we want to iterante through index for i in range(len(list)) is used 

"""
Exercise 24. Add New Item After a Specified Item
Practice Problem: Find a specific item in a list and insert a new item immediately after it.

Exercise Purpose: Unlike append() (end) or insert() (fixed index), this is a Context-Aware Insertion. 
This is useful for things like adding a “New!” tag after a specific product name or inserting a middleware 
step into a list of processing functions.

Given Input:

List: [10, 20, 30, 40, 50]
Insert after: 30
New Item: 35
Expected Output: Updated List: [10, 20, 30, 35, 40, 50]

"""
List = [10, 20, 30, 40, 50]
element = 30
NewItem = 35
for i in range(len(List)):
    if List[i] == element:
        List.insert(i+1,NewItem) # synatx of insert(position,value)
print(f"The Updated List = {List}")

"""
Exercise 25. Replace List’s Item with New Value if Found
Practice Problem: Find the first occurrence of a specific value in a list and replace it with a new value.

Exercise Purpose: This is a Selective Update. It mimics “Find and Replace” functionality. 
It teaches you how to identify a location in memory and overwrite it without affecting the rest of the list structure.

Given Input:

List: [5, 10, 15, 20, 25]
Find: 20
Replace with: 200
Expected Output: Modified List: [5, 10, 15, 200, 25]

"""
List = [5, 10, 15, 20, 25]
Find = 20
Replace = 200

for i in range(len(List)):
    if List[i] == Find:
        List[i] = Replace
print(f"Updated List = {List}")

"""
Exercise 26. Find the Second Largest Number in a List
Practice Problem: Write a Python function that takes a list of numbers and returns the second largest value. 
Ensure the function handles lists with duplicate values correctly (e.g., if the list is [10, 10, 9], the second largest is 9).

Exercise Purpose: This exercise teaches you how to process data sets where “rank” matters. 
It also highlights the importance of handling duplicates. 
Simply sorting a list does not work if the largest number appears multiple times. 
It introduces the concept of using Sets to make data unique.

Given Input: List: [12, 35, 1, 10, 34, 1, 35]

Expected Output: Second Largest: 34

"""

List = [12, 35, 1, 10, 34, 1, 35]

for i in List:
    largest = max(List)
    if i == largest:
        List.remove(largest)
# print(List)
SecondLargest = max(List)
print(f"Second Largest = {SecondLargest}")


List = [12, 35, 1, 10, 34, 1, 35]
iter = sorted(List)
large = len(iter)
largest_element = iter[large-1]
print(f" The largest Element in the list is {largest_element}")
if iter[large - 2] == iter[large - 1]:
    second_large = iter[large - 3]
else:
    second_large = iter[large - 2]

print(f"Second Large  is {second_large}")

"""
Exercise 27. Find the Most Frequent Element
Practice Problem: Create a script that identifies the “Mode” of a list—the element that appears most frequently. 
If there is a tie, returning one of the top elements is sufficient for this exercise.

Exercise Purpose: Finding the mode is a fundamental task in data science and statistics. 
This exercise introduces Frequency Mapping using dictionaries, a vital pattern for counting 
occurrences in any programming language.

Given Input: List: [1, 3, 3, 2, 1, 1, 4, 3, 3]
Expected Output: Mode: 3

"""
List = [1, 3, 3, 2, 1, 1, 4, 3, 3]
Frequency = {}
for i in List:
    if i in Frequency:
        Frequency[i] +=1
    else:
        Frequency[i] = 1
print(Frequency)
print(f"The Mode value is {max(Frequency,key = Frequency.get)}")



"""
Exercise 28. Extract Every Nth Element from a List
Practice Problem: Write a function that accepts a list and an integer n, returning a new list 
containing every nth element from the original, starting from the first element (index 0).

Exercise Purpose: This exercise explores List Slicing, one of Python's most powerful features. 
Understanding slicing notation allows you to manipulate sequences with minimal code, which is 
essential for tasks like data sampling.

Given Input:

List: ['a', 'b', 'c', 'd', 'e', 'f', 'g']
n: 3
Expected Output: Result: ['a', 'd', 'g']

"""
List = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
n = 3
print(List[::n])


"""
Exercise 29. Check if List is Palindrome
Practice Problem: Determine if a list reads the same forward and backward. 
The function should return True if it is a palindrome and False otherwise.

Exercise Purpose: Palindrome checks are classic logic tests. 
This exercise demonstrates how to compare a sequence against its own reverse, 
reinforcing concepts of Symmetry and sequence comparison

Given Input: List: [1, 2, 3, 2, 1]
Expected Output: Is Palindrome: True

"""
def palindrome(list):
    return list == list[::-1] #list[::-1] -- means reverse

List = [1, 2, 3, 2, 1]
print(f"{palindrome(List)} ")


"""
Exercise 30. Find All Common Elements Between Three Lists
Practice Problem: Given three separate lists, write a function that returns a list containing only the elements 
that appear in all three.

Exercise Purpose: This exercise introduces Set Intersection. 
When you need to find commonalities across multiple data sources, 
converting them to sets and finding their intersection is the most efficient method (O(n) average time complexity).

Given Input:

List A: [1, 5, 10, 20]
List B: [6, 7, 20, 80, 100]
List C: [3, 4, 15, 20, 30, 70, 80]
Expected Output: Common Elements: [20]

"""
def common_elements(List1,List2,List3):
    common = set(List1) & set(List2) & set(List3)
    return list(common)

ListA = [1, 5, 10, 20]
ListB = [6, 7, 20, 80, 100]
ListC = [3, 4, 15, 20, 30, 70, 80]

print(f"The common elements in all 3 lists are {common_elements(ListA,ListB,ListC)}")

"""
Exercise 31. Filter Strings by Length in a List
Practice Problem: Write a function that takes a list of strings and an integer k. 
The function should return a new list containing only the strings that have a length greater than or equal to k.

Exercise Purpose: This exercise introduces List Comprehensions, which are the “Pythonic” way to filter data. 
It demonstrates how to combine iteration and conditional logic into a single, readable line of code.

Given Input:

List: ["apple", "pie", "banana", "kiwi", "pear"]
k: 5
Expected Output: Filtered List: ['apple', 'banana']

"""

def filter_by_length(List,k):
    return [s for s in List if len(s)>=k]

List = ["apple", "pie", "banana", "kiwi", "pear"]
print(f"The elements that are greater than is {filter_by_length(List,5)}")


"""
Exercise 32. Check if List is Sorted
Practice Problem: Create a function that determines if a list of numbers is sorted in non-decreasing (ascending) order. 
Return True if it is, and False otherwise.

Exercise Purpose: Checking order is a common prerequisite for algorithms like Binary Search. 
This exercise teaches you to perform Neighbor Comparison by examining an element and its immediate successor together.

Given Input: List: [10, 20, 30, 25, 40]

Expected Output: Is Sorted: False

"""
def check_sort(List):
    return List == sorted(List)

List = [10, 20, 30, 25, 40]
print(check_sort(List))

"""
Exercise 33. List to Dictionary Conversion

Practice Problem: Given two lists of the same length, one containing keys and the other containing values. 
combine them into a single dictionary.

Exercise Purpose: In data processing, you often receive related data in separate arrays. 
This exercise teaches you how to use the zip() function to pair elements and transform them into a dictionary.

Given Input:

Keys: ["name", "age", "city"]
Values: ["Alice", 25, "New York"]
Expected Output:

Dictionary: {'name': 'Alice', 'age': 25, 'city': 'New York'}

"""

def mydict(keys,values):
    return dict(zip(keys,values))# zip creates an iterator of Tuple and the tuple is converted to dictionary

Keys = ["name", "age", "city"]
Values = ["Alice", 25, "New York"]

print(f"The Student information is {mydict(Keys,Values)}")


"""
Exercise 34. Find the Difference Between Two Lists
Practice Problem: Write a function that finds the “difference” between two lists—specifically, 
all elements that are present in the first list but not in the second list.

Exercise Purpose: This exercise explores Set Logic and exclusion. 
It is a common task when synchronizing databases or filtering out “already processed” items from a new batch of data.

Given Input:

List A: [1, 2, 3, 4, 5]
List B: [2, 4, 6]
Expected Output: Difference (A - B): [1, 3, 5]

"""
ListA = [1, 2, 3, 4, 5]
ListB = [2, 4, 6]
List  = []
for i in ListA:
    if i not in ListB:
        List.append(i)
print(List)

"""
Exercise 35. Remove Negative Numbers In-place
Practice Problem: Write a function that removes all negative numbers from a list without creating a new list. 
You must modify the original list object directly.

Exercise Purpose: This is a classic “trap” exercise. If you remove items while iterating forward, 
the indices shift and you will skip elements. This exercise teaches In-place Modification and the 
importance of iterating backwards or using slice assignment.

Given Input: List: [10, -5, 20, -1, 0, -8]
Expected Output: Modified List: [10, 20, 0]

"""

List = [10, -5, 20, -1, 0, -8]
ModifiedList = []
for i in List:
    if i >= 0:
        ModifiedList.append(i)
print(ModifiedList)



"""
Exercise 36. Extend Nested List by Adding a Sublist
Practice Problem: Write a function that iterates through a list of nested lists and appends a 
specific sublist (or value) to each inner list.

Exercise Purpose: Working with “lists of lists” is common in matrix manipulation and data grouping. 
This exercise reinforces the concept of Nested Iteration, accessing an object that exists inside another object 
and modifying it in place.

Given Input:

Nested List: [['apple', 'banana'], ['cherry', 'date']]
To Append: "elderberry"
Expected Output: Modified List: [['apple', 'banana', 'elderberry'], ['cherry', 'date', 'elderberry']]

"""
List = [['apple', 'banana'], ['cherry', 'date']]
app = "elderberry"
List[0].append(app)
List[1].append(app)
print(List)


"""
Exercise 37. Concatenate Two Lists in a Specific Order
Practice Problem: Given two lists of strings, create a new list that contains every possible combination 
of elements from the first and second list, concatenated together.

Exercise Purpose: This exercise simulates a Cartesian Product. 
It is useful for generating permutations like combining first names with last names or product categories with sizes. 
It shows how Nested List Comprehensions can replace bulky nested loops.

Given Input:

List 1: ["Hello ", "Take "]
List 2: ["Dear", "Sir"]
Expected Output:

Result: ['Hello Dear', 'Hello Sir', 'Take Dear', 'Take Sir']

"""




"""
Exercise 38. Flatten Nested List (2D to 1D)
Practice Problem: Take a 2D list (a list containing several lists) and “flatten” it 
into a single 1D list containing all the individual elements in their original order.

Exercise Purpose: Flattening is a core data-wrangling task. When you have data chunked 
into groups (like rows in a table) but need to perform a single operation on every individual piece, 
you must flatten the structure first.

Given Input: 2D List: [[1, 2, 3], [4, 5], [6, 7, 8, 9]]

Expected Output: 1D List: [1, 2, 3, 4, 5, 6, 7, 8, 9]

"""
List = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
List1d = List[0] + List[1] + List[2]
print(List1d)


"""
Exercise 39. Flatten a Deeply Nested List (Recursion)
Practice Problem: Write a function that flattens a list of arbitrary depth. The list 
may contain integers or other lists, which in turn may contain even more lists (e.g., [1, [2, [3, 4]]]).

Exercise Purpose: This is a significant step up in logic. It introduces Recursion, 
the act of a function calling itself. This is the only clean way to handle “infinite” 
depth without knowing the structure ahead of time.

Given Input: Deep List: [1, [2, [3, 4], 5], 6, [7, 8]]

Expected Output: Flattened: [1, 2, 3, 4, 5, 6, 7, 8]
"""

def deeplist(List):
    result = []
    for i in List:
        if isinstance(i,list):
            result.extend(deeplist(i))
        else:
            result.append(i)
    return result

DList = [1, [2, [3, 4], 5], 6, [7, 8]]
print(deeplist(DList))


"""

Exercise 40. Calculate Cumulative Sum (Prefix Sums)
Practice Problem: Create a function that transforms a list of numbers into their cumulative sum. 
Each element at index i in the new list should be the sum of all elements from index 0 to i in the original list.

Exercise Purpose: Cumulative sums (or prefix sums) are used in financial tracking (running balance), 
signal processing, and algorithms that require quick range-sum queries. It teaches you how to maintain a Running Total.

Given Input: List: [10, 20, 30, 40]
Expected Output: Cumulative Sum: [10, 30, 60, 100]

"""
def sumoflist(List):
    total = 0 # we use this for iteration or increasing purpose
    sums = [] # this is to store the value
    for i in List:
        total += i
        sums.append(total)
    return sums

List = [10, 20, 30, 40]
print(F"The cummulative sums of list {List} is {sumoflist(List)}")


"""
Exercise 41. Rotate a List (Left or Right by k positions)
Practice Problem: Write a function to rotate a list to the left by k positions. For example, if k=2, 
the first two elements move to the end of the list.

Exercise Purpose: List rotation is a common algorithm in circular buffers and scheduling. 
This exercise teaches you how to use the Modulo Operator (%) to handle cases where k is larger 
than the list length, and how to perform complex reordering using Slicing.

Given Input:

List: [1, 2, 3, 4, 5]
k: 2
Expected Output: Rotated List: [3, 4, 5, 1, 2]

"""

def rotate_list(List,k):
    List1 = List[0:k]
    List2 = List[k:len(List)]
    return List2 + List1

List = [1, 2, 3, 4, 5]
k = 2
print(rotate_list(List,k))



"""
Exercise 42. Split List into Chunks of Size N
Practice Problem: Create a function that takes a list and an integer N, and breaks the list into smaller sublists, 
each of length N. The last chunk may be shorter if the list length isn't  perfectly divisible by N.

Exercise Purpose: Batch processing is essential when dealing with large datasets or API limits 
(e.g., “send 50 emails at a time”). This exercise demonstrates the use of the Step Parameter in the range() function.

Given Input:

List: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N: 3
Expected Output:

Chunks: [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10]]

"""

def breakList(List,k):
    result = []
    # return [List[i : i + k] for i in range(0, len(List), k)]
    for i in range(0, len(List),k):
        result.append(List[i:i+k])
    return result

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(breakList(list,3))
# First we divided it into small chunks and then appended it into the greater one 


"""
Exercise 43. Move All Zeros to the End (Maintaining Order)
Practice Problem: Given a list of numbers, push all zeros to the end of the list while maintaining 
the relative order of all non-zero elements. This must be done efficiently.

Exercise Purpose: This “Stable Partitioning” problem is a favorite in technical interviews. 
It tests your ability to filter data based on a specific criterion while preserving the integrity of the remaining sequence.

Given Input: List: [0, 1, 0, 3, 12]

Expected Output: Result: [1, 3, 12, 0, 0]

"""
def zerosInlist(List):
    result = []
    zeroList = []
    for i in List:
        if i == 0:
            zeroList.append(i)
        else:
            result.append(i)
    return sorted(result) + zeroList


List = [0, 1, 0, 3, 12]
print(zerosInlist(List))


"""
Exercise 44. Generate Prime Numbers using List Comprehension
Practice Problem: Write a single list comprehension that generates a list of all prime numbers up to a given number n.

Prime number is a whole number greater than 1 that cannot be exactly divided by any whole number other than 
itself and 1 (e.g. 2, 3, 5, 7, 11).

Exercise Purpose: This exercise pushes your List Comprehension skills to the limit. 
It requires nesting logic and understanding the mathematical definition of a prime 
(a number x > 1 that has no divisors other than 1 and itself).

Given Input: n = 20
Expected Output: Primes: [2, 3, 5, 7, 11, 13, 17, 19]

"""

# n = 20
# for i in range(0,n+1):
    




"""
Exercise 45. Find All Subsets of a List (Power Set)
Practice Problem: Write a function to find the Power Set of a given list. 
The Power Set is a list of all possible subsets, including the empty list and the list itself.

Exercise Purpose: This introduces Combinatorial Logic. 
The number of subsets for a list of size n is always 2n. 
Mastering this is crucial for “Brute Force” algorithms where you need to test every possible combination of items.

Given Input: List: [1, 2, 3]
Expected Output:
Subsets: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

"""
def get_power_set(lst): # -- not solved by me 
    result = [[]]
    for element in lst:
        # For every existing subset, create a new one including the 'element'
        new_subsets = [subset + [element] for subset in result]
        result.extend(new_subsets)
    return result
        
List = [1, 2, 3]
print(get_power_set(List))

# Explanation to Solution:

# Iterative Building:

# Start with [[]].
# Add 1: Current subsets [] + new subset [1] = [[], [1]].
# Add 2: Current subsets [], [1] + new ones [2], [1, 2] = [[], [1], [2], [1, 2]].
# This doubling effect continues for every element, resulting in exactly 2n subsets.
# Order: This specific method generates subsets in a logical order, gradually increasing the complexity of the combinations.