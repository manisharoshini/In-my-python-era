# -------------------------------------------------------------------------------------------------
num_of_sub = int(input("Enter the number of subjects: "))
total_maximum_marks = 0
total_obtained_marks = 0

for i in range(num_of_sub):
    maximum_marks = int(input("Enter Maximum Marks of Each subject: "))
    obtained_marks = int(input("Enter Obtained Marks of Each subject: "))
    total_maximum_marks += maximum_marks
    total_obtained_marks += obtained_marks

def calcPercentAndGrade(total_maximum_marks,total_obtained_marks):
    percentage = (total_obtained_marks/total_maximum_marks) * 100 # if we put this in a loop the percentage will recalculate for every iteration and takes unnecessary space in memory
    grade = 0
    if percentage >= 91 and percentage <= 100:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 65:
        grade = "B"
    elif percentage >= 51:
        grade = "C"
    elif percentage >= 40:
        grade = "D"
    else:
        grade = "Fail"
    print(f"Grade: {grade}")
    return percentage,grade

percentage,grade = calcPercentAndGrade(total_maximum_marks, total_obtained_marks) # unpacking returned values
# # the above code means take returned tuple and store each value separately
print(f'you got {total_obtained_marks}/{total_maximum_marks} and Your Percentage is {percentage:.2f}')

# -- Note: Add exceptions to this 