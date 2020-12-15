N = "13,16,0,12,15,1"

N = [int(x) for x in N.split(',')]
_N = len(N)

def p1():
    seen = {n: _N - i for i, n in enumerate(N, start=1)}
    curr = N[-1]
    for i in range(_N, 2020): #2020
        val = seen.get(curr, 0)

        # update seen
        seen[curr] = 0
        for k in seen.keys():
            seen[k] += 1
        

        curr = val
    print(curr)

def p2():
    seen = {n: [i] for i, n in enumerate(N, start=1)}
    curr = N[-1]
    nxt_ = -1
    for i in range(_N + 1, 30_000_000 + 1): #30_000_000
        #print(f'Turn {i}. ', end="")
        #print(i)
        val = seen.get(curr, 0)

        if val == 0:
            #print('We have never seen', val, 'before. ', end="")
            seen[curr] = []
            nxt_ = 0
        elif len(val) == 1:
            #print(f"{curr} has only ever been seen once, on turn {val[0]}. ", end="")
            nxt_ = i - 1 - val[0]
        else:
            #print(f'We last saw {curr} on turns {val}. ', end="")
            nxt_ = val[-1] - val[-2]



        #print(f'Therefore, saying', nxt_)

        #seen[curr].append(i)
        if nxt_ not in seen:
            seen[nxt_] = []
        elif len(seen[nxt_]) == 2:
            seen[nxt_].pop(0)
        seen[nxt_].append(i)
        #seen[val].append(i)

        

        curr = nxt_
    print(curr)

p1()
p2()