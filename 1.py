import itertools
N = [int(x) for x in open('./in/1.txt').readlines()]

def p1():
    for x, y in itertools.product(N, N):
        if x + y == 2020:
            print(f"{x} + {y} = 2020")
            print(f"{x} * {y} = {x * y}")
            return x * y

def p2():
    for x, y, z in itertools.product(N, N, N):
        if x + y + z == 2020:
            print(f"{x} + {y} + {z} = 2020")
            print(f"{x} * {y} * {z} = {x * y * z}")
            return x * y * z
p1()
p2()
