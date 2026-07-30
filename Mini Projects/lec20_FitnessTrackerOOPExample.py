"""
Data attributes
    How can you represent your object with data?
What it is
    For a coordinate: x and y values
    For a workout: start time, end time, calories

Functional attributes (behavior/operations/methods)
    How can someone interact with the object?
What it does
    For a coordinate: find distance between two
    For a workout: display an information card

"""

# here start end and calories are initialized in the constructor so it means # "Take whatever calories the user gave me and store it."
# and the icon and kind is not initialized in parameter it means "I don't care what the user gives me — every object created from this class gets 'workout'."

from dateutil import parser # library is a collection of objects or methods, functions that deal with same type of data 

class Workout(object):
    cal_per_hour = 200 # class varibale - all instances of Workout can read this .. 
    # we can access cal_per_hour outside the class by just doing -- print(Workout.cal_per_hour)
    def __init__(self,start,end,calories = None): # here start and end is passed in as string 
        self.start = parser.parse(start) # "Take whatever calories the user gave me and store it."
        self.end = parser.parse(end) # "Take whatever calories the user gave me and store it."
        self.calories = calories # "Take whatever calories the user gave me and store it."
        self.icon = 'sad' # "I don't care what the user gives me — every object created from this class gets 'workout'."
        self.kind = 'workout' # "I don't care what the user gives me — every object created from this class gets 'workout'."

    # -- Adding Getters and Setters -- used outside the class to access data attributes

    # -- getters to get the values ---
    def get_calories(self):
        if (self.calories == None):
            return Workout.cal_per_hour*(self.end-self.start).total_seconds()/3600 # only for this phrase we are reconverting it into daytime object and total_seconds() is a method that work on datetime datatype 
        else:
            return self.calories

        # return self.calories (old ones)
    def get_start(self):
        return self.start
    def get_end(self):
        return self.end

        # -- Setters to set the values --
    def set_calories(self,calories):
        self.calories = calories
    def set_start(self,start):
        self.start = start
    def set_end(self,end):
        self.end = end


# # -- Inspect internal state of class --

# print(Workout.__dict__.keys())
# print(Workout.__dict__.values())

# # --testers for workout class --
# myworkout = Workout('9/30/2021 1:35 PM','9/30/2021 1:57 PM',200)
# print(myworkout.__dict__.keys())
# print(myworkout.__dict__.values()) 

"""
Output: 
dict_keys(['start', 'end', 'calories', 'icon', 'kind'])
dict_values(['9/30/2021 1:35 PM', '9/30/2021 1:57 PM', 200, 'sad', 'workout'])

The fact here is start end and calories are fetched from myworkout 
sad and workout is fetched from the main __init__ class

"""
# -- The confusion of Workout and myworkout - Dict class 
"""
             CLASS                         OBJECT
        Workout                         myworkout
           │                                │
           │                                │
     Workout.__dict__               myworkout.__dict__
           │                                │
           ▼                                ▼
     class information              object's attributes


class is NOT a dictionary data type, but Python internally gives classes and objects a special dictionary called __dict__ that stores their attributes. 
That's why the two look so damn similar

-- we can use dot notation to access this attributes, its better to use getters and setters --
it is better to use getter and setter because the implementation might changes, if chnages and if we try to access the data attribute direclty code might crash 
Note to myself: (if in future you didnt understood this just copy paste in chatgpt it will give you an example to explain)
"""
# print(myworkout.calories) # acess data attributes directly.. NOT RECOMMENDED
# print(myworkout.get_calories()) # access attributes via methods -- This is better because it supports information hiding

# #  -- Testers --
# # -- Format 1
# start = '9/30/2026 1:45 PM'
# end = '9/30/2026 2:45 PM'

# # -- Format 2
# start = 'Sept 30 2026 1:45 PM'
# end = 'September 30 2026 3:45 PM'

# start_date = parser.parse(start) # parse will parse the string object to date object 
# end_date = parser.parse(end)
# # parser knows to parse all the type of data in any format 

# print(type(start_date))

# print(end_date - start_date) # this will give us output in the form of hours:mins:secs
# print((end_date - start_date).total_seconds()) # this will give output in seconds


# # -- Cal_per_hour -- 

# print(Workout.cal_per_hour) # -- we can call the variables that is inside the class by just putting the classname before the variable we want to print
# # we dont need instance here

# w = Workout('1/1/2024','1/1/2024', None)
# print(w.cal_per_hour) # we can also access it through the instances 

# # we can also change cal_per hour outside the class:
# Workout.cal_per_hour = 250 
# print(w.cal_per_hour) # here the cal_per_ hour is changed to 250 permenantly

# # we cant do this access its not recommended but if we want we can change it throuh methods (like getter and setter) 

# ==== You Try it ====