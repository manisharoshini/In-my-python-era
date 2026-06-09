# -- Iterative ALgorithm -- 

# -- Multiplication in other way to understand loops and iterations

# -- Using For loop --
# def mult(a,b):
#     total = 0
#     for i in range(b):
#         total += a
#     return total
# print(f"The multiplication is {mult(6,7)}")

# # --Using While loop -- 
# def mult(a,b):
#     result = 0
#     while b > 0:
#         result = result + a 
#         b -= 1 # here the counter starts from zera and decreses way down to 0
#     return result
# print(mult(6,7))

# here the recursive step is a + a*(b-1) 

# -- Recursive addition : Run on python tutor for clearity 
def mult_recur(a,b):
    if b == 1:
        return a 
    else:
        return a + mult_recur(a,b-1) # function is called inside body itself 
print(mult_recur(4,5))
# this will create chains of function call.. 
# here we created loop by just calling function inside function body - this is called Recursion 

"""
What (Exaclty) is Recursion ?
Algorithmically: its a way to desgin solutions for problems by Divide and conquer method or we can also call it as
Decrease and conquer mehtod

-- means reduce the problem to simpler versions of same problem or problem that can be solved directly
"""