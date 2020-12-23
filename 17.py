import itertools
from tqdm.auto import tqdm

N = """.#.
..#
###""".split('\n')

N = [ln.strip() for ln in open('./in/17.txt').readlines()]

H = len(N)
W = len(N[0])

assert H == W

LIMIT = 20

origin = LIMIT // 2 - H // 2



def p1():
    # consensus: [z][y][x]
    board = [[[0 for _ in range(LIMIT)] for _ in range(LIMIT)] for _ in range(LIMIT)]

    for y, row in enumerate(N, start=origin):
        for x, col in enumerate(row, start=origin):
            if col == "#":
                board[origin][y][x] = 1

    def neighbours_1(curr, z, y, x):
        t = 0
        for dz, dy, dx in itertools.product([-1, 0, 1], repeat=3):
            if dz == dy == dx == 0: continue
            t += 0 <= (k := z + dz) < LIMIT and \
                0 <= (j := y + dy) < LIMIT and \
                0 <= (i := x + dx) < LIMIT and \
                curr[k][j][i]
        return t

    def transition(curr, neighbours):
        new = []
        for k, plane in enumerate(curr):
            new_plane = []
            for j, row in enumerate(plane):
                new_row = []
                for i, col in enumerate(row):
                    if col == 1 and not 2 <= neighbours(curr, k, j, i) <= 3:
                        new_row.append(0)
                    elif col == 0 and neighbours(curr, k, j, i) == 3:
                        new_row.append(1)
                    else:
                        new_row.append(col)
                new_plane.append(new_row)
            new.append(new_plane)

        return new


    curr = board
    for i in tqdm(range(6)):
        curr = transition(curr, neighbours_1)
    
    print(sum(sum(sum(row) for row in plane) for plane in curr))

def p2():
    # consensus: [z][y][x]
    board = [[[[0 for _ in range(LIMIT)] for _ in range(LIMIT)] for _ in range(LIMIT)] for _ in range(LIMIT)]

    for y, row in enumerate(N, start=origin):
        for x, col in enumerate(row, start=origin):
            if col == "#":
                board[origin][origin][y][x] = 1

    def ns(curr, dims):
        t = 0

    def neighbours_2(curr, w, z, y, x):
        t = 0
        for dw, dz, dy, dx in itertools.product([-1, 0, 1], repeat=4):
            if dw == dz == dy == dx == 0: continue
            t += 0 <= (m := w + dw) < LIMIT and \
                 0 <= (k := z + dz) < LIMIT and \
                 0 <= (j := y + dy) < LIMIT and \
                 0 <= (i := x + dx) < LIMIT and \
                curr[m][k][j][i] == 1
        return t

    def transition(curr, neighbours):
        new = []
        for m, space in enumerate(curr):
            new_space = []
            for k, plane in enumerate(space):
                new_plane = []
                for j, row in enumerate(plane):
                    new_row = []
                    for i, col in enumerate(row):
                        if col == 1 and not 2 <= neighbours(curr, m, k, j, i) <= 3:
                            new_row.append(0)
                        elif col == 0 and neighbours(curr, m, k, j, i) == 3:
                            new_row.append(1)
                        else:
                            new_row.append(col)
                    new_plane.append(new_row)
                new_space.append(new_plane)
            new.append(new_space)

        return new


    curr = board
    for i in tqdm(range(6)):
        curr = transition(curr, neighbours_2)
    
    print(sum(sum(sum(sum(row) for row in plane) for plane in space) for space in curr))

p1()
p2()