from itertools import chain
from tqdm.auto import tqdm
N = "215694783"
N = list(map(int, N))

max_cup = max(N) # 9

def pretty_print(cups, start = 1):
    ret = [start]
    curr = cups[start]
    for _ in range(len(N) - 1):
        ret.append(curr)
        curr = cups[curr]
    return "".join(map(str,ret))

def move(cups, curr, mx = max_cup):
    picked = [cups[curr]]
    for _ in range(2):
        picked.append(cups[picked[-1]])
    
    dest = curr - 1 or mx
    while dest in picked:
        dest = (dest - 1 or mx)


    cups[dest], cups[picked[-1]], cups[curr] = picked[0], cups[dest], cups[picked[-1]]

    return cups[curr]

def p1():
    cups = {x: N[(i + 1) % len(N)] for i, x in enumerate(N)}
    curr = N[0]
    for _ in range(100):
        curr = move(cups, curr)
    k = pretty_print(cups, 1)[1:]
    print(k)
    return k

def p2():
    cups = {x: N[(i + 1) % len(N)] for i, x in enumerate(N)}
    _curr = N[-1]
    for i in range(max_cup + 1, 1_000_001):
        cups[_curr] = i
        _curr = i
    cups[1_000_000] = N[0]


    curr = N[0]
    for _ in tqdm(range(10_000_000)):
        curr = move(cups, curr, 1_000_000)
    a = cups[1]
    b = cups[a]
    print(a, '*', b, '=', end=" ")
    k = a * b
    print(k)
    return k

p1()
p2()