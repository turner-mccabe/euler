
import sys
import time

# this code solves the problem at the following link: 
# https://projecteuler.net/problem=16

# for information, please visit: 
# https://projecteuler.net/about

# read in test case as a command line argument
case = int(sys.argv[1])

# start timer
t0 = time.time()

# define factorial function
def factorial(n):
    if n < 0:
        return None
    result = 1
    while n >= 1:
        result = result * n
        n = n - 1
    return result


# finds the sum of all digits in a string containing integers
def digitSum(string):
    dsum = 0
    for x in string:
        dsum = int(x) + dsum
    return dsum

# find the factorial
value = str(factorial(case))

# find solution
sol = digitSum(value)
print("the solution is", sol)

# print elapsed time
print(time.time() - t0, "seconds elapsed")
