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

class Workout(object):
    def __init__(self,start,end,calories):
        self.start = start # "Take whatever calories the user gave me and store it."
        self.end = end # "Take whatever calories the user gave me and store it."
        self.calories = calories # "Take whatever calories the user gave me and store it."
        self.icon = 'sad' # "I don't care what the user gives me — every object created from this class gets 'workout'."
        self.kind = 'workout' # "I don't care what the user gives me — every object created from this class gets 'workout'."

    # -- Adding Getters and Setters -- used outside the class to access data attributes

    # -- getters to get the values ---
    def get_calories(self):
        return self.calories
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
        self.end = endd


# -- Inspect internal state of class --

# print(Workout.__dict__.keys())
# print(Workout.__dict__.values())

# --testers for workout class --
myworkout = Workout('9/30/2021 1:35 PM','9/30/2021 1:57 PM',200)
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
print(myworkout.calories) # acess data attributes directly.. NOT RECOMMENDED
print(myworkout.get_calories()) # access attributes via methods -- This is better because it supports information hiding