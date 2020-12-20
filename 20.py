import itertools
from constraint import *
from functools import cache, cached_property
import copy
from math import prod


N = open('./in/_20test.txt').read().split('\n\n')
N = open('./in/20.txt').read().split('\n\n')

TILES = {}
deps = {}



lookup = {
    '_000N': 'top',
    '_0NNN': 'right',
    '_N0NN': 'bottom',
    '_00N0': 'left'
}

class Tile(object):
    def __init__(self, _id, _rough_arr) -> None:
        super().__init__()
        self._id = _id
        _arr = [[(0, 1)[x == "#"] for x in row] for row in _rough_arr]
        self._arr = _arr
        self._flipv = 0     # how many times flipped vertically, mod 2
        self._fliph = 0     # how many times flipped horizontally, mod 2
        self._rot = 0       # how many times rotated clockwise (ccw = -1)
        self.deps = [None, None, None, None]

    def r(self, i):
        return self._arr[i]

    def c(self, i):
        return [row[i] for row in self._arr]

    @property
    def _000N(self):
        return self._parse(self.r(0))

    @property
    def _00N0(self):
        return self._parse(self.c(0))

    @property
    def _0NNN(self):
        return self._parse(self.c(-1))

    @property
    def _N0NN(self):
        return self._parse(self.r(-1))

    def flipv(self):
        self._flipv = (not self._flipv) | 0
        self._arr = self._arr[::-1]

        self.deps[0], self.deps[2] = self.deps[2], self.deps[0]

        return self

    def fliph(self):
        self._fliph = (not self._fliph) | 0
        self._arr = [row[::-1] for row in self ._arr]
        self.deps[1], self.deps[3] = self.deps[3], self.deps[1]

        return self

    def rotate(self, n = 1):
        """rotate n * 90º clockwise."""
        if n == 0: return
        self._rot = (self._rot + 1) % 4
        self._arr = [self.c(i)[::-1] for i in range(len(self._arr))]
        
        self.deps = self.deps[-1:] + self.deps[:-1]

        if n > 0:
            self.rotate(n - 1)
        return self

    @property
    def _hot_edges(self):
        return sum(1 for edge in self.deps if edge is not None)


    @property
    def _edges(self):
        return [
            getattr(self, method)
            for method in lookup.keys()
        ]

    def _parse(self, vec):
        return "".join("#" if x == 1 else "." for x in vec)

    def copy(self):
        return copy.deepcopy(self)

    def __repr__(self) -> str:
        ret = [f"Tile {self._id} (v={self._flipv},h={self._fliph},r={self._rot})"]
        for row in self._arr:
            ret.append(self._parse(row))
        return "\n".join(ret)

for tile in N:
    _id, *_arr = tile.split('\n')
    _id = int(_id.split()[1][:-1])
    _arr = [ln.strip() for ln in _arr]
    TILES[_id] = Tile(_id, _arr)




def set_dep(key, val, edge):
    if key not in deps:
        deps[key] = [None, None, None, None]
    deps[key][edge] = val
    TILES[key].deps = deps[key][:]



def _idx(edge, common, dir=1):
    return next(i for i, method in enumerate(lookup.keys()) if getattr(edge, method)[::dir] in common)

# TODO: could store more metadata. which edge to which? what flips needed?
for x, y in itertools.product(TILES.values(), TILES.values()):
    if x is y: continue
    x_edges = set(x._edges)
    y_edges = set(y._edges)
    rev_y_edges = set(edge[::-1] for edge in y._edges)
    common = x_edges & (y_edges | rev_y_edges)
    if len(common) > 0:
        x_edge_idx = _idx(x, common)
        if common & rev_y_edges:
            y_edge_idx = _idx(y, common, -1)
        else: 
            y_edge_idx = _idx(y, common)


        set_dep(x._id, y._id, x_edge_idx)
        set_dep(y._id, x._id, y_edge_idx)

import math
N = int(math.sqrt(len(deps.keys())))



GRID = [[None for _ in range(N)] for _ in range(N)]


def print_grid():
    print('-' * (11 * N + 1))
    for row in GRID:
        for i in range(10):
            print('|', end="")
            for col in row:
                if col:
                    print(col._parse(col.r(i)), end="|")
                    continue
                print(' '* 10, end="|")
            print()
        print('-' * (11 * N + 1))


def crawl(node, row, col):
    GRID[row][col] = node
    #print(row, col, node._id)
    #print_grid()

    if col < N - 1:
        right_dep = TILES[node.deps[1]]

        while right_dep.deps[3] != node._id:
            right_dep.rotate()
        if right_dep.c(0) != node.c(-1):
            right_dep.flipv()
        
        crawl(right_dep, row, col + 1)

    
    if row < N - 1:
        bottom_dep = TILES[node.deps[2]]
        while bottom_dep.deps[0] != node._id:
            bottom_dep.rotate()
        
        if bottom_dep.r(0) != node.r(-1):
            bottom_dep.fliph()

        
        crawl(bottom_dep, row + 1, col)

SPRITE = """                  # 
#    ##    ##    ###
 #  #  #  #  #  #   """.split('\n')

MASK = [[(col == "#") | 0 for col in row] for row in SPRITE]
mask_sum = sum(sum(row) for row in MASK)

M = len(MASK)
M0 = len(MASK[0])

def convolve(img):
    t = 0
    for i in range(len(img) - M):
        for j in range(len(img[0]) - M0):
            #print('Looking for monsters at', i, j)
            for mr, ir in zip(MASK, img[i:]):
                broken = False
                for mc, ic in zip(mr, ir[j:]):
                    if mc and not ic:
                        broken = True
                        break
                if broken: break
                
            else:
                #print('found!')
                t += 1
    return t

def p1():
    corners = [tile for tile in TILES.values() if tile._hot_edges == 2]
    k = prod(tile._id for tile in corners)
    print(k)
    return k

def p2():
    corners = [tile for tile in TILES.values() if tile._hot_edges == 2]
    tl_corner = next(tile for tile in corners if tile.deps[0] is None and tile.deps[3] is None)
    # GRID[0][0] = tl_corner

    crawl(tl_corner, 0, 0)

    #print_grid()

    ultragrid = []
    rough = 0
    for row in GRID:
        for i in range(1,9):
            ultragrid += [''.join(t._parse(t.r(i)[1:-1]) for t in row)]
            rough += sum(sum(t.r(i)[1:-1]) for t in row)

    t = Tile(0, ultragrid)
    
    k = 0
    for _ in range(2):
        for _ in range(4):
            k = convolve(t._arr)
            if k > 0:
                break
            t.rotate()
        if k > 0:
            break
        t.fliph()

    print(rough - mask_sum * k)


p1()
p2()
