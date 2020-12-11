N = [
    "..##.......",
    "#...#...#..",
    ".#....#..#.",
    "..#.#...#.#",
    ".#...##..#.",
    "..#.##.....",
    ".#.#.#....#",
    ".#........#",
    "#.##...#...",
    "#...##....#",
    ".#..#...#.#",
]

N = [line.strip() for line in open('./in/3.txt').readlines()]

def p1():
    W = len(N[0])
    cursor = 0
    t = 0
    for line in N[1:]:
        cursor += 3
        cursor %= W
        if line[cursor] == "#":
            #print('X', end="")
            t += 1
        else: pass #print('O', end="")
    print(t)
    return t

def p2():
    W = len(N[0])
    def check(dx, dy):
        cursor = 0
        t  = 0
        for line in N[dy::dy]:
            cursor += dx
            cursor %= W
            if line[cursor] == "#":
                #print('X', end="")
                t += 1
            else: pass#print('O', end="")
        return t
    slopes = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2)
    ]
    t = 1
    for dx, dy in slopes:
         a = check(dx, dy)
         #print(a)
         t *= a
    print(t)
    return t 

p1()
p2()