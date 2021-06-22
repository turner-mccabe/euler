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



primes = gen_primes(10000)

primes = [i for i in primes if len(str(i))==4]
# print(primes)

def test():
    x = 0
    for p1 in primes:
        for i in range(6, (9973-p1) // 2, 6):
            p2 = i + p1
            if sorted(str(p1)) == sorted(str(p2)):
                if p2 in primes:
                    p3 = i + p2
                    if sorted(str(p1)) == sorted(str(p3)):
                        if p3 in primes:
                            print(p1, p2, p3, i)
                            x = x + 1
    return x 

sol = test()
print("solution is: ", sol)
print("elapsed time: ", time.time() - t0)