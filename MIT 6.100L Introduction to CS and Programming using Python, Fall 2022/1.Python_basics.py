# -------------------------------
x = 1 # Assign value 1 to variable x
y = 2# Assign value 2 to variable y

print(x)# Print the value of x
print(y)# Print the value of y

# Swap the values of x and y
temp = x # Store value of x in a temporary variable
x = y # Assign value of y to x
y = temp # Assign value stored in temp to y
print(x)# Print swapped value of x
print(y)# Print swapped value of y

# -------------------------------
# String concatenation examples
# -------------------------------
a = "me" # Assign string "me" to variable a
b = "Myself"# Assign string "Myself" to variable b

d = a + " " + b # Concatenate strings with a space in between
silly = a * 3 # Repeat string 'a' three times

print(d)# Print concatenated string
print(silly)# Print repeated string

# -------------------------------
# String game
# -------------------------------
b = ":" # Assign colon symbol to b
c = ")"# Assign closing bracket symbol to c

s1 = b + 2 * c # Concatenate ':' with two repetitions of ')'

print(s1)# Print the resulting string


f = "a" # Assign string "a" to f
g = " b" # Assign string with leading space " b" to g
h = "3" # Assign string number "3" to h

s2 = (f + g) * int(h)# Concatenate f and g, then repeat it int(h) times

print(s2)# Print the final string

# -------------------------------
# String indexing
# -------------------------------
s = "abc"# Assign string "abc" to s

a = s[0] # Access first character
b = s[1]# Access second character
c = s[2]# Access third character
print(a)# Print first character
print(b)# Print second character
print(c)# Print third character

# -------------------------------
# String slicing
# -------------------------------


sa = "abcdefgh"# Assign string "abcdefgh" to sa

print(sa[3:6])# Slice from index 3 to 5
print(sa[3:6:2])# Slice from index 3 to 5 with step 2
print(sa[:])# Print entire string
print(sa[::-1])# Reverse the string

# -------------------------------
# Example 2: String slicing
# -------------------------------
s2 = "ABC d3f ghi"# Assign mixed string to s2

print(s2)# Print the string
print(s2[3:len(s2)-1])# Slice from index 3 to second last character
print(s2[4:0:-1])# Reverse slice from index 4 to 1
# Empty slice because start > end
print(s2[6:3])  # its an empty string coz 6>3

# -------------------------------
# Input examples
# -------------------------------
text = input("TYPE SOMETHING: ")# Take user input as string

print(text * 5)# Print the input 5 times
num1 = input("Enter first number: ")# Take first number as string input
print(num1 * 5)# String repetition occurs here
num2 = int(input("Enter number: "))# Take number input and convert to integer
print(num2 * 5)# Multiply integer by 5

# -------------------------------
# If-else example
# -------------------------------
x = float(input("Enter a number: "))# Take first number as float
y = float(input("Enter a number: "))# Take second number as float

if x == y: 
    print("x and y are equal")# Check if x and y are equal
    if y != 0:
        print("x/y is", x / y) # Check if y is not zero to avoid division error
elif x < y:
    print("x is smaller")# Check if x is smaller than y
else: 
    print("y is smaller")# Otherwise y is smaller

print("Thanks!!")

# -------------------------------
# While loop example
# -------------------------------
n = int(input("Enter a non negative Integer: "))

# Loop until n becomes zero
while n > 0:
    print('x')
    n = n - 1

# -------------------------------
# While loop sequence example
# -------------------------------
n = 0 

# Loop until n is less than 5
while n < 5:
    print(n)
    n = n + 1

# -------------------------------
# Factorial using while loop
# -------------------------------
x = 4# Number whose factorial is to be found
i = 1  # Initialize counter
factorial = 1 # Initialize factorial result

# Loop until i reaches x
while i <= x:
    factorial *= i  # Multiply factorial by i
    i += 1          # Increment i
print(f'{x} is the factorial of {factorial}')

# -------------------------------
# For loop example
# -------------------------------
n = 0
# While loop version
while n < 5:
    print(n)
    n = n + 1
    
for n1 in range(5):
    print(n1)# For loop equivalent of above code

# -------------------------------
# Range control examples
# -------------------------------
for i in range(3, 20):
    print(i)# Loop from 3 to 19
for j in range(3, 20, 2):
    print(j)# Loop from 3 to 19 with step of 2

# -------------------------------
# Sum calculation using for loop
# -------------------------------
mySum = 0

# Loop from 0 to 9
for i in range(10):
    mySum += i
    print(mySum)

print("Sum is:", mySum)

# -------------------------------
# Break statement example
# -------------------------------
mysum = 0

# Loop through range with step 2
for i in range(5, 11, 2):
    mysum += i
    
    # Break loop if sum becomes 5
    if mysum == 5:
        break
        
    mysum += 1
    
print("Sum is:", mysum)

# -------------------------------
# Strings and loops examples
# -------------------------------
s = "demo loops - fruit loops"

# Loop using index
for index in range(len(s)):
    if s[index] == "i" or s[index] == "u":
        print("There's an i and u in the statement")

# Loop directly through characters
s1 = "demo loops - fruit loops"
for char in s1:
    if char == "i" or char == "u":
        print("There's an i and u in the statement")

# Loop using 'in' keyword
s2 = "demo loops - fruit loops"
for char in s2:
    if char in "iu":
        print("There's an i and u in the statement")
        
# -------------------------------------------------------------------------------------------------------------------

verb = input("Enter a verb: ")
print("I can" + " "+ verb + " " + "better than you !!")
print(verb * 5, end=' ')

print("I can",verb, "better than you !!")

#---------------------------------------------------------------------------------------------------
# Newton's algorithm 

x = int(input("Enter to find the cube root: "))
g = int(input("Enter Initial guess: "))

print("current estimated cube = ",g**3)
next_g = g - ((g**3 - x)/(3*g**2))
print("Next Guess = ", next_g)

# While Loop example infinite loop
while True:
    print("No !!")
#---------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------
# Expand the code to show the sad face when user entered the while loop two more types
# HINT: USE VARIABLE AS A COUNTER
count = 0
where = input("Go Left or Right?").lower()
while where == "right":
    count += 1
    if count > 2: 
        print("You are such a DumbAss")
    where = input("Go Left or Right?").lower()
print("Get lost Bitch !!!")
print(count, "many times you behaved like a dumb fucker")
#---------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------
# For Loops Prractice Examples:
for i in range(1,4,1):
    print("i love u !!")
    print(i)
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
for j in range(1,4,2):
    print(j ** 2)
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
for k in range(4,0,-1):
    print("$"*k)
#---------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------
#Fix the code using variables Start and End in the range, to get the total sum between including those values
#Eg: start = 3 and end = 5 the sum should be 12
mySum = 0
for i in range(3,6):
    mySum += i
print(mySum)

# OR
mysum = 0
start = 3
end = 5
for j in range(start,end+1):
    mysum += j
print(mysum)
#---------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------
# # write a code that loops a for loop over some range and prints how many even numbers are in the range.

count_evennum = 0

for i in range(5):
    if i % 2 == 0:
        count_evennum += 1
        print(i)
print("The count of even numbers: ",count_evennum)
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
for j in range(10):
    if j % 2 == 0:
        print(j)     
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
for k in range(2,9,3):
    if k % 2 == 0:
        print(k)
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------   
for l in range(-4,6,2):
    if l % 2 == 0:
        print(l)
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------        
for m in range(5,6):
    if m % 2 == 0:
        print(m)
#---------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------
# # ROBOT CHEERLEADING PRACTICE PROBLEM:
an_albhabet = 'AEIOUaeiou'
word = input("I'll cheer for you !!! Enter a word: ")
times = int(input("Enthusiasm level (1-10): "))

for w in word:
    if w in an_albhabet:
        print(f'give me an {w} : {w}')
    else:
        print(f'give me a {w} : {w}')
print("What does that spell?")
for i in range(times):
    print(f'{word} !!!!')
#---------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------
# Assume you are given a list of lowercase letters in variable s. count how many unique variable are in the string 
s = "abcdefabcdef"
seen = ""
for char in s:
    if char not in seen:
        seen = seen + char
print("Number of unique letters: ", len(seen))

secret_number = 39
guess = int(input("Enter a number: "))
if guess == secret_number:
   print("You guessed it right!")
else:
   print("Wrong")

print(guess == secret_number)
#---------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------
# Secret number advanced version

if guess == secret_number:
    print("You Gotcha !!")
elif guess < secret_number:
    print("Guess some higher")
elif guess > secret_number:
    print("Guess something Lower")
#---------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------
# Guess number using for loop:
found = False
secret = 4
for i in range(1,11):
    if i == secret:
        found = True # here we are dealing with the logics and then we put if ele statement outside the loop
if not found: # means if found == False
    print("not found")
else:
    print("found")
#---------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------        
# Guess and Check cubes (only positive values)

cube = int(input("Enter a value: "))
for guess in range(1,100):
    if guess ** 3 == cube:
        print("The cube root of ",cube,"is",guess)
#---------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------
# Guess and Check cubes (only positive and negative values)
cube = int(input("Enter a number: "))
for guess in range(abs(cube)): # abs --> Assumes number as positive even if the value is negative 
    if guess ** 3 ==abs(cube):
        if cube < 0:
            guess = -guess
        print(f'Cube root of {cube} is {guess}')
#---------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------
# guessing cube in different way:
cube = int(input("Enter a number: "))
for guess in range(abs(cube) + 1):
    if guess ** 3 >= abs(cube):
        break
if guess ** 3 != abs(cube):
    print(f'{cube} is not a perfect cube')
else:
    if cube < 0:
        guess = -guess
    print(f'Cube root of {cube} is {guess}')
#---------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------
# Guess and Check with word problems
# Eg1: Alyssa, Ben and Cindy are selling Tickets to a fundraiser Ben sells 2 fewer than Alyssa. 
# Cindy Sells twice as many as Alyssa. 10 tickets are sold totally by three peoples. How many tickets did Alyssa sell ?
for alyssa in range(11):
    for ben in range(11):
        for cindy in range(11):
            total = (alyssa + ben + cindy == 10)
            two_less = (ben == alyssa - 2)
            twice = (cindy == 2 * alyssa)
            if total and two_less and twice:
                print(f'Alyssa Sold {alyssa}')
                print(f'Ben sold {ben}')
                print(f'Cindy sold {cindy}')
# here they listed all thecombination once everything fits it will find remaining two !! similar to BRute Force !!
#---------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------
# same with Big Numbers 
# Eg2: Alyssa, Ben and Cindy are selling Tickets to a fundraiser Ben sells 20 fewer than Alyssa. 
# Cindy Sells twice as many as Alyssa. 1000 tickets are sold totally by three peoples. How many tickets did Alyssa sell ?
# by old solution each time loop iterates 1000 times.. its a solw process.. to overcome that we use
for alyssa in range(1001):
    ben = max(alyssa - 20,0) #If alyssa - 20 is positive, use it, If alyssa - 20 is negative, use 0 instead
    cindy = alyssa * 2
    if alyssa + ben + cindy == 1000:
        print(f'Ben sold {ben}')
        print(f'Alyssa sold {alyssa}')
        print(f'Cindy sold {cindy}')
# max statement: alyssa - 20 = 30, max(30, 0) = 30, Ben sold 30 tickets
# alyssa - 20 = -10, max(-10, 0) = 0, Ben sold 0 tickets (not negative)
#---------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------
#Algo: Square root Guess and Check
guess = 0
x = int(input("Enter a number to find the square root: "))
if x < 0:
    print("Square root of negative number is not possible")
    exit()
while guess**2 < x: # if guess squared is less than x
    guess += 1 # increment the guess by 1
if guess**2 == x: # if guess squared is equal to x
    print(f"The square root of {x} is {guess}")
else:
    print(f"{x} is not a perfect square")
#---------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------
# Guess and Check using for loop:
x = int(input("Enter a number to find the square root: "))
if x < 0:
    print("Square root of negative number is not possible")
    exit()
for guess in range(x+1):
    guess**2
    if guess**2 == x:
        print(f"The square root of {x} is {guess}")
        break
else:
    print(f"{x} is not a perfect square") 
    # this is for else block of for loop, it will execute only if the loop is exhausted without break
#---------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------
#Binary Number Logic
num = int(input("Enter a number: "))
if num < 0:
    is_neg = True
    num = abs(num)
else:
    is_neg = False
result = ''
if num == 0:
    print("0")
while num > 0:
    result = str(num % 2) + result
    num = num // 2
print(result)
if is_neg:
    print("-"+result)
#---------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------    
# Binary in Fractions
x = 0.1
p = 0
while((2**p)*x)%1 != 0:
    print('Remainder = '+str((p**2)*x - int((2**p)*x)))
    p+=1
num = int(x*(2**p))

result = ''
if num == 0:
    result = '0'
while num > 0:
    result = str(num % 2) + result
    num = num//2

for i in range(p - len(result)):
    result = '0' + result
    
result = result[0:-p] + '.' + result[-p:]
print("The binary representation of result is: "+ str(x) + " is " + str(result))
# 0.1 is not easy to compute !! 
#---------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------
# Guess and Check using approximation:
x = 12345
epsilon = 0.01
num_guesses = 0
guess = 0.0
increement = 0.0001

while abs(guess ** 2 - x) >= epsilon:
    guess += increement
    num_guesses += 1 # for loop will not work here because its for integer only.. and while loop is for float point as well 

print('num_guesses = ',num_guesses)
print(guess, "is the closest approximation")
#---------------------------------------------------------------------------------------------------