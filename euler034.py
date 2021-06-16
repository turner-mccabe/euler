import time

t0 = time.time()

# def factorial(n):
#     if n == 0: 
#         return 1
#     if n == 1: 
#         return 1
#     else:
#         return n * factorial(n - 1)


# replace factorial function with dictionary for speed:
fdict = { 
    0: 1,
    1: 1, 
    2: 2,
    3: 6,
    4: 24,
    5: 120,
    6: 720,
    7: 5040,
    8: 40320,
    9: 362880 
}


def check_factorial(n):
    digits = list(str(n))
    ints = list(map(int, digits))
    fsum = 0
    for i in ints:
        fsum = fsum + fdict[i]
    if fsum == n:
        if n > 3: print(n)
        return True
    return False


def solve(limit):
    valid = list(map(check_factorial, range(limit)))
    return [i for i in range(limit) if valid[i]]

number = 50000
sol = solve(number)

print("sol:", sum(sol)-3)
print("number:", number)
print("total time", time.time() - t0)