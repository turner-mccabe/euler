import time

# this code solves the problem at the following link: 
# https://projecteuler.net/problem=19

# for information, please visit: 
# https://projecteuler.net/about

# start timer
t0 = time.time()

"""
solution notes:
there are 12 months per year, so 12 * 100 years = 1200 total months. 
we would expect 1/7 firsts of the month to be sundays, so looking for a solution around 171

increment tally each month by the number of days that pass, and then do mod 7 == 0 to see if it's a sunday
"""
# start at 2 because 1 jan 1901 was a Tuesday
for tally in range(1, 7):
    # tally = 2
    sunday_count = 0
    year = 1901
    # iterate over all years
    while year < 2001:
        # set feb days variable to account for leap years
        feb_days = 28
        # if leap year, adjust feb days
        if year % 4 == 0:
            feb_days = 29
        # number of days in each month, in order
        month_lengths = [31, feb_days, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        # add leap year logic
        for days in month_lengths:
            tally += days
            if tally % 7 == 0:
                sunday_count += 1
        year += 1

    print(sunday_count)

print("elapsed time: ", time.time() - t0)

# note, it literally is 171... exactly average :/
