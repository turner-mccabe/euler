# this code solves the problem at the following link: 
# https://projecteuler.net/problem=22

# for information, please visit: 
# https://projecteuler.net/about

import time
from track_time import track_time

# start timer
t0 = time.time()

# read the names file
file = "p022_names.txt"
with open(file) as f:
    content = f.readlines()[0].split('","')

# clean the first and final names in the file
print(content[-1])
content[0] = content[0].replace('"', "")
content[-1] = content[-1].replace('"', "")
print(content[-1])

# set dictionary with letter lookup values:
d = {
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4,
    "E": 5,
    "F": 6,
    "G": 7,
    "H": 8,
    "I": 9,
    "J": 10,
    "K": 11,
    "L": 12,
    "M": 13,
    "N": 14,
    "O": 15,
    "P": 16,
    "Q": 17,
    "R": 18,
    "S": 19,
    "T": 20,
    "U": 21,
    "V": 22,
    "W": 23,
    "X": 24,
    "Y": 25,
    "Z": 26
}

# sort the names
content.sort()
# print(content)

# names_score = letter_score * position_score
# position_score is the index of the name + 1

def find_letter_score(name):
    """ gets the letter score for a name """
    score = 0
    for letter in name:
        score += d[letter]
    return score

# find the total names scores
total_score = 0
for i in range(len(content)): 
    letter_score = find_letter_score(content[i])
    position_score = i + 1
    name_score = letter_score * position_score
    total_score += name_score

# find solution
sol = total_score
print("the solution is", sol)

# print elapsed time
track_time(t0)
