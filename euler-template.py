import sys
import time

# this code solves the problem at the following link: 
# https://projecteuler.net/problem=4

# for information, please visit: 
# https://projecteuler.net/about

# start timer
t0 = time.time()

# define main function
def eulerFunction():











# read in test case as a command line argument
case = int(sys.argv[1])

# find solution
sol = eulerFunction(case)
print("the solution is", sol)

# print elapsed time
print(time.time() - t0, "seconds elapsed")