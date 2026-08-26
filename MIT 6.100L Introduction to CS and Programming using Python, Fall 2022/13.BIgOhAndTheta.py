# # Lecture 22: Big Oh and Theta 

# # -- Timing a program: 
# # -- last lecture we used time in this lecture we use performance counter ir perf_counter (this is used in real world)

# import time 
# def convert_to_km(m):
#     return m * 1.609

# t0 = time.perf_counter() # perf_counter() - This is more accurate that time.time()
# convert_to_km(10000000)
# dt = time.perf_counter()-t0

# print(f"t = {dt}seconds")

# ------------------------------------------------------------
# -- Here we are going to looke at two functions:  

def convert_to_km(m):
    return m * 1.609

def compound(invest,interest,n_months):
    total = 0
    for i in range(n_months):
        total = total * interest + invest
    return total

"""
Questions: 

1. How long does it take to compute this functions?
2. Does it depend on Input Parameters?
3. Are the times noticeably different for these two functions? 

"""