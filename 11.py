import itertools

N_ = list(map(str.strip, open('./in/11.txt').readlines()))
H = len(N_)
W = len(N_[0])
dim = max(H, W)


def adjacent_neighbors(N, row, col):
    t = 0
    for dy, dx in itertools.product([-1, 0, 1], [-1, 0, 1]):
        if dy == dx == 0:
            continue
        t += 0 <= (i := row + dy) < H and \
             0 <= (j := col + dx) < W and \
             N[i][j] == "#"
    return t


def transition(curr, neighbours, tolerance=4):
    new = []
    changed = False
    for i, row in enumerate(curr):
        new_row = []
        for j, cell in enumerate(row):
            if cell == "L" and neighbours(curr, i, j) == 0:
                new_row.append('#')
                changed = True
            elif cell == "#" and neighbours(curr, i, j) >= tolerance:
                new_row.append('L')
                changed = True
            else:
                new_row.append(cell)
        new.append(new_row)
    return changed, new


def p1():
    curr = N_
    for i in itertools.count():
        changed, curr = transition(curr, adjacent_neighbors)
        if not changed:
            k = sum(row.count("#") for row in curr)
            print(k, 'seats after', i, 'iterations')
            return k


def visible_neighbors(N, row, col):
    t = 0

    for dy, dx in itertools.product([-1, 0, 1], [-1, 0, 1]):
        if dy == dx == 0:
            continue
        try:
            delta = next(filter(lambda delt: 0 <= (i := row + delt * dy) < H and \
                                             0 <= (j := col + delt * dx) < W and \
                                             N[i][j] != '.', range(1, dim)))
            seen = N[row + delta * dy][col + delta * dx]
            t += seen == "#"
        except StopIteration:  # sorry lol
            pass

    return t


def p2():
    curr = N_
    for i in itertools.count():
        changed, curr = transition(curr, visible_neighbors, tolerance=5)
        if not changed:
            k = sum(row.count("#") for row in curr)
            print(k, 'seats after', i, 'iterations')
            return k


p1()
p2()
