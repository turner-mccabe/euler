import sys
import time
from math import sqrt

# this code solves the problem at the following link: 
# https://projecteuler.net/problem=9

# for information, please visit: 
# https://projecteuler.net/about

# read in test case as a command line argument
case = int(sys.argv[1])

# start timer
t0 = time.time()

# define main function
def eulerFunction(n):
    for a in range(0, n):
        print(a)
        for b in range(a+1, n):
            for c in range(b+1, n):
                s = a + b + c
                # print(a, b, c, s)
                if s == n:
                    sq_dif = a*a + b*b - c*c
                    if sq_dif == 0:
                        print("a triplet: ", a, " ", b, " ", c)
                        print("square difference ", sq_dif)
                        return a*b*c



sol = eulerFunction(case)
print("the solution is", sol)

# print elapsed time
print(time.time() - t0, "seconds elapsed")

# unused:
# # lists all perfect squares below n
# def listSquares(n):
#     l = []
#     i = 1
#     while i < n:
#         l.append(i*i)
#         i = i + 1
#     return l

# # # find solution
# squares_list = listSquares(1000)

# print(squares_list, case)