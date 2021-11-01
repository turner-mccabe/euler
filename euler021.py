import time
from track_time import track_time

# this code solves the problem at the following link: 
# https://projecteuler.net/problem=21

# start timer
t0 = time.time()


"""
d(n) = the sum of all divisors of n
amicable numbers are a, b, such that d(a) = b and d(b) = a, where a != b
come up with method of finding all amicable numbers under 10,000. calculate their sum.

under 10k means that we don't have to do very much performance optimization. 
We can probably just test every number, and then find the amicable ones

naive solution:
first, make function to calculate d(n)
then test a bunch of numbers

Improvements:
Primes are not amicable
"""

# see if i've already written a good function for calculating divisors

def sum_divisors(n):
    """ sums all divisors for n """
    sum = 1 
    # the key here is to only search the bottom range of possible values
    # any lower divisor naturally has an upper divisor, so we add both
    numbers = list(range(2, int(n**0.5)+1))
    for lower_divisor in numbers:
        if n % lower_divisor == 0:
            sum = sum + lower_divisor 
            upper_divisor = n / lower_divisor
            if upper_divisor != lower_divisor:
                sum = sum + upper_divisor
    # remove double counting for square numbers
    return int(sum)

# x = sum_divisors(284)

limit = 10000
from library import gen_primes_list
primes = gen_primes_list(limit)
test_list = list(range(limit + 1))
# find list of divisor sums
sd_list = []
for i in test_list:
    sd_list.append(sum_divisors(i))

# test for amicability, add amicable numbers to list
ami_list = []
sum = 0
for index in range(len(sd_list)):
    candidate1 = sd_list[index]
    if candidate1 <= limit:
        candidate2 = sd_list[candidate1]
        if candidate2 == index and candidate1 != candidate2:
            print("amicable pair found: ", candidate1, candidate2)
            ami_list.append(candidate1)
            sum = sum + candidate1

print(ami_list)
print(sum)

track_time(t0)