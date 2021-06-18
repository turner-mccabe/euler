import time

t0 = time.time()

# code for sanitizing the text input:

# string = """
# 75
# 95 64
# 17 47 82
# 18 35 87 10
# 20 04 82 47 65
# 19 01 23 75 03 34
# 88 02 77 73 07 63 67
# 99 65 04 28 06 16 70 92
# 41 41 26 56 83 40 80 70 33
# 41 48 72 33 47 32 37 16 94 29
# 53 71 44 65 25 43 91 52 97 51 14
# 70 11 33 28 77 73 17 78 39 68 17 57
# 91 71 52 38 17 14 91 43 58 50 27 29 48
# 63 66 04 68 89 53 67 30 73 16 69 87 40 31
# 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
# """

# print(string.replace(" ", ", ").replace("\n", "], \n[").replace(" 0", " "))



array = [
[75],
[95, 64],
[17, 47, 82],
[18, 35, 87, 10],
[20, 4, 82, 47, 65],
[19, 1, 23, 75, 3, 34],
[88, 2, 77, 73, 7, 63, 67],
[99, 65, 4, 28, 6, 16, 70, 92],
[41, 41, 26, 56, 83, 40, 80, 70, 33],
[41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
[53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
[70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
[91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
[63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
[4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]
]



def find_next_three(array, params):
    lst = []
    depth = 4

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