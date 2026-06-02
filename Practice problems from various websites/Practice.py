
# --------------------------------
# Hacker Rank Questoions 
# --------------------------------


"""

Title: Find Runner up score
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. 
You are given  scores. Store them in a list and find the score of the runner-up.
Input Format: The first line contains . The second line contains an array   of  integers each separated by a space.

"""
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    highest = float('-inf')
    second_highest = float('-inf')

    for i in arr:
        if i > highest:
            second_highest = highest
            highest = i
        elif i < highest and i > second_highest:
          second_highest = i
    print(second_highest)

"""

Title: Nested List
Given the names and grades for each student in a class of  students, store them in a nested list 
nd print the name(s) of any student(s) having the second lowest grade.
Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

"""
students = []
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])
        scores = []

scores = []
for student in students:
    scores.append(student[1])

unique_scores = list(set(scores))
unique_scores.sort()
second_lowest = unique_scores[1]

names = []
for student in students:
    if student[1] == second_lowest:
        names.append(student[0])

names.sort()

# OUTPUT PHASE
for name in names:
    print(name)

"""
Title: Finding the percentage
The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. 
Print the average of the marks array for the student name provided, showing 2 places after the decimal.

"""
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    scores = student_marks[query_name]
    avg = sum(scores)/len(scores)
    print(f'{avg:.2f}')

"""
Integers in Python can be as big as the bytes in your machine's memory.
There is no limit in size as there is:  (c++ int) or  (C++ long long int).
As we know, the result of  grows really fast with increasing .

Let's do some calculations on very large integers.

"""
a = int(input())
b = int(input())
c = int(input())
d = int(input())

print(a**b + c**d)

"""
You are given a positive integer . Print a numerical triangle of height  like the one below:
1
22
333
4444
55555
......
(use only 2 lines no use of str)
"""

for i in range(1,int(input())):
    print(i * (10**i - 1) // 9)

"""
In this challenge, the user enters a string and a substring. 
You have to print the number of times that the substring occurs in the given string. 
String traversal will take place from left to right, not from right to left.

"""

def count_substring(string, sub_string):
  length = len(sub_string)
  count = 0
  for i in range(len(string) - length + 1):
    string[i : i + length]
    if string[i : i + length] == sub_string:
      count += 1
  return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

"""
You are given a string S
Your task is to find out if the string  contains: alphanumeric characters, alphabetical characters, digits, 
lowercase and uppercase characters.

Input Format
A single line containing a string .

Output Format

In the first line, print True if  has any alphanumeric characters. Otherwise, print False.
In the second line, print True if  has any alphabetical characters. Otherwise, print False.
In the third line, print True if  has any digits. Otherwise, print False.
In the fourth line, print True if  has any lowercase characters. Otherwise, print False.
In the fifth line, print True if  has any uppercase characters. Otherwise, print False.

"""

if __name__ == '__main__':
    s = input()
    print(any(c.isalnum() for c in s))
    print(any(c.isalpha() for c in s))
    print(any(c.isdigit() for c in s))
    print(any(c.islower() for c in s))
    print(any(c.isupper() for c in s))

"""
You are given a string and your task is to swap cases. 
In other words, convert all lowercase letters to uppercase letters and vice versa.
For Example:
Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2 

"""

def swap_case(s):
  result = ""
  for i in s:
    if i.islower():
      result += i.upper()
    elif i.isupper():
      result += i.lower()
    else:
      result += i
  return result

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
    
"""
In Python, a string can be split on a delimiter.
>>> a = "this is a string"
>>> a = a.split(" ") # a is converted to a list of strings. 
>>> print a
['this', 'is', 'a', 'string']

Joining a string is simple:

>>> a = "-".join(a)
>>> print a
this-is-a-string 

"""

def split_and_join(line):
    line = line.split(" ")
    para = "-".join(line)
    return para

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
    
"""
You are given the firstname and lastname of a person on two different lines.
Your task is to read them and print the following:

Hello firstname lastname! You just delved into python.
Function Description

Complete the print_full_name function in the editor below.
print_full_name has the following parameters:
string first: the first name
string last: the last name

"""

"""
Complete the 'print_full_name' function below.

The function is expected to return a STRING.
The function accepts following parameters:
 1. STRING first
 2. STRING last
"""

def print_full_name(first, last):
    print(f'Hello {first} {last}! You just delved into python.')

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)

"""
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of followed by lines of commands where each command will 
be of the types listed above. 
Iterate through each command in order and perform the corresponding operation on your list.

"""

if __name__ == '__main__':
    N = int(input())
    List1 = []
    for i in range(N):
      command = input().split()
  
      if command[0] == "insert":
        List1.insert(int(command[1]), int(command[2]))
      
      elif command[0] == "remove":
        List1.remove(int(command[1]))
        
      elif command[0] == "sort":
        List1.sort()
        
      elif command[0] == "pop":
        List1.pop()
        
      elif command[0] == "reverse":
        List1.reverse()
        
      elif command[0] == "print":
        print(List1)
        
      elif command[0] == "append":
        List1.append(int(command[1]))

"""
Task
Given an integer, , and  space-separated integers as input, create a tuple, , of those  integers. 
Then compute and print the result of .

Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.

Input Format:
The first line contains an integer, , denoting the number of elements in the tuple.
The second line contains  space-separated integers describing the elements in tuple .

Output Format:
Print the result of .

"""

if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    t = tuple(integer_list)
    print(hash(t))

# This will work only when the version of pythin changes from Python 3 to python 2 