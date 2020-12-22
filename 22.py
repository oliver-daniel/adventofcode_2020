from collections import deque
from functools import cache
import itertools

N = """Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10""".split('\n\n')

N = open('./in/22.txt').read().strip().split('\n\n')

p1 = deque(map(int, N[0].split('\n')[1:]))
p2 = deque(map(int, N[1].split('\n')[1:]))

nxt_game = itertools.count(start=2)


def score(dq):
    lq = len(dq)
    return sum((lq - i) * x for i, x in enumerate(dq))


def P1():
    i = 0
    while p1 and p2:
        c1 = p1.popleft()
        c2 = p2.popleft()
        assert c1 != c2

        if c1 > c2:
            # player 1 wins
            p1.append(c1)
            p1.append(c2)
        else:
            p2.append(c2)
            p2.append(c1)
        i += 1
    print("done after", i, "rounds")
    a = score(p1)
    b = score(p2)
    if a: print(a)
    if b: print(b)

cache = {}

def crawl(a, b, game=1):
    cache[game] = set()
    
    #i = 1
    while a and b:
        tpls = (tuple(a), tuple(b))
        if tpls in cache[game]:
            #print('Early return')
            return 1
        cache[game].add(tpls)
        c1 = a.popleft()
        c2 = b.popleft()
        assert c1 != c2

        if len(a) >= c1 and len(b) >= c2:
            #print('Recursing...')
            cpy_a = deque(itertools.islice(a, 0, c1))
            cpy_b = deque(itertools.islice(b, 0, c2))
            winner = crawl(cpy_a, cpy_b, next(nxt_game))
            #print('Back to game', game)
            if winner == 1:
                #print('1 wins round', i, 'of game', game)
                a.append(c1)
                a.append(c2)
            else:
                #print('2 wins round', i, 'of game', game)
                b.append(c2)
                b.append(c1)
        else:
            if c1 > c2:
                #print('1 wins round', i, 'of game', game, '(normal)')
                a.append(c1)
                a.append(c2)
            else:
                #print('2 wins round', i, 'of game', game, '(normal)')
                b.append(c2)
                b.append(c1)

            
        
        #i += 1
    if a: 
        #print('1 wins game', game)
        return 1
    #print('2 wins game', game)
    return 2


def P2():
    p1 = deque(map(int, N[0].split('\n')[1:]))
    p2 = deque(map(int, N[1].split('\n')[1:]))
    crawl(p1, p2)
    print('done after', next(nxt_game) - 1, 'games')
    a = score(p1)
    b = score(p2)
    if a: print(a)
    elif b: print(b)


P1()
P2()