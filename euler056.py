import sys
import time

# this code solves the problem at the following link: 
# https://projecteuler.net/problem=56

# for information, please visit: 
# https://projecteuler.net/about

# start timer
t0 = time.time()


dictionary = {
    "1": 1,
    "2": 2, 
    "3": 3,
    "4": 4, 
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "0": 0
}


def solution(x):
    l = []
    for a in range(3, x):
        for b in range(3, x):
            exp = str(a ** b)
            if len(exp) >= 100:
                l.append(exp)

    sums = []
    for item in l:
        s = 0
        for char in item:
            s = s + dictionary[char]
        sums.append(s)
    return max(sums)

    
print(solution(100))

# print elapsed time
print(time.time() - t0, "seconds elapsed")