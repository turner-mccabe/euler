# euler 52
import time
t0 = time.time()

def check(n):
    letters = sorted(list(str(n)))
    if letters == sorted(list(str(n * 2))):
        if letters == sorted(list(str(n * 3))):
            if letters == sorted(list(str(n * 4))):
                if letters == sorted(list(str(n * 5))):
                    if letters == sorted(list(str(n * 6))):
                        return True
    return False

def test(x):
    for n in range(1, x):
        for i in range(10**(n-1), int((10**n)/6)):
            if check(i) == True:
                return i
    return

sol = test(7)
print("solution is ", sol)
print("products ", sol*2, sol*3, sol*4, sol*5, sol*6)
print("total time: ", time.time() - t0)