import sys
import time
from math import floor

# this file has good functions for finding primes efficiently

# Cleaner equivalent code in: euler003-brief.py

# this code solves the problem at the following link: 
# https://projecteuler.net/problem=3

# for information, please visit: 
# https://projecteuler.net/about

# start timer
t0 = time.time()

# breakthrough:
# we want to reduce the amount of time we spend building the list of primes. 
# the largest prime factor is equal to n/(smallest prime factor)
# it is much faster to find the smallest prime factor


def smallestPrimeFactor(n):
    if n%2 == 0: return 2
    if n%3 == 0: return 3
    primes = [2, 3]
    for prime in primes:
        next_prime = findNextPrime(primes)
        primes.append(next_prime)
        if n % next_prime == 0:
            return next_prime

# checks if a number is prime
# it uses only primes as potential factors and exits when it knows a number isn't prime
def isPrime(primes_list, x):
    for i in primes_list:
        if x % i == 0:
            return None
    return True


# generates a list of the primes less than n, given a list of primes to start with
# if all(x % prime != 0 for prime in primes):  # this line is a 2x slower alternative to using isPrime()
def findNextPrime(primes):
    x = primes[-1] + 2
    #TODO this is hacky
    while x: 
        if isPrime(primes, x) == True:
            return x
        x = x + 2


# # find all prime factors
# super efficient runtime
def primeFactors(n):
    factors = []
    while n > 1:
        factor = smallestPrimeFactor(n)
        factors.append(factor)
        n = floor(n / factor)
    return factors

# # read in test case as a command line argument
case = int(sys.argv[1])
print("the solution is", primeFactors(case))

# print elapsed time
print(time.time() - t0, "seconds elapsed")
