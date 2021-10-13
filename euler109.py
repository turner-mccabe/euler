from time import time
from track_time import track_time
t0 = time()

# build list of possible base dart singles singles_darts:
singles_darts = []
for i in range(20):
    singles_darts.append(i+1)
singles_darts.append(25)

# set up doubles_darts and all_darts lists (all darts will have duplicates, which is OK)
doubles_darts = []
all_darts = []
for x in singles_darts:
    all_darts.append(x)
    all_darts.append(x * 2)
    doubles_darts.append(x * 2)
    if x != 25:
        all_darts.append(x * 3)

# sort the list
all_darts.sort()

print(all_darts)
print(doubles_darts)

# then simulate the possible 3-dart checkouts that combine singles_darts from all darts list and doubles list.
# use a triple nested for loop with breaks and a counter
threshold = 100
count = 0
for i in range(len(all_darts)):
    for j in range(len(all_darts)):
        if j > i:
            break
        for k in range(len(doubles_darts)):
            checkout_score = all_darts[i] + all_darts[j] + doubles_darts[k]
            if checkout_score < threshold:
                count = count + 1

# 2 dart checkouts
for x in range(len(all_darts)):
    for y in range(len(doubles_darts)):
        checkout_score = all_darts[x] + doubles_darts[y]
        if checkout_score < threshold:
            count = count + 1

# there are 21 one-dart checkouts, all are under 100.
# count = count + 21
# this is the loop that will be accurate for all thresholds, even under 100:
for z in range(len(doubles_darts)):
    checkout_score = doubles_darts[z]
    if checkout_score < threshold:
        count = count + 1

print("solution is: ", count)
track_time(t0)