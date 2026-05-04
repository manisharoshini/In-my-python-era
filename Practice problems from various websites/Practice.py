
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
