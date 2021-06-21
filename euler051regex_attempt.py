import re
import time
t0 = time.time()

# sieve of eratosthenes    
""" Returns  a list of primes < n """
def gen_primes(n):
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]



# https://projecteuler.net/problem=51
# Notes on the problem:

# for this problem, we should look at digit similarities. 

# the final digit of all candidate primes will be 1, 3, 7, or 9, 
# so the final digit can't be the one that is replacable

# the number of digits to be replaced is unknown. 


# string format will be 1*24*o, where * is replaced by any number, and o is replaced by ones
def prime_occurences(format_string, primes):
    maxi = 0
    for ones in ["1", "3", "7", "9"]:
        count = 0
        # use regex to find matches:
        item = format_string.replace("o", ones)
        matches = re.findall(item, primes)
        # print(item, matches)
        count = len(matches)
        if count > maxi and count < 10: 
            maxi = count
        if count == 8: 
            print(count, item, matches)
            # print("total time", time.time() - t0)
            # exit()
    # print(format_string, maxi)
    return maxi

def multi_digit_check(n):
    # create a list of primes as strings:
    primes = list(map(str, gen_primes(10**n)))
    maxi = []
    format_codes = []

    # use binary to generate all possible patterns for a given digit amount
    digits = n-1
    for variation in range(2 ** digits - 1):
        code = bin(variation)[2:].zfill(digits).replace("1", "a").replace("0", ".") + "o"
        format_codes.append(code)
    # print(format_codes)
        
    # print(primes)
    primes = [i for i in primes if len(i) == n]
    primes = "\n".join(primes)

    # test all format codes to see which has the most prime digit replacements
    for raw in format_codes:
        maxi.append(flexi_replace(raw, primes))

    return sorted(maxi, reverse=True)[0]




def flexi_replace(raw, primes):
    maxi = []
    lst = list(raw)
    trials = [raw]

    while "a" in lst:
        new = []
        for item in trials:
            for i in range(1, 10):
                format_string = item.replace("a", str(i), 1)
                new.append(format_string)
        trials = new
        lst = list(trials[0])

    for string in trials:
        maxi.append(prime_occurences(string, primes))

    return sorted(maxi, reverse=True)[0]



def regex_check(n):
    # create a list of primes as strings:
    primes = list(map(str, gen_primes(10**n)))
    primes = [i for i in primes if len(i) == n]
    primes = "\n".join(primes)

    format_codes = []

    # use binary to generate all possible patterns for a given digit amount
    digits = n-1
    for variation in range(2 ** digits - 1):
        code = bin(variation)[2:].zfill(digits).replace("1", "a").replace("0", ".") + "o"
        format_codes.append(code)
    # print(format_codes)
        
    # print(primes)


    # test all format codes to see which has the most prime digit replacements
    for raw in format_codes:
        maxi.append(flexi_replace(raw, primes))

    return sorted(maxi, reverse=True)[0]


sol = multi_digit_check(6)
print("solution is", sol)

print("total time", time.time() - t0)
