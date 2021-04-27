import sys
import time

# this code solves the problem at the following link: 
# https://projecteuler.net/problem=25

# for information, please visit: 
# https://projecteuler.net/about

# start timer
t0 = time.time()

# define main function
def genFibonacci(n):
    if n < 3:
        return
    count = 3
    x = 1
    y = 1
    while count <= n:
        temp = y
        y = y + x
        x = temp
        count = count + 1
    return(y)

def checkLength(length):
    result = 0
    n = 4
    while len(str(result)) < length:
        n = n + 1
        result = genFibonacci(n)
    return n

# read in test case as a command line argument
case = int(sys.argv[1])

# find solution
sol = checkLength(case)
print("the solution is", sol)

# print elapsed time
print(time.time() - t0, "seconds elapsed")