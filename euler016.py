
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

# define exponent function
def exponent(n, power):
    if power <= 0:
        return 1
    if power == 1:
        return n
    result = n
    for i in range(1, power):
        result = result * n
    return result


# finds the sum of all digits in a string containing integers
def digitSum(string):
    dsum = 0
    for x in string:
        dsum = int(x) + dsum
    return dsum

# find the exponent
value = str(exponent(2, power = case))

# find solution
sol = digitSum(value)
print("the solution is", sol)

# print elapsed time
print(time.time() - t0, "seconds elapsed")
