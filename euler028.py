import sys
import time
import numpy
from math import floor

# this code solves the problem at the following link: 
# https://projecteuler.net/problem=28

# for information, please visit: 
# https://projecteuler.net/about

# read in test case as a command line argument
case = int(sys.argv[1])

# start timer
t0 = time.time()

# use the pattern geometry of the spiral to calculate sum
#   without needing to actually make the spiral
def sumDiagonals(n):
    maximum = n * n
    s = 1
    x = 1
    skip = 2
    # every four loops, increase how many numbers are skipped
    while x < maximum:
        for i in range(4):
            x = x + skip
            print(x)
            s = s + x 
        skip = skip + 2
    return s


# find solution
sol = sumDiagonals(case)
# sol = createSpiral(case)
print("the solution is", sol)

# print elapsed time
print(time.time() - t0, "seconds elapsed")


# define spiral creation function
# this function works to create the spiral, but it currently fails on the very last pass
# dropping this effort for now, because there is a much easier way to calculate spiral sums
def createSpiral(n): 
    # create multi-dim matrix by providing shape
    matrix = numpy.empty(shape=(n, n),dtype='object')
    print(matrix)

    # finds the middle of the spiral
    center = floor(n/2)

    # counter value tells how far to move along the spiral
    # it increments every two direction changes
    counter = 1

    # entry is the value written to the spiral. 
    # It increments on each write to the matrix
    entry = 1

    # initiate longitude and latitude values
    longitude = center
    latitude = center

    # set the center of the matrix to 1
    matrix[center][center] = entry
    print("")
    print(matrix)
    # increment entry
    entry = entry + 1

    maximum = n * n    
    while entry <= maximum:
        for i in range(0, counter): 
            latitude = latitude + 1 # move right
            matrix[longitude][latitude] = entry
            entry = entry + 1 
        print("")
        print(counter)
        print(matrix)

        for i in range(0, counter):
            longitude = longitude + 1 # move down 
            matrix[longitude][latitude] = entry
            entry = entry + 1 

        # increment counter every two directions moved in:
        counter = counter + 1 
        print("")
        print(counter)
        print(matrix)

        for i in range(0, counter):
            latitude = latitude - 1 # move left
            matrix[longitude][latitude] = entry
            entry = entry + 1 
        print("")
        print(counter)
        print(matrix)

        for i in range(0, counter):
            longitude = longitude - 1 # move up
            matrix[longitude][latitude] = entry
            entry = entry + 1 

        # increment counter every two directions moved in:
        counter = counter + 1 
        print("")
        print(counter)
        print(matrix)

    return matrix

