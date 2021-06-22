# euler 63
import time 
t0=time.time()

def digital_powers(digits):
    count = 0
    for i in range(9, 0, -1):
        exp = i ** digits
        if len(str(exp)) < digits:
            return count
        elif len(str(exp)) == digits:
            print(i, digits, exp)
            count = count + 1
    return count

def find_all(limit):
    sum = 0
    for n in range(1, limit+1):
        sum = sum + digital_powers(n)
    return sum

# print(digital_powers(2))
sol = find_all(22)
print("solution is: ", sol)
print("total time", time.time() - t0)