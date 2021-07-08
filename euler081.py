import time

# this code solves the problem at the following link: 
# https://projecteuler.net/problem=81

# for information, please visit: 
# https://projecteuler.net/about

# start timer
t0 = time.time()

array = [
    [131, 673, 234, 103,  81],
    [201,  96, 342, 965, 150],
    [630, 803, 746, 422, 111],
    [537, 699, 497, 121, 956],
    [805, 732, 524,  37, 331]
]








# find solution
# sol = 
# print("the solution is", sol)
print(time.time() - t0, "seconds elapsed")


# functions from problems 18 and 67, for reference:


def find_next_three(array, params):
    lst = []
    depth = 2
    initial_sum = params[0]
    i = params[1]
    j = params[2]
    # handle cases where search depth would exceed length of the array:
    if len(array) -1 == i:
        return [initial_sum, i, j]
    if len(array) - 1 < i + depth:
        depth = len(array) - 1 - i
    # find sums for each possible path
    for path_num in range(2 ** depth):
        path = bin(path_num)[2:].zfill(depth).replace("1", " 1").replace("0", " 0").split()
        s = initial_sum
        position = j        
        for x in range(depth):
            position = position + int(path[x])
            s = s + array[i+1 + x][position]
        lst.append([s, i + depth, position]) # sum and i, j landing coordinates of the path. 
    # trim to the top output for each ending position
    output = trim(lst)
    return output


# trimming function
# only need to keep the maximum of each final location.     
def trim(lst):
    pos = [i[2] for i in lst]
    pos = list(set(pos))
    output = []
    for p in pos:
        temp = []
        for l in lst:
            if l[2] == p:
                temp.append(l)
        output.append(sorted(temp, key=lambda x: x[0], reverse=True)[0])
    return output

# finds the maximum path through an array, iterating using the find_next_three function
def max_path(array):
    x = find_next_three(array, [array[0][0], 0, 0])
    i = 0
    while i < len(array) - 1:
        sets = []
        for item in x: 
            sets = sets + find_next_three(array, item)
        x = trim(sets)
        i = x[0][1]
    return x

out = max_path(array)
sol = sorted(out, key=lambda x: x[0], reverse=True)[0][0]

print(out)
print("solution is", sol)

print("total time: ", time.time() - t0)


# naieve functions I made while exploring the problem:

def find_next(i, j):
    o1 = array[i+1][j]
    o2 = array[i+1][j+1]
    if o1 > o2: return o1
    return o2


def find_next_two(array, i, j):
    o1 = array[i+1][j]
    o2 = array[i+1][j+1]
    p1 = array[i+2][j]
    p2 = array[i+2][j+1]
    p3 = array[i+2][j+2]
    q1 = o1 + p1
    q2 = o1 + p2
    q3 = o2 + p2
    q4 = o2 + p3
    lst = [q1, q2, q3, q4]
    return lst