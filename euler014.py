import sys
import time

# this code solves the problem at the following link: 
# https://projecteuler.net/problem=14

# for information, please visit: 
# https://projecteuler.net/about


# start timer
t0 = time.time()

# define main function
def collatz(x):
    count = 1
    n = x
    if n <= 0:
        return None
    while n != 1:
        if n % 2 == 0:
            n = n / 2
            count = count + 1
        else: 
            n = 3 * n + 1
            count = count + 1
    return count

def findLargest(n):
    top_count = 0
    top_input = 0
    minimum = 1
    for i in range(minimum, n):
        temp = collatz(i)
        if temp > top_count:
            top_count = temp
            top_input = i
            print("new top count: ", top_count, "   input was: ", top_input)
    return top_input, top_count



# read in test case as a command line argument
case = int(sys.argv[1])

# # find solution
sol = findLargest(case)
print("the solution is", sol)

# print elapsed time
print(time.time() - t0, "seconds elapsed")