# --- Normal code ---
def sum_digits(s):
    total = 0
    for char in s:
        if char in '0123456789':
            val = int(char)
            total += val
    return total

print(sum_digits("1234"))
print(sum_digits("abcd9082j"))

# -- using Try and Except block -- 
def sum_digits_except(s):
    total = 0
    for char in s:
        try:
            val = int(char)
            total += val
        except:
            print("Cant convert ",char)
    return total

print(sum_digits_except("1234"))
print(sum_digits_except("1234abcdefg"))

