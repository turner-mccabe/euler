# this code solves the problem at the following link: 
# https://projecteuler.net/problem=81

# for information, please visit: 
# https://projecteuler.net/about

from track_time import track_time
import time

t0 = time.time()

# read the file
text_file = open("p081_matrix.txt", "r")
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
def find_next_layers(array, params):
    lst = []
    for path in ["right", "down"]:
        # path is an array of direction instructions based on the binary values of path_num
        initial_sum = params[0]
        horiz_position = params[2]
        verti_position = params[1]
        # horiz_position is the j value (left-right). It is incremented when path[x] == 1 (diagonal move)
        if path == "right":
            horiz_position = horiz_position + 1
        elif path == "down":
            verti_position = verti_position + 1
        # cap the expansion of indexes
        if verti_position >= len(array) or horiz_position >= len(array):
            break
        new_sum = initial_sum +  array[verti_position][horiz_position]
        lst.append([new_sum, verti_position, horiz_position])
    return lst

# finds the maximum path through an array, iterating using the find_next_three function
# this runs find_next_layers function until the array is finished
def max_path(array):
    pointers = find_next_layers(array, [array[0][0], 0, 0, 0])
    i = 0
    # while the search_depth is less than the max search_depth
    while i <= 2*len(array) - 3:
        sets = []
        # for each current pointer, find the next layer of pointers
        for item in pointers:
            sets = sets + find_next_layers(array, item)
        # trim the overall set of pointers
        pointers = trim(sets)
        # set i to the layer (vertical position + horiz position) specified in the pointers
        i = pointers[0][2] + pointers[0][1]
    return pointers

out = max_path(values)

print(out)
track_time(t0)
