# the factors are  [71, 839, 1471, 6857]
# the solution is 6857
# 0.02800607681274414 seconds elapsed

import time
t0 = time.time()

# main function
# efficiently finds all prime factors of n
def primeFactors(n):
    factors = []
    while n > 1:
        factor = smallestPrimeFactor(n)
        factors.append(factor)
        n = round(n / factor)
    return factors

# dependency functions: 

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


# recursive, finds next prime given a list of primes and a starting point
def findNextPrime(primes, x):
    for i in primes:
        if x % i == 0:
            return findNextPrime(primes, x + 2)
    return x

solution = primeFactors(600851475143)
print("the factors are ", solution)
print("the solution is", solution[-1])
print(time.time() - t0, "seconds elapsed")