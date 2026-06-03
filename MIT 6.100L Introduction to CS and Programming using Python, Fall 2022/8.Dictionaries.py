# -- Name and Score of the Students and how we access it BEFORE we use dictionaries --
def get_grades(students,namelist,gradelist):
    i = namelist.index(students)
    grade = gradelist[i]
    return (students,grade)

names = ['Manisha', 'Roshini', 'Mano']
grades = ['A+', 'A','A++']
print(get_grades('Mano',names,grades))

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

# ---------------------------------------------------------------------------------------------------------------
# DICTIONARY : mapping a key to a value (means here we are customizing the index with the name we want)
# {} --> Store Dictionaries
my_dict = {} # length of dictionary is Zero
d = {4:16} # Single element dictionary 
grades = {'Ana':'B', 'Matt':'A', 'Kayl':'A'}
# print(grades)

# -- how do we look up the value associated with the key ? --
print(grades['Matt']) # here grades['Matt'] -> replaced by the value A
# print(grades['Grace']) # will give KeyError

# ---------------------------------------------------------------------------------------------------------------
# Try Yourself: grades in dict mapping student names str to grades str. Here Student is the list of Student names
# this returns list containing grades for students in same order

def find_grades(grades,students):
    Lnew = []
    for elem in students: # here elem is 'Anabell', 'Matt', 'Katy'
        grade = grades[elem]
        Lnew.append(grade)
     
    return Lnew

d = {'Anabell':'B', 'Matt':'A', 'Katy':'C'}
print(find_grades(d,['Matt','Katy'])) # returns ['A','C']

# ---------------------------------------------------------------------------------------------------------------
# -- OPERATIONS ON DICTIONARY --
# -- Add an Entry -- 

grades = {'Ana':'B', 'Matt':'A', 'Kayl':'A'}
grades['Grace'] = 'A+'
print(grades)

# -- Change an Entry 
grades['Grace'] = 'C'
print(grades)

# -- Delete Entry --
del(grades['Grace'])
print(grades)

# -- to check f the keys in dictionary (for that we use in operator)
print('John' in grades) # gives boolean value as output.. this will only check keys and will not change it.
print('Ana' in grades)

# ---------------------------------------------------------------------------------------------------------------
'''
-- Try it Yourself --
Ld is a list of dicts and k is an int.. returns True if k is a key in any dicts of Ld and False otherwise
'''

def find_k_Ld(Ld,k):
    for elem in Ld: # here elem is key1,val1
        if k in elem:
            return True
    return False

d1 = {1:2, 3:4, 5:6}
d2 = {2:4, 4:6}
d3 = {1:1, 3:9, 4:16, 5:25}

print(find_k_Ld([d1,d2,d3],2))
print(find_k_Ld([d1,d2,d3],25))

# ---------------------------------------------------------------------------------------------------------------
# More Operations:
grades = {'Ana':'B', 'Matt':'A', 'Kayl':'A'}

# -- To iterate over KEYS
print(grades.keys()) # will return New Data Type named "dict_keys" output: dict_keys(['Ana', 'Matt', 'Kayl'])
print(list(grades.keys())) # will return keys in the list format

# -- TO iterate over Vlues
print(grades.values()) # will return New Data Type named "dict_values" Output: dict_values(['B', 'A', 'A'])
print(list(grades.values())) # will return values in the list format
# There's no order like list.. the only order it follows the way we are entering the data

# -- TO iterate over both Keys and Values
print(grades.items())
print(list(grades.items()))

# -- looping 
for key,value in grades.items():
    print(f"key is {key} and Value is {value}") # key is Ana and Value is B key is Matt and Value is A key is Kayl and Value is A

# ---------------------------------------------------------------------------------------------------------------

# -- TRY IT YOURSELF --
# key == values 

# My logic
def count_match(d):
    counter = 0
    for k,v in d.items():
        if k == v:
            counter += 1
    return counter

d = {1:2, 3:4, 5:6}
print(count_match(d))

d = {1:d, 'a':'a', 5:5}
print(count_match(d))

# -- Other way: 
def count_match(d):
    counter = 0
    for x in d.keys():
        if d[x] == x:
            counter += 1 
    return counter

d = {1:2, 3:4, 5:6}
print(count_match(d))

d = {1:d, 'a':'a', 5:5}
print(count_match(d))

# ---------------------------------------------------------------------------------------------------------------
# how hash function works - Sum the letters and take mod of 16 (Method is written in Notebook)
# ---------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------------
# Master Dictionary for student functions
grades_master = {
    'Ana': { # one entry - we are mapping strings to dictionary
        'mq' : [5,4,4],
        'ps' : [10,9,8],
        'fin': 'B'
            },
    'Bob': { # another entry - we are mapping strings to dictionary
        'mq' : [6,7,8],
        'ps' : [8,9,10],
        'fin' : 'A'
    }
}
print(grades_master)
print(grades_master['Ana']['mq']) # [5,4,4]


# ---------------------------------------------------------------------------------------------------------------
# # Average of Particular Subject

grades_master = {
    'Ana': { # one entry - we are mapping strings to dictionary
        'mq' : [5,4,4],
        'ps' : [10,9,8]
            },
    'Bob': { # another entry - we are mapping strings to dictionary
        'mq' : [6,7,8],
        'ps' : [8,9,10]
    }
}

def get_average(data, what):
    all_data = []
    for stud in data.keys():
        all_data = all_data + data[stud][what]
        print(all_data) # for reference for loop running 
    return sum(all_data)/len(all_data)

print(get_average(grades_master,'mq'))

# ---------------------------------------------------------------------------------------------------------------
'''
Larger Example: Find most common words in song lyrics
Top most common words in the song 

Step1: we have to create frequency dictionary -- means dictionary of the word and its count
Step2: Find the word that occurs most often and how many times
Step3: find the word that occurs atleast X times X = 1

'''
# -- Step 1: 
def frequency_dictionary(song):
    song_words = song.lower()
    word_list = song_words.split()
    # print(word_list)
    word_dict = {}
    for words in word_list:
        if words in word_dict:
            word_dict[words] += 1
        else:
            word_dict[words] = 1
    return word_dict

# -- Step 2: 
def find_frequency_word(word_dict):
    frequent_words = []
    less_frequent = []
    highest = max(word_dict.values()) # word_dict.values() --> [5,3,5,2] --> max([5,3,5,2]) --> 5 --> highest = 5
    for k,v in word_dict.items(): 
        if v == highest: # if the values of word_dic == 5 at that time the condition becomes True and append works 
            frequent_words.append(k)
    return (frequent_words, highest),(less_frequent) #(['who','you'], 5)


def occurs_often(word_dict,x):
    freq_list = []
    word_freq_tuple = find_frequency_word(word_dict)

    while word_freq_tuple > x:
        word_freq_tuple = find_frequency_word(word_dict)
        freq_list.append(word_freq_tuple)
        for word in word_freq_tuple[0]:
            del(word_dic[word])
    return freq_list

song = " Its such a funny thing, how nothings funny when its you You tell em what you mean but they keep whiting out the truth Its like a work of art that never gets to see the light Keep you beneath the stars, wont let you touch the sky"
# song = "Who says Who says youre not perfect Who says youre not worth it Who says youre the only one thats hurting Trust me thats the price of beauty Who says youre not pretty Who says youre not beautiful Who says" 

word_dic = frequency_dictionary(song)
print(word_dic)
print("++++++++++++++++++++++++++++++++++++++++++++=")
most_freq = find_frequency_word(word_dic)
print(f"MOST FREQUENT VALUES ARE: {most_freq}")
# --- Error code -- need to solve ---

# ---------------------------------------------------------------------------------------------------------------

