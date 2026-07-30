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
from math import sin,cos,sqrt,atan2,radians


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

    def __str__(self):
        width = 16
        retstr = f"|{'-'* width}| \n"
        retstr += f"|{' '* width}| \n"
        iconLen = 0
        retstr += f"|{self.icon}{' '* (width-3)}|\n"
        retstr += f"|{self.kind}{' '* (width-len(self.kind)-1)}|\n"
        retstr += f"|{' '* width}|\n"
        duration_str = str(self.get_duration())
        retstr += f"|{duration_str}{' '* (width-len(duration_str)-1)}|\n"
        cal_str = f"{self.get_calories():.0f}"
        retstr += f"|{cal_str} Calories {' '* (width-len(cal_str)-11)}|\n"

        retstr += f"|{' '* (width)}|\n"
        retstr += f"|{' '* (width)}|\n"

        return retstr

    def __eq__(self,other):
        return type(self) == type(other) and \
        self.start == other.start and \
        self.end == other.end and \
        self.kind == other.kind and \
        self.get_calories() == other.get_calories()
    # Here this says if all are same then the workouts are same too 


    # we cant copy paste all of this __str__ code so we created in parent class and call it in subclass 

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

# # ==== You Try it ====4
# # -- testers -- 
# w_one = Workout('Jan 1 2021 12:20 pm', 'Jan 1 2021 1:30 pm')
# print(f"In this the Calories are calculated: {w_one.get_calories()}")

# w_two = Workout('Jan 1 2021 12:20 pm', 'Jan 1 2021 1:30 pm',300)
# print(f"In this the calories are given: {w_two.get_calories()}")

def gpsDistance(p1,p2):
    R = 6373.0

    lat1 = radians(p1[0])
    long1 = radians(p1[1])
    lat2 = radians(p2[0])
    long2 = radians(p2[1])

    # Compute haversine distance
    dlon = long2 - long1
    dlat = lat2 - lat1

    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2) ** 2
    c = 2* atan2(sqrt(a),sqrt(1 - a))

    return R * c

# # --- Run Workout Class

class RunWorkout(Workout):
    cals_per_km = 100
    def __init__(self,start,end,elev=0,calories = None,routeGpsPoints = None):
        super().__init__(start,end,calories) # here parent class is accessed via super() -- the return of the super is the thing in the parenthesis of Runworkout class ie 'Workout'
        self.icon = 'running - icon' # override parent'd default
        self.kind = 'RUNNING' # override parent'd default
        self.elev = elev # This is a new Data Attribute that did not there in parent class 
        self.routeGpsPoints = routeGpsPoints

    def get_elev(self):
        return self.elev
    def set_elev(self,e):
        self.elev = e

    # -- we have our own get_calories() method --
    def get_calories(self):
        if (self.routeGpsPoints != None):
            dist = 0
            lastP = self.routeGpsPoints[0]
            for p in self.routeGpsPoints[1:]:
                dist += gpsDistance(lastP,p) # gpsDistance -- This is just a their own library we can aslo cretaed here 
                lastP = p
            return dist * RunWorkout.cals_per_km
        else:
            return super().get_calories()
    def __eq__(self,other):
        return super().__eq__(other) and self.elev == other.elev
    # so here this means all the things that are equal in parent class shoud work and also extra thing that is elev should also be equals



class SwimWorkout(Workout):
    cal_per_hour = 400
    def __init__(self,start,end,pace,calories = None):
        super().__init__(start,end,calories)
        self.icon = "Swimming - icon"
        self.kind = "SWIMMING"
        self.pace = pace

    def get_pace(self):
        return self.pace
    def set_pace(self,p):
        self.pace = p

    def get_calories(self):
        if (self.calories == None):
            return SwimWorkout.cal_per_hour * (self.end-self.start).total_seconds()/3600
        else:
            return self.calories


# -- Testers --
# w = Workout('9/30/2021 1:35 PM', '9/30/2021 1:57 PM')
# r = RunWorkout('9/30/2021 1:35 PM', '9/30/2021 1:57 PM')

# print(r)
# print(w)
 
"""
When can we use instance of a subclass ?
- We can use an instance of RunWorkout anywhere Workout can be used. Beacuse RunWorkout is a Workout but Workout is not a RunWorkout. 
- Opposite is not True (cannot use Workout anywhere RunWorkout is used). Because runworkout has other attributes other than Workout class. 
- Consider two helping functions

"""

def total_calories(workout):
    cals = 0
    for w in workout:
        cals += w.get_cals()
    return cals

def total_elevation(run_workouts):
    elev = 0
    for e in run_workouts:
        elev += e.get_elev()
    return elev

# # -- Testers --
# w1 = Workout('9/30/2021 1:35 PM', '9/30/2021 1:57 PM')
# print(w1.get_calories()) # this will print the value
# # print(w1.get_elev()) # -- This will throw an error becasue the get_elev() belongs to RunWorkout class and the w1 belongs to Workout class. 
# # Hence "We can use an instance of RunWorkout anywhere Workout can be used. Beacuse RunWorkout is a Workout but Workout is not a RunWorkout" is proved

# w2 = Workout('9/30/2021 1:35 PM', '9/30/2021 1:57 PM',450)
# print(w2.get_calories())

# rw1 = RunWorkout('9/30/2021 1:35 PM', '9/30/2021 1:57 PM',250)
# print(rw1.get_calories())
# print(rw1.get_elev())
# print("______________________")
# rw2 = RunWorkout('9/30/2021 1:35 PM', '9/30/2021 1:57 PM',350,700) # elev comes before coz we have palces=d it first ib runworkout
# print(rw2.get_calories())
# print(rw2.get_elev())
# print("______________________")
# rw3 = RunWorkout('9/30/2021 1:35 PM', '9/30/2021 1:57 PM',calories=240)
# print(rw3.get_elev())
# print(rw3.get_calories())


# # -- Testers for checking the latitude and longitude functions --
# points = [(42.3601,-71.0589),(42.3370,-71.2092)]
# run1 = RunWorkout('9/30/2021 1:35 PM', '9/30/2021 1:57 PM',calories=240,routeGpsPoints=points)
# print(f"Calories with route points: {run1.get_calories()}")

# run2 = RunWorkout('9/30/2021 1:35 PM', '9/30/2021 1:57 PM',calories=240)
# print(f"Calories with simple ones: {run2.get_calories()}")

# -- testers for __eq__ --
w1 = Workout('9/30/2021 1:35 PM','9/30/2021 2:05 PM', 500)
w2 = Workout('9/30/2021 1:35 PM','9/30/2021 2:05 PM') # cal are
w3 = Workout('9/30/2021 1:35 PM','9/30/2021 2:05 PM', 100)

rw1 = RunWorkout('9/30/2021 1:35 PM','9/30/2021 3:05 PM', 100)
rw2 = RunWorkout('9/30/2021 1:35 PM','9/30/2021 3:05 PM', 200)
rw3 = RunWorkout('9/30/2021 1:35 PM','9/30/2021 3:05 PM', 100)

print(w1 == w2) # False -- since only length of workout is same
print(w1 == w3) # False -- since only length of workout is same
print(w2 == w3) # True -- length and clories both are equal
print(w1 == rw1) # False -- types of w1 and rw1 are different
print(rw1 == rw2) # False -- Elevation are different
print(rw1 == rw3) # True -- Everything is same 

# -------------------End-------------------------------------------------------------