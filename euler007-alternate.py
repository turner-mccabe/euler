import sys
import time
from math import floor

# this code is cleaner but twice as slow as the code in euler007-nthPrime.py

# this code solves the problem at the following link: 
# https://projecteuler.net/problem=7

# for information, please visit: 
# https://projecteuler.net/about

# start timer
t0 = time.time()

# define main function

# this code is slow and compact
def genPrimesList(n):
    primes = [2, 3, 5]
    x = primes[-1] + 2
    while len(primes) < n:
        x = x + 2
        if all(x % prime != 0 for prime in primes):
            primes.append(x)
    return primes


# if all(x % prime != 0 for prime in primes):  # this line is a 2x slower alternative to using isPrime() 

# this code is fast and compact
# checks if a number is prime
# it uses only primes as potential factors and exits when it knows a number isn't prime
def isPrime(primes_list, x):
    for i in primes_list:
        if x % i == 0:
            return None
    return True
def genPrimesList(primes, n):
    x = primes[-1] + 2
    while x < n:
        if isPrime(primes, x) == True:
            primes.append(x)
        x = x + 2
    return primes
    

# # read in test case as a command line argument
case = int(sys.argv[1])

# # find solution
sol = genPrimesList(case)
print("the solution is", sol[-1])

# print elapsed time
print(time.time() - t0, "seconds elapsed")