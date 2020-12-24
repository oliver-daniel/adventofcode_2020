import itertools as it
from tqdm.auto import tqdm

N = """sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew""".split('\n')

N = open('./in/24.txt').readlines()

LOOKUP = {
   'e': (1, 0),
   'w': (-1, 0),
   'se': (1, -1), 
   'sw': (0, -1),
   'ne': (0, 1),
   'nw': (-1, 1)
}


def to_coords(dirs):
    _l = len(dirs)
    dx, dy = 0, 0

    cts = {x: dirs.count(x) for x in LOOKUP}
    cts['w'] -= cts['sw'] + cts['nw']
    cts['e'] -= cts['se'] + cts['ne']

    for token, (_dx, _dy) in LOOKUP.items():
        dx += _dx * cts[token]
        dy += _dy * cts[token]

    return (dx, dy)

tiles = {}
for dirs in N:
    coords = to_coords(dirs.strip())
    if coords in tiles:
        tiles[coords] = (not tiles[coords]) | 0
    else:
        tiles[coords] = 1

def p1():
    k = sum(tiles.values())
    print(k)
    return k

def neighbours(tiles, x, y):
    t = 0
    for (dx, dy) in LOOKUP.values():
        coords = (x + dx, y + dy)
        t += tiles.get(coords, 0)
    return t

def transition(_tiles):
    tiles = {**_tiles}
    for coords, is_black in _tiles.items():
        nbrs = neighbours(_tiles, *coords)
        if is_black and not 1 <= nbrs <= 2:
            tiles[coords] = 0
        elif not is_black and nbrs == 2:
            tiles[coords] = 1

    return tiles


def p2():
    LIMIT = 71  # experimentally determined for speed
    global tiles
    for coords in it.product(range(-LIMIT, LIMIT), repeat=2):
        if coords in tiles:
            continue
        tiles[coords] = 0
    
    for i in tqdm(range(100), leave=False):
        tiles = transition(tiles)

    k = sum(tiles.values())

    xs, ys = map(list, zip(*(t for t in tiles.keys() if tiles[t])))

    print(k)
    return k
    

p1()
p2()

