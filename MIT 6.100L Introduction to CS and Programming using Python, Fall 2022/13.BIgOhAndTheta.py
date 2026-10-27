# # Lecture 22: Big Oh and Theta 

# # -- Timing a program: 
# # -- last lecture we used time in this lecture we use performance counter ir perf_counter (this is used in real world)

import time 
# def convert_to_km(m):
#     return m * 1.609

# t0 = time.perf_counter() # perf_counter() - This is more accurate that time.time()
# convert_to_km(10000000)
# dt = time.perf_counter()-t0

# print(f"t = {dt}seconds")

# # ------------------------------------------------------------
# # -- Here we are going to looke at two functions:  

# def convert_to_km(m):
#     return m * 1.609

# def compound(invest,interest,n_months):
#     total = 0
#     for i in range(n_months):
#         total = total * interest + invest
#     return total

# # Inputs 
# L_N = [1]
# for i in range(7):
#     L_N.append(L_N[-1]*10)

# for N in L_N:
#     t = time.perf_counter()
#     km = convert_to_km(N)
#     dt = time.perf_counter() - t
#     print(f"Convert_to_km({N}) took {dt:.2e} seconds ({1/dt:,.2f}/sec)")

# print()
# # -- Here we are checking which variable of compound functions effects the running time (Checking the effects of input parameters on time )
# # here we chnage invest rate: 
# for N in L_N:
#     t = time.perf_counter()
#     money = compound(N,1.05,12)
#     dt = time.perf_counter()-t
#     print(f"Compound({N}) took {dt:.2e}seconds ({1/dt:,.2f}/sec)")
# # lets check what happens if we change the interest rate:
# for N in L_N:
#     t = time.perf_counter()
#     money = compound(10.0,1+1/N,12)
#     dt = time.perf_counter()-t
#     print(f"Compound({N}) took {dt:.2e}seconds ({1/dt:,.2f}/sec)")
# # here we are changing the months to check whether it has effect on Time or not:
# for N in L_N:
#     t = time.perf_counter()
#     money = compound(10.0,1.05,N)
#     dt = time.perf_counter()-t
#     print(f"Compound({N}) took {dt:.2e}seconds ({1/dt:,.2f}/sec)")

"""
Scientific notations: 1.44e-0.6 = 1.44 x 10^-6 --> read the seconds 

Observations about above code: 
1. Time grows with the input only when n_months chnages
2. Average time seems to increase by 10 as size of argument increases by 10
3. relationship between size and time only predictable for large sizes

Questions: 

1. How long does it take to compute this functions?
2. Does it depend on Input Parameters?
3. Are the times noticeably different for these two functions? 

"""

# # ----------------------------------------------------------------------------
# # INPUTS HERE ARE LISTS: lets check the change in time

# def sum_of(L):
#     total = 0.0
#     for elt in L:
#         total = total + elt 
#     return total

# L_N = [1]
# for i in range(7):
#     L_N.append(L_N[-1]*10)

# for N in L_N:
#     L = list(range(N)) # this means 1st input will be [1,2..10], end input will be [1,2,3..100] and 3rd 4th goes on 
#     t = time.perf_counter()
#     s = sum_of(L)
#     dt = time.perf_counter() - t
#     print(f"Sum of ({N}) took {dt:.2e}seconds ({1/dt:,.2f}/sec)")

"""
Observations:
1. Size of input now the length of list, not how big the elements numbers are 
2. Average time increases by 10 as size of argument increases by 10
3. relationship between size and time only predictable for larger sizes
4. Time seems compareable to computation of compound
Another observations Number took compount took 8 seconds to run 100 millions and list of 100 milions took about 7 seconds -- This is youtube's observations 

"""

# # -------------------------------------------------------------------------------------------

# # Brute Force Technique -- Measure time to find element in the list
# def is_in(L,x):
#     for ele in L:
#         if ele == x:
#             return True
#         return False

# # Bisection Search 
# def binary_search(L,x):
#     lo = 0
#     hi = len(L)
#     while lo-hi > 1:
#         mid = (lo+hi)//2
#         if L[mid] <= x:
#             lo = mid
#         else:
#             hi = mid
#     return L[lo] == x

# '''
# Here builtin functions took less time that normal ones which we have created

# '''


#  -- NESTED LOOP COMLEXITY --

"""
diameter Function: Means there are several points in a plane or a surface This code will tell us which one have the biggest distance and whats that distance.. 
This is the aim of the function
"""

import math

def diameter(L):
    farthest_dist = 0
    for i in range(len(L)): # selects one point and calculates distance between others
        for j in range(i+1,len(L)): # go through each element except myself 
            p1 = L[i]
            p2 = L[j]
            dist = math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)
            if dist>farthest_dist:
                farthest_dist = dist
    return farthest_dist

# L = [ (math.cos(0),math.sin(0)), (math.cos(1),math.sin(1)), (math.cos(2),math.sin(2)), (math.cos(3),math.sin(3)) ]
# print(diameter(L))

def create_list_of_2D_points(N):
    L = []
    for i in range(N):
        x = math.cos(i) * i
        y = math.sin(i) * i
        L.append((x,y))
    return L
L_N = [100,200,400,800,1600,3200,6400]

diameter_times = []
last = 0

for N in L_N:
    L = create_list_of_2D_points(N)
    t = time.perf_counter()
    d = diameter(L)
    dt = time.perf_counter() - t
    diameter_times.append(dt)
    print(f"diameter of {N} points took {dt} seconds")
    if(last != 0):
        print(f"delta = {dt/last:.1f}x for 2x many points")
    last = dt