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
