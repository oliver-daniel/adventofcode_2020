N = open('./in/9.txt').readlines()

N = [int(x) for x in N]


def p1():
    PREAMBLE_SIZE = 25
    for i, num in enumerate(N[PREAMBLE_SIZE:]):
        preamble = N[i: PREAMBLE_SIZE + i]
        for num2 in preamble:
            if num - num2 in preamble:
                break
        else:
            print(num)
            return num


def p2():
    WEAKNESS = 258585477
    psa = [0]
    t = 0
    for x in N:
        t += x
        psa.append(t)

    for r, x in enumerate(psa):
        for l, y in enumerate(psa[:r]):
            if x - y == WEAKNESS:
                print('found at', r, '-', l)
                subset = N[l : r]
                m = min(subset)
                M = max(subset)
                print(m + M)
                return m + M

p1()
p2()