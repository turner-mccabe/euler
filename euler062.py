import time
t0 = time.time()

# generate cubes up to n**3

def gen_cubes(n, target):
    cubes = sorted([[sorted(list(str(i**3))), i] for i in range(1, n)], key=lambda x: x[0])
    count = 1
    l = []
    for i in range(n-2):
        if cubes[i][0] == cubes[i + 1][0]:
            count = count + 1
        else:
            if count==target:
                l.append(cubes[i+1-count][1])
            count = 1
    sol = sorted(l)[0]
    return sol**3

sol = gen_cubes(70000, 5)
print("solution is ", sol)
print("total time: ", time.time() - t0)