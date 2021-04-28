import sys
import time
from math import floor

# this file has good functions for finding primes efficiently

# this code solves the problem at the following link: 
# https://projecteuler.net/problem=10

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


# finds the next prime, given a list of primes 
# this efficient solve checks only odd candidates 
def findNextPrime(primes_list):
    # start with x = largest prime + 2 (not plus 1 since primes > 2 can't be even)
    x = primes_list[-1] + 2
    checkPrime = isPrime(primes_list, x)
    while checkPrime == None:
        # increment x and check again
        x = x + 2
        checkPrime = isPrime(primes_list, x)
    return x        

# generates a list of the first n primes (minium n==3)
def genPrimesList(n):
    primes = [2, 3, 5]
    tally = 2+3
    while primes[-1] < n:
        tally = tally + primes[-1]
        next_prime = findNextPrime(primes)
        primes.append(next_prime)
    return primes, tally


# # read in test case as a command line argument
case = int(sys.argv[1])

# # find solution
sol = genPrimesList(case)
print("the solution is", sol[-1])

# print elapsed time
print(time.time() - t0, "seconds elapsed")