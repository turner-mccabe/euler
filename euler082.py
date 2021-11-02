# this code solves the problem at the following link: 
# https://projecteuler.net/problem=82

# for information, please visit: 
# https://projecteuler.net/about

from track_time import track_time
import time

t0 = time.time()

# read the file
text_file = open("p082_matrix.txt", "r")
lines = text_file.read().split(sep="\n")
text_file.close()

values = []
for i in lines[0:-1]:
    temp = []
    for j in i.split(sep=","):
        temp.append(int(j))
    values.append(temp)
# print(len(lines))

# # manually entered short values
# values = [
#     [131, 673, 234, 103, 18],
#     [201, 96, 342, 965, 150],
#     [630, 803, 746, 422, 111],
#     [537, 699, 497, 121, 956],
#     [805, 732, 524, 37, 331]
# ]

"""
Move from the left column to the right column, going up, down or right. 
Finding the minimal path sum. 

if len(values) = side length of the square = x,
At each layer, there are x possible minimum sums to hold after trimming
to go from layer N to layer N+1, there are N^2 paths to check (looping back is never minimal)
each location in layer N must travel to each location in layer N+1 to be sure

The first move from a layer is always to the right. Then, up or down to find the rest of the values for te new layer. 
Moving up or down initially is never going to be minimal compared to starting one cell up or down. 
"""

# search_depth is how many layers to search
def find_next_layer(array, params):
    lst = []
    initial_sum = params[0]
    horiz_position = params[2]
    verti_position = params[1]
    # start by going right: 
    horiz_position = horiz_position + 1
    new_sum = initial_sum +  array[verti_position][horiz_position]
    lst.append([new_sum, verti_position, horiz_position])
    # then try going up  until we hit the top: 
    while verti_position > 0:
        verti_position = verti_position - 1
        new_sum = new_sum + array[verti_position][horiz_position]
        lst.append([new_sum, verti_position, horiz_position])
    # reset verti_position and new sum
    verti_position = params[1]
    new_sum = initial_sum +  array[verti_position][horiz_position]
    # now go down until we hit the bottom:
    while verti_position < len(array[0])-1:
        verti_position = verti_position + 1
        new_sum = new_sum + array[verti_position][horiz_position]
        lst.append([new_sum, verti_position, horiz_position])   
    return lst

# trimming function
# only need to keep the minimum of each final location.    
# # trim to the top output for each ending position
# lst is the list of multiple of these [[inital_sum11, i1, j1], [inital_sum12, i1, j2]]
def trim(lst):
    # get list of unique verti_position values
    pos = [item[1] for item in lst]
    pos = list(set(pos))
    output = []
    for p in pos:
        temp = []
        for element in lst:
            # find all list elements with matching i values for each unique i (pos) value
            if element[1] == p:
                temp.append(element)
        # sorts the temp elements by their initial_sum values, and returns the minimum
        output.append(sorted(temp, key=lambda x: x[0])[0])
    return output

# finds the maximum path through an array, iterating using the find_next_three function
# this runs find_next_layer function until the array is finished
# there are len(array) = x possible starting positions
def min_path(array):
    # find the x starting positions
    pointers = []
    for start_pos in range(len(array)):
        pointers = pointers + find_next_layer(array, [array[start_pos][0], start_pos, 0])
    # trim the first layer of results
    pointers = trim(pointers)
    # print(pointers)
    # iterate through the rest of the array, using the existing pointers
    # while the search_depth is less than the max search_depth
    i = 1
    while i < len(array) - 1:
        sets = []
        # for each current pointer, find the next layer of pointers
        for item in pointers:
            sets = sets + find_next_layer(array, item)
        # trim the overall set of pointers
        pointers = trim(sets)
        # print(pointers)
        # set i to the layer (horiz position) specified in the pointers
        i = pointers[0][2]
    return pointers

# find the solution
out = min_path(values)

print(out)
print("Minimal Path Sum is: ", sorted(out, key=lambda x: x[0])[0][0])
track_time(t0)
