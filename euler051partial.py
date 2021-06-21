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
        # since there are only two digits, we only need to check the first digit. 
        for i in range(1, 10):
            item = format_string.replace("*", str(i)).replace("o", ones)
            if item in primes:
                count = count + 1
        if count == 8:
            print(item, format_string, count)
        if count > maxi: 
            maxi = count
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
        code = bin(variation)[2:].zfill(digits).replace("1", "a").replace("0", "*") + "o"
        format_codes.append(code)
        
    print(primes[-1])
    primes = [i for i in primes if len(i) == n]

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



sol = multi_digit_check(6)
print("solution is", sol)

print("total time", time.time() - t0)





# functions created during testing: 

# lets make a function to test 2 digit numbers:

# def two_digit_check():
#     # create a list of primes as strings:
#     primes = list(map(str, gen_primes(99)))
#     maxi = 0

#     for ones in ["1", "3", "7", "9"]:
#         count = 0
        
#         # since there are only two digits, we only need to check the first digit. 
#         for i in range(1, 10):
#             item = str(i) + ones 
#             if item in primes:
#                 count = count + 1
#                 # print(item)
#         print("*", ones, count)
#         if count > maxi: 
#             maxi = count
#     return maxi



# def three_digit_check():
#     # create a list of primes as strings:
#     primes = list(map(str, gen_primes(999)))
#     maxi = 0

#     for ones in ["1", "3", "7", "9"]:
#         count = 0
        
#         # since there are three digits, we need to check the first and second digits, and both

#         # check both: 
#         for i in range(1, 10):
#             item = str(i) + str(i) + ones 
#             if item in primes:
#                 count = count + 1
#                 # print(item)
#         print("* *", ones, count)
#         if count > maxi: 
#             maxi = count

#         for tens in range(1, 10):
#             # check tens
#             count = 0
#             for i in range(1, 10):
#                 item = str(i) + str(tens) + ones 
#                 if item in primes:
#                     count = count + 1
#                     # print(item)
#             print("*", tens, ones, count)
#             if count > maxi: 
#                 maxi = count
            
#             # check hundreds
#             count = 0
#             for i in range(1, 10):
#                 item = str(tens) + str(i) + ones 
#                 if item in primes:
#                     count = count + 1
#                     # print(item)
#             print(tens, "*", ones, count)
#             if count > maxi: 
#                 maxi
#     return maxi



# def replace_a(raw, primes):
#     maxi = []
#     for i in range(1, 10):
#         format_string = raw.replace("a", str(i))
#         maxi.append(prime_occurences(format_string, primes))
#     return sorted(maxi, reverse=True)[0]

# def replace_b(raw, primes):
#     maxi = []
#     for i in range(1, 10):
#         format_string = raw.replace("b", str(i))
#         maxi.append(replace_a(format_string, primes))
#     return sorted(maxi, reverse=True)[0]




# def multi_digit_check():
#     # create a list of primes as strings:
#     primes = list(map(str, gen_primes(9999)))
#     maxi = []
#     # check both: 
#     maxi.append(flexi_replace("**o", primes))
#     # check tens
#     raw = "a*o"
#     maxi.append(flexi_replace(raw, primes))
#     # check hundreds
#     raw = "*ao"
#     maxi.append(flexi_replace(raw, primes))

#     # check thousands: 
#     # check all three
#     maxi.append(flexi_replace("***o", primes))

#     # check tens hundreds
#     raw = "a**o"
#     maxi.append(flexi_replace(raw, primes))
    
#     # check hundreds thousands
#     raw = "**ao"
#     maxi.append(flexi_replace(raw, primes))

#     # check tens thousands
#     raw = "*a*o"
#     maxi.append(flexi_replace(raw, primes))

#     # check tens
#     raw = "aa*o"
#     maxi.append(flexi_replace(raw, primes))
    
#     # check hundreds
#     raw = "a*ao"
#     maxi.append(flexi_replace(raw, primes))

#     # check thousands
#     raw = "*aao"
#     maxi.append(flexi_replace(raw, primes))


#     # check ten-thousands: 
#     # check all four
#     maxi.append(prime_occurences("****o", primes))

#     # check tens hundreds
#     raw = "ba**o"
#     maxi.append(replace_a(raw, primes))
    
#     # check hundreds thousands
#     raw = "b**ao"
#     maxi.append(replace_a(raw, primes))

#     # check tens thousands
#     raw = "b*a*o"
#     maxi.append(replace_a(raw, primes))

#     # check tens
#     raw = "cba*o"
#     maxi.append(replace_b(raw, primes))
    
#     # check hundreds
#     raw = "cb*ao"
#     maxi.append(replace_b(raw, primes))

#     # check thousands
#     raw = "c*bao"
#     maxi.append(replace_b(raw, primes))

#     # check tenthousands
#     raw = "*cbao"
#     maxi.append(replace_b(raw, primes))

#     return sorted(maxi, reverse=True)[0]
