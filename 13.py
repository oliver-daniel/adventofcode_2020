import functools
import itertools
import sys

N = """
939
7,13,x,x,59,x,31,19
""".split('\n')[1:-1]

N = open('./in/13.txt').readlines()

DEPARTURE = int(N[0])
BUSES = [int(x) if x != 'x' else 'x' for x in N[1].split(',')]
# there's gonna be something to do with those x's.


def p1():
    P1_BUSES = [bus for bus in BUSES if bus != 'x']
    for i in itertools.count():
        for bus in P1_BUSES:
            if (DEPARTURE + i) % bus == 0:#if divides(bus, DEPARTURE + i):
                print(f'Found a bus with id {bus} leaving at {DEPARTURE + i}')
                print(f'{i} * {bus} = {(k:= i * bus)}')
                return k

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(*ns):
    ret = 1
    for n in ns:
        ret *= n // gcd(ret, n)
    return ret

@functools.cache
def divides(k, n):
    try:
        if n <= k:
            return n == k
        return divides(k, n - k)
    except RecursionError:
        return n % k == 0

def p2():
    N_ = lcm(*[bus for bus in BUSES if bus != 'x'])
    t = 0
    for i, bus in enumerate(BUSES):
        if bus == 'x':
            continue
        y = N_ // bus
        z = pow(y, -1, bus)
        t += (bus - i) * y * z
        print(i, bus, t)
    print(t % N_)
    return t



p1()
print('----')
p2()