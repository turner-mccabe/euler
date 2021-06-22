import time
t0 = time.time()




# generate list of primes under 1 million 
# sieve of eratosthenes
def gen_primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]



# resilient fractions are any primes that are NOT prime factors of the denominator


def find_prime_divisors(n, primes):
    ''' finds all prime divisors for a given number '''
    divisors = set()
    i = 0
    while primes[i] <= int(n*0.5) + 1:
        if n % primes[i] == 0: # if n is divisible by the prime, add to list
            divisors.add(primes[i])
            # # cut off running early if the number is divisible by 2. runs twice as fast, but results are incomplete for even numbers
            # if primes[i] == 2:
            #     return divisors
        i = i + 1
    return divisors


# latest notes:
# how to find the resilience:
# find the prime factorization of the numerator and the prime factorization of the denominator
# if any of the prime factors of a numerator are a prime factor of the denominator, then the fraction is not resilient
# for example, 10/12.
# numerator prime factors are 5 and 2. Denominator prime factors are 2 (squared) and 3
# they share a common prime factor, 2. because of this, the fraction is not resilient.

# if we had a dictionary or list of the prime factorization of each number, 
#   we could search the list to see if each numerator shares any possible factors with the denominator

# improvement: even numbers will always be non-resilient, so don't need to be tested for

# pretty sure this fn is O(n^2) time complexity
def gen_divisors(n):
    ''' generates a dictionary of prime divisors of all numbers 2 thru n '''
    primes = gen_primes(n+10)
    pd_dict = {}
    # finds prime divisors for even numbers only 
    for i in range(2, n+1):
        pd_dict[i] = find_prime_divisors(i, primes)
    return pd_dict





# this function compares prime factors 
# uses dictionaries and sets to improve performance
def resilience(denom, pd_dict):
    res = denom - 1
    denom_set = pd_dict[denom]
    # ignore denominators with < 8 distinct prime factors
    # if len(denom_set) < 9:
    #     return 1
    for n in range(2, denom - 1):
        # print(n, pd_dict[n] & pd_dict[denom])
        if pd_dict[n] & denom_set:
            res = res - 1
    return res / (denom - 1)


def solve(numerator, denominator, n):
    t1 = time.time()
    pd_dict = new_gen_divisors(n)
    dict_gen_time = time.time() - t1
    target = numerator/denominator
    print("target = ", target)

    i = 30030
    res = resilience(i, pd_dict)
    while res >= target:
        i = i + 30030
        if i > n -1:
            t1 = time.time()
            n= i * 2
            pd_dict = new_gen_divisors(n)
            dict_gen_time = time.time() - t1
        res = resilience(i, pd_dict)
        # if res != 1:
        print(i, res)
    print("dictionary gen time", dict_gen_time)
    return i



# time complexity: 
# I think this is O(n^2) time complexity. It runs 100 times longer for 10x larger n value
def new_gen_divisors(n):
    ''' combines gen_divisors() and find_prime_divisors() with no performance difference '''
    primes = gen_primes(n+10)

    pd_dict = {}
    # finds prime divisors 
    for num in range(2, n+1):
        divisors = set()
        i = 0
        special_condition = num % 30
        # only search half of the range of the number
        while primes[i] <= 97:
            if num % primes[i] == 0: # if n is divisible by the prime, add to list
                divisors.add(primes[i])
                # cut off running early if the number is divisible by 2. runs twice as fast, but results are incomplete for even numbers
                if special_condition != 0:
                    if primes[i] == 2:
                        break
                    if primes[i] == 3:
                        break
                    if primes[i] == 5:
                        break
                    # if primes[i] == 7:
                    #     break
                    # if primes[i] == 11:
                    #     break
                    # if primes[i] == 13:
                    #     break
                    # if primes[i] == 17:
                    #     break
                    # if primes[i] == 19:
                    #     break
            i = i + 1
        if len(divisors) == 0: # manually add number if it is prime
            divisors.add(num)
        pd_dict[num] = divisors
        # print(num, pd_dict[num], len(pd_dict[num]))
    return pd_dict




# res = resilience(3933930, sol)
# print(sol[3933930])
# print(res)

# sol = solve(15499, 94744, 2000000)
# sol = solve(35, 100)
# print("solution is: ", sol)


# best version for future prime factor use
def reusable_prime_factors(n):
    ''' returns distinct prime factors of #s 2 thru n as a dictionary '''
    primes = gen_primes(n+10)
    pd_dict = {}
    # finds prime divisors 
    for num in range(2, n+1):
        divisors = set()
        i = 0
        # only search half of the range of the number
        while primes[i] <= n//2 + 1:
            if num % primes[i] == 0: # if n is divisible by the prime, add to list
                divisors.add(primes[i])
            i = i + 1
        if len(divisors) == 0: # manually add number if it is prime
            divisors.add(num)
        pd_dict[num] = divisors
        # print(num, pd_dict[num], len(pd_dict[num]))
    return pd_dict



# sol = reusable_prime_factors(10000)

# for i in sol:
#     x = 0
#     if len(sol[i]) >= 5:
#         x = x + 1
#         print(i, sol[i], resilience(i, sol))



# Final solution:

# these functions don't require the set of all primes to be calculated. 
# they ALSO don't require the dictionary to be calculated. 
# this code is Very easy on memory, and only requires like 10 primes to be known
# takes advantage of the fact that we know it must be the lowest prime with n factors, where n is unknown
def c_resilience(n, primes_range):
    res = n - 1 
    res = res - (n // 2 - 1) # takes care of even numbers. 25% faster
    for num in range(3, n-1, 2):
        # only search primes_range, the prime factors of n
        for i in primes_range[1:]:
            if num % i == 0: # if n is divisible by a prime factor of n, count it
                res = res - 1
                break # this break is required. 50% faster
    return res / (n - 1)



def o_resilience(n, primes_range):
    res = n - 1 
    res = res - (n // 2 - 1) # takes care of even numbers. 25% faster
    res = res - (n // 6) # takes care of threes. 10% faster
    # for num in range(3, n-1, 2):
    num = 5
    accel = 0
    while num < n:
        # only search primes_range, the prime factors of n
        for i in primes_range[2:]:
            if num % i == 0: # if n is divisible by a prime factor of n, count it
                res = res - 1
                break # this break is required. 50% faster
        if accel == 0:
            num = num + 2
            accel = 1
        else:
            num = num + 4
            accel = 0
    return res / (n - 1)



def solution(target):
    primes = gen_primes(100)
    i = 1
    x = 2*primes[i]
    
    res = o_resilience(x, primes[0:i+1])
    print(x, primes[0:i+1], res)
    while res > target:
        i = i + 1
        x = x*primes[i]
        res = o_resilience(x, primes[0:i+1])
        print(x, primes[0:i+1], res)
    return x


def small_solution():
    factors = [2, 3, 5, 7, 11, 13, 17, 23, 29]
    x = 1
    for f in factors:
        x = x * f
    res = c_resilience(x, factors)
    print(x, factors, res)
    return x


# sol = small_solution()
# print("a solution is ", sol)


sol = solution(15499/94744)
print("a solution is ", sol)
print("elapsed time: ", time.time() - t0)


# 
# 
# 
# 
# 
# 
# 
# 
# 


# these functions don't require the set of all primes to be calculated. 
# however, they throw a memory error eventually, because the dictionary takes up space
def targeted_prime_factors(n, primes_range):
    ''' returns distinct prime factors of #s 2 thru n as a dictionary '''
    pd_dict = {}
    # finds prime divisors 
    for num in range(2, n):
        divisors = set()
        # only search half of the range of the number
        for i in primes_range:
            if num % i == 0: # if n is divisible by the prime, add to list
                divisors.add(i)
        if len(divisors) >= 0: # Only add entry to the dictionary if there is a divisor
            pd_dict[num] = divisors
        # print(num, pd_dict[num])
    return pd_dict


# this function compares prime factors 
# uses dictionaries and sets to improve performance
def altered_resilience(denom, pd_dict, x_factors):
    res = denom - 1
    denom_set = set(x_factors)
    for n in range(2, denom - 1):
        # print(n, pd_dict[n] & pd_dict[denom])
        if pd_dict[n] & denom_set:
            res = res - 1
    return res / (denom - 1)


def older_solution(n):
    primes = gen_primes(100)
    print(primes)
    print(primes[0])
    target = n
    x = 2
    i = 1
    x = x*primes[i]
    print("x is  ", x)
    print(primes[0:i+1])

    pf_dict = targeted_prime_factors(x, primes[0:i+1])
    res = altered_resilience(x, pf_dict, primes[0:i+1])
    print(x, primes[0:i+1], res)
    while res > target:
        i = i + 1
        x = x*primes[i]
        pf_dict = targeted_prime_factors(x, primes[0:i+1])
        res = altered_resilience(x, pf_dict, primes[0:i+1])
        print(x, primes[0:i+1], res)
    return x

