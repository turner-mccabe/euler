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



def circular(n):
    n = str(n)
    length = len(n)
    digits = list(n)
    for i in digits:
        if i in ['2', '4', '5', '6', '8', '0']:
            return None
    digits = digits + list(n)
    rotations = []
    output = []
    for i in range(length):
        rotations.append(digits[i:i+length])
    for i in rotations:
        output.append(''.join(i))
    circle = list(map(int, output))
    return circle


def solve(n):
    primes = gen_primes(n)
    count = 2
    threshold = 0
    for i in primes:
        if i > threshold:
            threshold = 10 ** len(str(i))
            prime_list = gen_primes(threshold)
            print("length change: ", threshold)
        circle = circular(i)
        if circle == None:
            continue
        for j in circle:
            if j not in prime_list:
                break
            else:
                continue
        else:
            for x in circle:
                if x > i:
                    prime_list.remove(x)
                    count = count + 1
            prime_list.remove(i)
            count = count + 1
            # print(i, j)
    return count


def slow_solve(n):
    primes = gen_primes(n)
    count = 0
    for i in primes:
        circle = circular(i)
        if circle == None:
            continue
        for j in circle:
            if j not in primes:
                break
            else:
                continue
        else:
            count = count + 1
    return count


# generates the set of circular numbers for n, not including n
def fast_circular(n):
    n = str(n)
    digits = list(n) + list(n)
    output = []
    for i in range(1, len(n)):
        output.append(int(''.join(digits[i:i+len(n)])))
    return output

# trims out even digits and 5 from list of primes below n
# finds circular permutations of each prime
# quickly determines if a number can be a circular prime
def fast_solve(n):
    primes = gen_primes(n)
    prime_list = []
    for p in primes:
        for char in list(str(p)):
            if char in ['2', '4', '5', '6', '8', '0']:
                break
            else:
                continue
        else:
            prime_list.append(p)
    count = 2
    for i in prime_list:
        circle = fast_circular(i)
        for j in circle:
            if j not in prime_list:
                break
            else:
                continue
        else:
            count = count + 1
    return count


sol = fast_solve(1000000)
print("sol:", sol)



print("total time", time.time() - t0)


