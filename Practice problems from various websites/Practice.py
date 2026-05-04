
# --------------------------------
# Hacker Rank Questoions 
# --------------------------------


"""

Title: Find Runner up score
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. 
You are given  scores. Store them in a list and find the score of the runner-up.
Input Format: The first line contains . The second line contains an array   of  integers each separated by a space.

"""
# if __name__ == '__main__':
#     n = int(input())
#     arr = map(int, input().split())
#     highest = float('-inf')
#     second_highest = float('-inf')

#     for i in arr:
#         if i > highest:
#             second_highest = highest
#             highest = i
#         elif i < highest and i > second_highest:
#           second_highest = i
#     print(second_highest)

"""

Title: Nested List
Given the names and grades for each student in a class of  students, store them in a nested list 
nd print the name(s) of any student(s) having the second lowest grade.
Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

"""
# students = []
# if __name__ == '__main__':
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
#         students.append([name,score])
#         scores = []

# scores = []
# for student in students:
#     scores.append(student[1])

# unique_scores = list(set(scores))
# unique_scores.sort()
# second_lowest = unique_scores[1]

# names = []
# for student in students:
#     if student[1] == second_lowest:
#         names.append(student[0])

# names.sort()

# # OUTPUT PHASE
# for name in names:
#     print(name)

"""
Title: Finding the percentage
The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. 
Print the average of the marks array for the student name provided, showing 2 places after the decimal.

"""
# if __name__ == '__main__':
#     n = int(input())
#     student_marks = {}
#     for _ in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         student_marks[name] = scores
#     query_name = input()
#     scores = student_marks[query_name]
#     avg = sum(scores)/len(scores)
#     print(f'{avg:.2f}')

"""
Integers in Python can be as big as the bytes in your machine's memory.
There is no limit in size as there is:  (c++ int) or  (C++ long long int).
As we know, the result of  grows really fast with increasing .

Let's do some calculations on very large integers.

"""
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())

# print(a**b + c**d)

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

# for i in range(1,int(input())):
#     print(i * (10**i - 1) // 9)

"""
In this challenge, the user enters a string and a substring. 
You have to print the number of times that the substring occurs in the given string. 
String traversal will take place from left to right, not from right to left.

"""

# def count_substring(string, sub_string):
#   length = len(sub_string)
#   count = 0
#   for i in range(len(string) - length + 1):
#     string[i : i + length]
#     if string[i : i + length] == sub_string:
#       count += 1
#   return count

# if __name__ == '__main__':
#     string = input().strip()
#     sub_string = input().strip()
    
#     count = count_substring(string, sub_string)
#     print(count)

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

# if __name__ == '__main__':
#     s = input()
#     print(any(c.isalnum() for c in s))
#     print(any(c.isalpha() for c in s))
#     print(any(c.isdigit() for c in s))
#     print(any(c.islower() for c in s))
#     print(any(c.isupper() for c in s))