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
    factors = [" "]
    while n > 1:
        factor = smallestPrimeFactor(n)
        if factor != factors[-1]:
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

# main function
# Finds the first N consecutive integers to have N distinct prime factors each (N = digits)
def nested(x, layer, digits):
    length = len(primeFactors(x + digits - layer)) - 1
    if (layer == digits and length == digits):
        return ["solution", x]
    if length == digits:
        if layer>=2: print(layer, x, digits)
        return nested(x, layer+1, digits)
    return [x + 1]


# read in digits as a command line argument
digits = int(sys.argv[1])
x = 10000
layer = 1
top = 100000

while x < top:
    temp = nested(x, layer, digits)
    if temp[0] == "solution":
        sol = temp[1]
        break
    else:
        x = temp[0]

print("the solution is", sol)
print(time.time() - t0, "seconds elapsed")






# Finds the first four consecutive integers to have four distinct prime factors each.
def consecutivePFL(digits):
    x = 10**(digits-1)
    top = 10**digits
    while x < top:   
        print(x)
        if len(primeFactors(x + digits - layer))-1 == digits:
            if len(primeFactors(x + digits - layer))-1 == digits:
                if len(primeFactors(x + digits - layer))-1 == digits:
                    if len(primeFactors(x + digits - layer))-1 == digits:    
                        return x   
                    else: 
                        x = x + digits + layer - 1# layer = 4
                else:
                    x = x + digits + layer - 1# layer = 3
            else:
                x = x + digits + layer - 1# layer = 2
        else:
            x = x + digits + layer - 1 # layer = 1
    return 
