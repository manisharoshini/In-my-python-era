num_of_sub = int(input("Enter Number of Subjects: "))
total = 0
percentage = 0

for i in range(num_of_sub):
    marks = float(input("Enter the Marks of Each Subject: "))
    total += marks

percentage = total/num_of_sub # if we put this in a loop the percentage will recalculate for every iteration and takes unnecessary space in memory
print(total, percentage)


# -----------------------------------------------------------
def calculate_marks():
    return 

def calculate_cgpa():
    return