import time

t0 = time.time()

# # read the file
text_file = open("p067_triangle.txt", "r")
lines = text_file.read().split(sep="\n")
text_file.close()

values = []
for i in lines[0:-1]:
    temp = []
    for j in i.split(sep=" "):
        temp.append(int(j))
    values.append(temp)
print(len(values))
# print(values)


# trimming function
# only need to keep the maximum of each final location.    
# # trim to the top output for each ending position
# lst values have the same data structure as params: [inital_sum, i, j]
# lst is the list of multiple of these [[inital_sum11, i1, j1], [inital_sum12, i1, j2]]
def trim(lst):
    pos = [i[2] for i in lst]
    # pos is the j value (left-right)
    # this gets the unique pos values:
    pos = list(set(pos))
    output = []
    for p in pos:
        temp = []
        for element in lst:
            # find all list elements with matching j values for each unique j (pos) value
            if element[2] == p:
                temp.append(element)
        # print("temp")
        # print(temp)
        # sorts the temp elements by their initial_sum values, and returns the maximum
        output.append(sorted(temp, key=lambda x: x[0], reverse=True)[0])
        # print(output)
    return output

# this searches down and diagonally down. It doesn't currently go right
# TODO adjust this for square array
# depth is how many layers to search
def find_next_layers(array, params, depth=3):
    lst = []
    # depth = 3
    # initial sum is the current starting location
    initial_sum = params[0]
    # i and j are the current starting positions
    i = params[1]
    j = params[2]
    # handle cases where search depth would exceed length of the array:
    if len(array) -1 == i:
        return [initial_sum, i, j]
    if len(array) - 1 < i + depth:
        depth = len(array) - 1 - i
    # find sums for each possible path
    # bin(path_num) is a series of zeroes and ones that cover every combo of moving down or moving over
    # bin(path_num) has 16 values, but there are
    # there are 8 possible paths
    # bin(path_num)[2:] cuts off the '0b' string that precedes binary values
    # zfill(depth) adds leading zeroes until the string has length of 4.
    # .replace("1", " 1").replace("0", " 0").split() turns it into an array
    for path_num in range(2 ** depth):
        # print(bin(path_num))
        path = bin(path_num)[2:].zfill(depth).replace("1", " 1").replace("0", " 0").split()
        # path is an array of zeroes and ones based on the binary values of path_num
        # print(path)
        s = initial_sum
        position = j
        # x is an index variable for the path. (values of 0, 1, 2, 3)
        for x in range(depth):
            # position is the j value (left-right). It is incremented when path[x] == 1 (diagonal move)
            position = position + int(path[x])
            # the i value is always incremented in a triangle matrix. because we always move down. this needs to change
            s = s + array[i+1 + x][position]
        lst.append([s, i + depth, position]) # sum and i, j landing coordinates of the path.
        # print(lst)
    # trim to the top output for each ending position
    # lst values have the same data structure as params: [inital_sum, i, j]
    # lst is the list of multiple of these [[inital_sum11, i1, j1], [inital_sum12, i1, j2]]
    # the trim function removes duplicate lst elements with matching i and j values, keeping the highest one
    # will change trim to keep the lowest value for each position
    output = trim(lst)
    # print("trimming")
    return output

# finds the maximum path through an array, iterating using the find_next_three function
# this runs find_next_layers function until the array is finished
def max_path(array):
    pointers = find_next_layers(array, [array[0][0], 0, 0])
    i = 0
    # while the depth is less than the max depth
    while i < len(array) - 1:
        sets = []
        # for each current pointer, find the next layer of pointers
        for item in pointers:
            sets = sets + find_next_layers(array, item)
        # trim the overall set of pointers
        pointers = trim(sets)
        # set i to the vertical position specified in the pointers
        # in a triangle, the vertical position will be the same for all records
        # TODO consider adding a fourth item to the pointers: overall search depth
        i = pointers[0][1]
    return pointers

out = max_path(values)
sol = sorted(out, key=lambda x: x[0], reverse=True)[0][0]

print(out)
print("solution is", sol)

print("total time: ", time.time() - t0)
