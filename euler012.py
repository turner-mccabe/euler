import time

t0 = time.time()

# only used for initial triangle generation
def gen_triangle(n):
    return sum(range(1, n+1))

def check_divisors(n):
    count = 2 
    if n % 2 == 0:
        count = 4
    # the key here is to only search the bottom range of possible values
    # any lower divisor naturally has an upper divisor, so we count 2
    numbers = list(range(3, int(n**0.5)))
    for item in numbers:
        if n % item == 0:
            count = count + 2
    return count

def solve(divisors, term): 
    i = 0
    num = gen_triangle(term)
    while i < divisors:
        term = term + 1
        num = num + term
        i = check_divisors(num) 
    return [num, term]



divisors = 500
term = 1
sol = solve(divisors, term)

print("sol:", sol[0], " term: ", sol[1])
print("total time", time.time() - t0)