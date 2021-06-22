import time

t0 = time.time()


# generate list of primes under 1 million 
# sieve of eratosthenes
def gen_primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    # print("range", range(3,int(n**0.5)+1,2))
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
        # print(sieve)
    return [2] + [i for i in range(3,n,2) if sieve[i]]




def solution(n):
    primes = gen_primes(n)
    print(len(primes))
    max = 0
    # odds
    for span in range(21, 544, 2):
        for i in range(1, len(primes) - span):
            s = sum(primes[i:i+span])
            if s in primes:
                max = s
                # print(primes[i:i+span], s, span)
                break
            if s < n:
                continue
            else:
                break
        else:
            break
    return max



sol = solution(1000000)
    





print("solution is :", sol)



print("total time", time.time() - t0)


