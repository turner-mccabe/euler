# https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n

import time

# sieve of eratosthenes
def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    # print("range", range(3,int(n**0.5)+1,2))
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
        # print(sieve)
    return [2] + [i for i in range(3,n,2) if sieve[i]]


s = 0
x = primes(2000000)
for prime in x:
    s = s + prime
print(s)




# # half sieve (?) this is slower
def primes1(n):
    """ Returns  a list of primes < n """
    sieve = [True] * (n//2)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in range(1,n//2) if sieve[i]]




# a faster variation starting with a third of a sieve:

import numpy
def primesfrom2to(n):
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = numpy.ones(n//3 + (n%6==2), dtype=numpy.bool)
    for i in range(1,int(n**0.5)//3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[       k*k//3     ::2*k] = False
            sieve[k*(k-2*(i&1)+4)//3::2*k] = False
    return numpy.r_[2,3,((3*numpy.nonzero(sieve)[0][1:]+1)|1)]


# A (hard-to-code) pure-python version of the above code would be:

def primes2(n):
    """ Input n>=6, Returns a list of primes, 2 <= p < n """
    n, correction = n-n%6+6, 2-(n%6>1)
    sieve = [True] * (n//3)
    for i in range(1,int(n**0.5)//3+1):
      if sieve[i]:
        k=3*i+1|1
        sieve[      k*k//3      ::2*k] = [False] * ((n//6-k*k//6-1)//k+1)
        sieve[k*(k-2*(i&1)+4)//3::2*k] = [False] * ((n//6-k*(k-2*(i&1)+4)//6-1)//k+1)
    return [2,3] + [3*i+1|1 for i in range(1,n//3-correction) if sieve[i]]

# n = 2000000

# t0 = time.time()
# ans = primes(n)
# print(ans[-1])
# print(time.time() - t0, "seconds elapsed for primes")


# t1 = time.time()
# ans1 = primes1(n)
# print(ans1[-1])
# print(time.time() - t1, "seconds elapsed for half sieve")



