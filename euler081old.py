import time

# this code solves the problem at the following link: 
# https://projecteuler.net/problem=81

# for information, please visit: 
# https://projecteuler.net/about

import numpy as np
from track_time import track_time
import time

t0 = time.time()

# # read the file
# text_file = open("p081_matrix.txt", "r")
# lines = text_file.read().split(sep="\n")
# text_file.close()

# values = []
# for i in lines[0:-1]:
#     temp = []
#     for j in i.split(sep=","):
#         temp.append(int(j))
#     values.append(temp)
# print(len(lines))

"""
Note:
this shit is working for half of the array,
but it can't handle when the array options reduce

"""

# manually entered short values
values = [
    [131, 673, 234, 103, 18],
    [201, 96, 342, 965, 150],
    [630, 803, 746, 422, 111],
    [537, 699, 497, 121, 956],
    [805, 732, 524, 37, 331]
]

"""
if len(values) = side length of the square = x,
then there are x-1 expanding jumps, and x-1 contracting jumps
There is also an initial 'jump' that lands us on the top left value.

i is the height, j is the left-right. i could be changed to y, and j changed to x

In total, there are 2(x-1) + 1 numbers selected. (9 in the simple case)
199 numbers will be selected in the big matrix.

The max number of trimmed totals will be equal to x


How to check if find_next_three() will hit a bad index?
params = [initial_sum, i, j], where i, j is the location of the pointer
max values for i, j are x-1

While expanding:
if i+3 > x-1 or j+3 > x-1:
    then do find next two instead
When overall search_depth == x-1, then we start to reduce the possible paths.
"""


# trimming function
# only need to keep the minimum of each final location.    
# # trim to the top output for each ending position
# lst values have the same data structure as params: [inital_sum, i, j, depth]
# lst is the list of multiple of these [[inital_sum11, i1, j1], [inital_sum12, i1, j2]]
# pos can also be used for the i value because the matrix is square
# this also gets the unique pos values:
# pos = range(current_depth + 1)
def trim(lst):
    # get list of unique i or j values
    # for all values, i+j = current_depth
    # we only have to look at i OR j, because the values are symetrical and 1-to-1
    pos = [item[2] for item in lst]
    pos = list(set(pos))
    output = []
    for p in pos:
        temp = []
        for element in lst:
            # find all list elements with matching j values for each unique j (pos) value
            if element[2] == p:
                temp.append(element)
        # sorts the temp elements by their initial_sum values, and returns the minimum
        output.append(sorted(temp, key=lambda x: x[0])[0])
    return output

# search_depth is how many layers to search
def find_next_layers(array, params, search_depth=1):
    lst = []
    # search_depth = 3
    # initial sum is the current starting location
    initial_sum = params[0]
    # i and j are the current starting positions
    i = params[1]
    j = params[2]
    current_depth = params[3]
    # currently, total_rows is for a half-depth search
    total_rows = len(array) -1
    # TODO total_rows = 2*(len(array) -1) + 1 = 2*len(array) - 1
    # handle cases where search search_depth would exceed length of the array:
    # if total_rows == current_depth:
    #     # condition when there are no more rows remaining
    #     return [initial_sum, i, j]
    # if total_rows - current_depth < search_depth:
    #     # reduce search depth if there aren't enough rows left
        # search_depth = total_rows - current_depth
    # find sums for each possible path
    # bin(path_num) is a series of zeroes and ones that cover every combo of moving down or moving over
    # bin(path_num) has 16 values, but there are
    # there are 8 possible paths
    # bin(path_num)[2:] cuts off the '0b' string that precedes binary values
    # zfill(search_depth) adds leading zeroes until the string has length of 4.
    # .replace("1", " 1").replace("0", " 0").split() turns it into an array
    for path_num in range(2 ** search_depth):
        path = bin(path_num)[2:].zfill(search_depth).replace("1", " right").replace("0", " down").split()
        # path is an array of direction instructions based on the binary values of path_num
        s = initial_sum
        horiz_position = j
        verti_position = i
        # x is an index variable for the path. (values of 0, 1, 2, 3)
        for x in range(search_depth):
            # horiz_position is the j value (left-right). It is incremented when path[x] == 1 (diagonal move)
            if path[x] == "right":
                horiz_position = horiz_position + 1
            elif path[x] == "down":
                verti_position = verti_position + 1
            
            # cap the expansion of indexes
            if verti_position >= len(array): 
                verti_position = len(array) - 1
                break
            if horiz_position >= len(array):
                horiz_position = len(array) - 1
                break
            pos_value = array[verti_position][horiz_position]
            s = s + pos_value
        new_depth = horiz_position + verti_position
        lst.append([s, verti_position, horiz_position, new_depth]) # sum and i, j landing coordinates of the path.
    # lst values have the same data structure as params: [inital_sum, i, j]
    # lst is the list of multiple of these [[inital_sum11, i1, j1], [inital_sum12, i1, j2]]
    # the trim function removes duplicate lst elements with matching i and j values,
    # keeping the lowest value for each position
    # print("trimming")
    print(lst)
    # output = trim(lst)
    # print(output)
    output = lst
    return output

# finds the maximum path through an array, iterating using the find_next_three function
# this runs find_next_layers function until the array is finished
def max_path(array):
    pointers = find_next_layers(array, [array[0][0], 0, 0, 0])
    i = 0
    # while the search_depth is less than the max search_depth
    while i <= 2*len(array) - 2:
        sets = []
        # for each current pointer, find the next layer of pointers
        for item in pointers:
            sets = sets + find_next_layers(array, item)
        # trim the overall set of pointers
        print("pre-trimming: ")
        print(sets)
        pointers = trim(sets)
        print("trimmed: ")
        print(pointers)
        # set i to the vertical position specified in the pointers
        # in a triangle, the vertical position will be the same for all records
        # TODO consider adding a fourth item to the pointers: overall search search_depth
        i = pointers[0][3]
        print(i)
    return pointers


# set params
# params = [values[0][0], 0, 0, 0]
# find solution
# x = find_next_layers(values, params)

out = max_path(values)

print(out)
track_time(t0)

def find_next(array, i, j):
    o1 = array[i+1][j]
    o2 = array[i][j+1]
    if o1 < o2:
        return o1
    return o2


def find_next_two(array, i, j):
    o1 = array[i+1][j]
    o2 = array[i][j+1]
    p1 = array[i+2][j]
    p2 = array[i+1][j+1]
    p3 = array[i][j+2]
    q1 = o1 + p1
    q2 = o1 + p2
    q3 = o2 + p2
    q4 = o2 + p3
    lst = [q1, q2, q3, q4]
    return lst
