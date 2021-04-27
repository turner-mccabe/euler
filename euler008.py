
import sys
import time

# this code solves the problem at the following link: 
# https://projecteuler.net/problem=8

# for information, please visit: 
# https://projecteuler.net/about

# read in test case as a command line argument
case = int(sys.argv[1])

# start timer
t0 = time.time()

# input block - 1000 digit number
block = """
73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450
"""
# calculates the greatest product of block from aconsecutive run of  n digits


# define main function
def euler2(block, n):
    # ensure that the block argument is used as a string
    string = str(block)
    # remove \n newlines from multiline string
    string = str.join("", string.splitlines())

    # if there is a 0, then the product will be 0
    # therefore, we can eliminate all runs of length < n
    seq = string.split("0")
    result = list(filter(lambda x: len(x) >= n, seq))
    # print("potential result strings", result)

    # candidates will be the list of all possible product strings
    candidates = []
    # now, find the largest product from the result strings 
    for i in result:
        start = 0
        end = n
        while end <= len(i):
            candidates.append(productStr(i[start:end]))
            start = start + 1
            end = end + 1
    return max(candidates)

# finds the product of all digits in a string containing integers
def productStr(string):
    product = 1
    for x in string:
        product = int(x) * product
    return product


# find solution
sol = euler2(block, case)
print("the solution is", sol)


# print elapsed time
print(time.time() - t0, "seconds elapsed")
