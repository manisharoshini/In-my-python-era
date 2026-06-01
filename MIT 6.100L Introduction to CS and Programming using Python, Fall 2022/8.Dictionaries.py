# # -- Name and Score of the Students and how we access it BEFORE we use dictionaries --
# def get_grades(students,namelist,gradelist):
#     i = namelist.index(students)
#     grade = gradelist[i]
#     return (students,grade)

# names = ['Manisha', 'Roshini', 'Mano']
# grades = ['A+', 'A','A++']
# print(get_grades('Mano',names,grades))

# -- Another approach using List --
def get_grades (who,what,data):
    for stud in data:
        if stud[0] == who:
            for info in stud[1:]:
                if info[0] == what:
                    return who,info
                
eric = ['eric',['ps',[8,4,5]],['mq',[6,7]]]
Ana = ['Ana',['ps',[9,5,5]],['mq',[4,8]]]
John = ['John',['ps',[7,6,8]],['mq',[9,8]]]

grades = [eric, Ana, John]

print(get_grades('eric','mq',grades))
print(get_grades('Ana','ps',grades))
