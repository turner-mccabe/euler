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

# adds additional side length to an existing spiral
def addSpiral(existing_side_length, x):
    extra_diagonals = ['', '', '', '']
    for m in range(4):
        x = x + 1 + existing_side_length # skip = 1 + existing side length
        extra_diagonals[m] = x
    return extra_diagonals

# todo look at hash maps instead of lists for checking results

def slowSolve(criterion):
    side_length = 3
    spiral = [1, 3, 5, 7, 9]
    primes = genPrimesList(100000)
    results = 3
    prime_rate = .6
    t_primes = 0
    t_results = 0
    while prime_rate > criterion:
        # iterate spiral
        spiral = addSpiral(side_length, spiral[-1])
        side_length = side_length + 2
        t_prime = time.time()

        # iterate primes if needed 
        if primes[-1] < spiral[-1]:
            primes = genPrimesList(int(1.15*spiral[-1])) 
            if side_length >= 100:
                # clear out unused primes to improve results gen speed
                i = -1
                while primes[i] > spiral[0]:
                    i = i - 1000
                primes = primes[i:]
                print("spiral", spiral[0], "i", i, "prime", primes[0], "prime rate", prime_rate)
                

        t_primes = t_primes + time.time() - t_prime
        t0results = time.time()

        # calculate results
        # for number in spiral:
        #     if number in primes:
        #         results = results + 1
        for number in spiral:
            for prime in primes:
                if prime == number:
                    results = results + 1
                elif prime > number: 
                    break
        prime_rate = results / (side_length*2 - 1)


        # periodically trim the primes list
        le = len(primes)//100
        while spiral[0] > primes[le]:
            primes = primes[le:]



        t_results = t_results + time.time() - t0results   


    print("total primes gen time", t_primes)
    print("total results gen time", t_results)
    return side_length


criterion = 0.1

# # find solution
print("the solution is", slowSolve(criterion))

# print elapsed time
print(time.time() - t0, "seconds elapsed")