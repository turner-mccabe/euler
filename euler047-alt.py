import sys
import time

# this code solves the problem at the following link: 
# https://projecteuler.net/problem=47

# for information, please visit: 
# https://projecteuler.net/about

t0 = time.time()


# efficiently finds all prime factors of n
# *** altered to only append distinct primes
def primeFactors(n):
    factors = []
    while n > 1:
        factor = smallestPrimeFactor(n)
        factors.append(factor)
        n = round(n / factor)
    return factors

# finds smallest prime factor by building a list of primes
# each new prime is tested to be a factor of n, if yes, it returns the prime factor
def smallestPrimeFactor(n):
    if n%2 == 0: return 2
    if n%3 == 0: return 3
    primes = [2, 3]
    for prime in primes:
        next_prime = findNextPrime(primes, primes[-1] + 2)
        primes.append(next_prime)
        if n % next_prime == 0:
            return next_prime

# *** This had to be commented out because of max recursion depth exceeded
# replaced by iterative method in the two functions below 

# recursive, finds next prime given a list of primes and a starting point
# def findNextPrime(primes, x):
#     for i in primes:
#         if x % i == 0:
#             return findNextPrime(primes, x + 2)
#     return x


def isPrime(primes_list, x):
    for i in primes_list:
        if x % i == 0:
            return None
    return True

def findNextPrime(primes, x):
    while x: 
        if isPrime(primes, x) == True:
            return x
        x = x + 2


# Finds the first four consecutive integers to have four distinct prime factors each.
def conPrimes(x, top, n):
    factor3 = set(primeFactors(x + 2))
    factor2 = set(primeFactors(x + 1))
    factor1 = set(primeFactors(x))
    while x < top:   
        factor4 = set(primeFactors(x + 3))
        if len(factor4) == n:
            print(1, x+3, factor4)
            if len(factor3) == n:
                print(2, x)
                if len(factor2) == n:
                    print(3, x)
                    if len(factor1) == n:    
                        return x   
            x = x + 1
            factor1 = factor2
            factor2 = factor3
            factor3 = factor4
        else:
            x = x + 4
            factor3 = set(primeFactors(x + 2))
            factor2 = set(primeFactors(x + 1))
            factor1 = set(primeFactors(x))
    return 

# Finds the first four consecutive integers to have four distinct prime factors each.
def threePrimes(x, top, n):
    factor2 = set(primeFactors(x + 1))
    factor1 = set(primeFactors(x))
    while x < top:   
        factor3 = set(primeFactors(x + 2))
        if len(factor3) == n:
            print(2, x+2, factor3)
            if len(factor2) == n:
                print(3, x)
                if len(factor1) == n:    
                    return x   
            x = x + 1
            factor1 = factor2
            factor2 = factor3
        else:
            x = x + 3
            factor2 = set(primeFactors(x + 1))
            factor1 = set(primeFactors(x))
    return 

n = 4
x = 70000
top = 80000
sol = conPrimes(x, top, n)
print(time.time() - t0, "seconds elapsed")
# next do 30k to 40k
print("the solution is", sol)


