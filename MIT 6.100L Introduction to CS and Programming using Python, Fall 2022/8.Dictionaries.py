# # -- Name and Score of the Students and how we access it BEFORE we use dictionaries --
# def get_grades(students,namelist,gradelist):
#     i = namelist.index(students)
#     grade = gradelist[i]
#     return (students,grade)

# names = ['Manisha', 'Roshini', 'Mano']
# grades = ['A+', 'A','A++']
# print(get_grades('Mano',names,grades))

# # -- Another approach using List --
# def get_grades (who,what,data):
#     for stud in data:
#         if stud[0] == who:
#             for info in stud[1:]:
#                 if info[0] == what:
#                     return who,info
                
# eric = ['eric',['ps',[8,4,5]],['mq',[6,7]]]
# Ana = ['Ana',['ps',[9,5,5]],['mq',[4,8]]]
# John = ['John',['ps',[7,6,8]],['mq',[9,8]]]

# grades = [eric, Ana, John]

# print(get_grades('eric','mq',grades))
# print(get_grades('Ana','ps',grades))

# ---------------------------------------------------------------------------------------------------------------
# # DICTIONARY : mapping a key to a value (means here we are customizing the index with the name we want)
# # {} --> Store Dictionaries
# my_dict = {} # length of dictionary is Zero
# d = {4:16} # Single element dictionary 
# grades = {'Ana':'B', 'Matt':'A', 'Kayl':'A'}
# # print(grades)

# # -- how do we look up the value associated with the key ? --
# print(grades['Matt']) # here grades['Matt'] -> replaced by the value A
# # print(grades['Grace']) # will give KeyError

# # ---------------------------------------------------------------------------------------------------------------
# # Try Yourself: grades in dict mapping student names str to grades str. Here Student is the list of Student names
# # this returns list containing grades for students in same order

# def find_grades(grades,students):
#     Lnew = []
#     for elem in students: # here elem is 'Anabell', 'Matt', 'Katy'
#         grade = grades[elem]
#         Lnew.append(grade)
     
#     return Lnew

# d = {'Anabell':'B', 'Matt':'A', 'Katy':'C'}
# print(find_grades(d,['Matt','Katy'])) # returns ['A','C']

# # ---------------------------------------------------------------------------------------------------------------
# # -- OPERATIONS ON DICTIONARY --
# # -- Add an Entry -- 

# grades = {'Ana':'B', 'Matt':'A', 'Kayl':'A'}
# grades['Grace'] = 'A+'
# print(grades)

# # -- Change an Entry 
# grades['Grace'] = 'C'
# print(grades)

# # -- Delete Entry --
# del(grades['Grace'])
# print(grades)

# # -- to check f the keys in dictionary (for that we use in operator)
# print('John' in grades) # gives boolean value as output.. this will only check keys and will not change it.
# print('Ana' in grades)

# # ---------------------------------------------------------------------------------------------------------------
'''
-- Try it Yourself --
Ld is a list of dicts and k is an int.. returns True if k is a key in any dicts of Ld and False otherwise
'''

# def find_k_Ld(Ld,k):
#     for elem in Ld: # here elem is key1,val1
#         if k in elem:
#             return True
#     return False

# d1 = {1:2, 3:4, 5:6}
# d2 = {2:4, 4:6}
# d3 = {1:1, 3:9, 4:16, 5:25}

# print(find_k_Ld([d1,d2,d3],2))
# print(find_k_Ld([d1,d2,d3],25))

# # ---------------------------------------------------------------------------------------------------------------
