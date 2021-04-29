import sys
import time

# this code solves the problem at the following link: 
# https://projecteuler.net/problem=58

# for information, please visit: 
# https://projecteuler.net/about

# start timer
t0 = time.time()

# slowSolve() is the main function. it is actually faster than solve()

# sieve of eratosthenes
def genPrimesList(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    # print("range", range(3,int(n**0.5)+1,2))
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
        # print(sieve)
    return [2] + [i for i in range(3,n,2) if sieve[i]]



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
# not too slow to run
def checkResults(primes_list, numbers_list):
    results = []
    for number in numbers_list:
        if number in primes_list:
            results.append(True)
        else:
            results.append(False)
    return results

def solve(side_length, criterion):
    spiral = spiralDiagonals(side_length)
    primes = genPrimesList(spiral[-1])
    results = checkResults(primes, spiral)

    prime_rate = sum(results)/len(results)

    t_spiral = 0
    t_primes = 0
    t_results = 0

    while prime_rate > criterion:
        print("")
        # # criteria for skipping side length iterations
        # # this should be mathematically sound because of percentages
        # # could possibly be even more aggressive
        t0spiral = time.time()
        if side_length > 100:
            if prime_rate <= criterion*1.02:
                increment = 2
            else:
                # dynamically adjusts side length interval
                percent_dif = 100 * (prime_rate / criterion - 1)
                # print(percent_dif)
                saftey_factor = 0.9
                # weight = (side_length - 100)/4
                increment = int(round(saftey_factor * percent_dif))
                if increment % 2 != 0: increment = increment - 1
                if increment < 2: increment = 2
                print("final increment", increment)
        else:
            increment = 2
        
        # set side length iteration
        side_length = side_length + increment
        print("side_length", side_length)


        # spiral.extend(addSpiral(side_length, spiral)) # code for adding increments to the spiral
        spiral = spiralDiagonals(side_length)    # code for recreating the diagonal. Allows us to skip side_length steps above

        t_spiral = t_spiral + time.time() - t0spiral

        while primes[-1] < spiral[-1]:
            t_prime = time.time()
            primes = genPrimesList(int(round(1.2*spiral[-1]))) #TODO optimize
            print("prime finding time:", time.time() - t_prime)
            print("added primes up to:", primes[-1])
            t_primes = t_primes + time.time() - t_prime

        t0results = time.time()
        #TODO improve results checking performance
        # print(spiral)
        results.extend(checkResults(primes, spiral[-2*increment:]))
        # print("official results: ", results)
        prime_rate = sum(results)/len(results)

        t_results = t_results + time.time() - t0results

        print("prime_rate", prime_rate)


    print("total spiral gen time", t_spiral)
    print("total primes gen time", t_primes)
    print("total results gen time", t_results)
    return side_length

# one-time search for results
# not too slow to run
def checkResults1(primes_list, numbers_list):
    results = []
    for number in numbers_list:
        if number in reversed(primes_list):
            results.append(True)
    return results

def slowSolve(criterion):
    side_length = 3
    spiral = spiralDiagonals(side_length)
    primes = genPrimesList(spiral[-1])
    results = checkResults(primes, spiral)

    prime_rate = sum(results)/len(spiral)

    t_spiral = 0
    t_primes = 0
    t_results = 0
    increment = 2

    while prime_rate > criterion:
        print("")

        # iterate spiral
        t0spiral = time.time()
        spiral.extend(addSpiral(side_length, spiral))
        side_length = side_length + increment
        print("side_length", side_length)
        t_spiral = t_spiral + time.time() - t0spiral

        # iterate primes if needed 
        while primes[-1] < spiral[-1]:
            t_prime = time.time()
            primes = genPrimesList(int(round(1.2*spiral[-1]))) 
            if side_length >= 200:
                # clear out unused primes to improve results gen speed
                primes = [prime for prime in primes if prime >= spiral[-5]]
            print("prime finding time:", time.time() - t_prime)
            print("added primes up to:", primes[-1])
            t_primes = t_primes + time.time() - t_prime

        # calculate results
        t0results = time.time()
        results.extend(checkResults(primes, spiral[-2*increment:]))
        prime_rate = sum(results)/len(spiral)

        t_results = t_results + time.time() - t0results

        print("prime_rate", prime_rate)


    print("total spiral gen time", t_spiral)
    print("total primes gen time", t_primes)
    print("total results gen time", t_results)
    return side_length



# # read in test case as a command line argument
# case = int(sys.argv[1])
criterion = 0.1

# find solution
sol = slowSolve(criterion)
print("the solution is", sol)

# print elapsed time
print(time.time() - t0, "seconds elapsed")


