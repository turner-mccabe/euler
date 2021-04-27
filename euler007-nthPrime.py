import sys
import time
from math import floor

# this file has good functions for finding primes efficiently

# this code solves the problem at the following link: 
# https://projecteuler.net/problem=7

# for information, please visit: 
# https://projecteuler.net/about

# start timer
t0 = time.time()

# define main function

# checks if a number is prime
# it uses only primes as potential factors and exits when it knows a number isn't prime
def isPrime(primes_list, x):
    for i in primes_list:
        if x % i == 0:
            return None
    return True


# # read in test case as a command line argument
case = int(sys.argv[1])

# # find solution
sol = genPrimesList(case)
print("the solution is", sol[-1])

# print elapsed time
print(time.time() - t0, "seconds elapsed")