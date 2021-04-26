import sys
import time

# this code solves the problem at the following link: 
# https://projecteuler.net/problem=15

# for information, please visit: 
# https://projecteuler.net/about

# read in test case as a command line argument
case = int(sys.argv[1])

# start timer
t0 = time.time()

# initial attempt produces correct solutions, but is too slow
# this function takes approx 1 second for case = 12,
# it takes 4 times longer for 13 and 4 times longer again for case = 14
# extrapolating, case = 20 is estimated to take 17 hours. 
def paths(i, j):
    if (i == 0 or j == 0):
        return 1
    else:
        return paths(i-1, j) + paths(i, j-1)
        

# define main function
# this function converges faster
# it is more than 28 times faster 
# for case = 20, it takes 4 minutes instead of 17 hours
def paths2(i, j):
    if (i == 0 or j == 0):
        return 1
    if i == 1:
        return j + 1
    if j == 1:
        return i + 1
    else:
        return 2*paths2(i-1,j-1) + paths2(i,j-2) + paths2(i-2,j)

# find solution
sol = paths2(case, case)
print("the solution is", sol)

# print elapsed time
print(time.time() - t0, "seconds elapsed")


# # this loop was used for performance testing
# for case in range(1, 12):
#     # find solution
#     sol = paths2(case, case)
#     print("the solution is", sol)
