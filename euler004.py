import sys
import time

# this code solves the problem at the following link: 
# https://projecteuler.net/problem=4

# for information, please visit: 
# https://projecteuler.net/about

# read in test case as a command line argument
case = int(sys.argv[1])

# start timer
t0 = time.time()

# define main function
def ssDif(n):
    s1 = 1
    s2 = 1
    for i in range(2, n+1):
        s1 = s1 + i*i
        s2 = s2 + i
    return s2*s2 - s1
    

# find solution
sol = ssDif(case)
print("the solution is", sol)

# print elapsed time
print(time.time() - t0, "seconds elapsed")
