import sys
import time

# this code solves the problem at the following link: 
# https://projecteuler.net/problem=58

# for information, please visit: 
# https://projecteuler.net/about

# start timer
t0 = time.time()

# sieve of eratosthenes
def genPrimesList(n):
    """ Input n>=6, Returns a list of primes, 2 <= p < n """
    n, correction = n-n%6+6, 2-(n%6>1)
    sieve = [True] * (n//3)
    for i in range(1,int(n**0.5)//3+1):
      if sieve[i]:
        k=3*i+1|1
        sieve[      k*k//3      ::2*k] = [False] * ((n//6-k*k//6-1)//k+1)
        sieve[k*(k-2*(i&1)+4)//3::2*k] = [False] * ((n//6-k*(k-2*(i&1)+4)//6-1)//k+1)
    return [2,3] + [3*i+1|1 for i in range(1,n//3-correction) if sieve[i]]

# creates an array of the diagonals of a spiral. uses addSpiral()
def spiralDiagonals(side_length):
    diagonals = [1]
    existing_side_length = 1
    while existing_side_length < side_length:
        diagonals.extend(addSpiral(existing_side_length, diagonals))
        existing_side_length = int((len(diagonals) - 1) / 2 + 1)
    return diagonals

# adds additional side length to an existing spiral
def addSpiral(existing_side_length, diagonals):
    x = diagonals[-1]
    extra_diagonals = []
    skip = 1 + existing_side_length
    for i in range(4):
        x = x + skip
        extra_diagonals.append(x)
    return extra_diagonals



# one-time search for results
def checkResults(primes_list, numbers_list):
    results = []
    for number in numbers_list:
        if number in primes_list:
            results.append(True)
        # else:
        #     results.append(False)
    return results

# todo look at hash maps instead of lists for checking results

def slowSolve(criterion):
    side_length = 3
    spiral = spiralDiagonals(side_length)
    primes = genPrimesList(spiral[-1])
    results = sum(checkResults(primes, spiral))
    spiral_count = len(spiral)
    prime_rate = results/len(spiral)
    t_primes = 0
    t_results = 0
    while prime_rate > criterion:
        # iterate spiral
        spiral = addSpiral(side_length, spiral)
        spiral_count = spiral_count + 4
        side_length = side_length + 2

        # iterate primes if needed 
        t_prime = time.time()
        while primes[-1] < spiral[-1]:
            primes = genPrimesList(int(round(1.1*spiral[3])) + 10) 
            if side_length >= 100:
                # clear out unused primes to improve results gen speed
                primes = [prime for prime in primes if prime >= spiral[0]]
        t_primes = t_primes + time.time() - t_prime

        # calculate results
        t0results = time.time()
        results = results + sum(checkResults(primes, spiral[-4:]))
        prime_rate = results/spiral_count
        print("side_length", side_length, "prime_rate", prime_rate)
        t_results = t_results + time.time() - t0results

    print("total primes gen time", t_primes)
    print("total results gen time", t_results)
    return side_length


def isPrime(primes_list, x):
    for i in primes_list:
        if x % i == 0:
            return False
    return True
 
def findNextPrime(primes_list):
    # start with x = largest prime + 2 (not plus 1 since primes > 2 can't be even)
    x = primes_list[-1] + 2
    while isPrime(primes_list, x) == False:
        x = x + 2
        checkPrime = isPrime(primes_list, x)
    return x      










# print(spiralDiagonals(25000)[-1])
# x = genPrimesList(625050001)
# print(x[-1])
# print(findNextPrime(x))
# # read in test case as a command line argument
# case = int(sys.argv[1])
criterion = 0.1

# # find solution
print("the solution is", slowSolve(criterion))

# print elapsed time
print(time.time() - t0, "seconds elapsed")