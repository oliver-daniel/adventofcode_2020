from enum import Enum

data = open('./in/12.txt').readlines()

DIRNS = 'ESWN'


def p1():
    dx = 0
    dy = 0
    facing = 0

    def N(n):
        nonlocal dx, dy
        dy += n

    def S(n):
        nonlocal dx, dy
        dy -= n

    def E(n):
        nonlocal dx, dy
        dx += n

    def W(n):
        nonlocal dx, dy
        dx -= n

    for dirn, *dist in data:
        dist = int("".join(dist))
        if dirn in DIRNS:
            eval(f'{dirn}({dist})')
        elif dirn == 'L':
            deg = dist // 90
            facing -= deg
            if facing < 0: facing += 4
        elif dirn == 'R':
            deg = dist // 90
            facing += deg
            facing %= 4
        else:  #F
            eval(f'{DIRNS[facing]}({dist})')
    dx = abs(dx)
    dy = abs(dy)
    print(dx, dy, dx + dy)
    return dx + dy


def p2():
    wx = 10
    wy = 1
    dx = 0
    dy = 0

    def N(n):
        nonlocal wx, wy, dx, dy
        wy += n

    def S(n):
        nonlocal wx, wy, dx, dy
        wy -= n

    def E(n):
        nonlocal wx, wy, dx, dy
        wx += n

    def W(n):
        nonlocal wx, wy, dx, dy
        wx -= n

    def R(k):
        nonlocal wx, wy, dx, dy
        wx, wy = wy, -wx
        if k > 1:
            R(k - 1)

    def L(k):
        nonlocal wx, wy, dx, dy
        wx, wy = -wy, wx
        if k > 1:
            L(k - 1)

    def F(n):
        nonlocal wx, wy, dx, dy
        dx += wx * n
        dy += wy * n

    for dirn, *dist in data:
        dist = int("".join(dist))
        if dirn not in 'LR':
            eval(f'{dirn}({dist})')
        else:
            eval(f'{dirn}({dist // 90})')
    dx = abs(dx)
    dy = abs(dy)
    print(dx, dy, dx + dy)
    return dx + dy


p1()
p2()