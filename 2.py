N = [
    "1-3 a: abcde",
    "1-3 b: cdefg",
    "2-9 c: ccccccccc",
]

#N = open('./in/2.txt').readlines()

def p1():
    t = 0
    for limits, char, pw in map(str.split, N):
        lower, upper = map(int, limits.split('-'))
        char = char[0]
        if lower <= pw.count(char) <= upper:
            t += 1
    print(f"Total: {t}")
    return t

def p2():
    t = 0
    for edges, char, pw in map(str.split, N):
        lower, upper = map(lambda x: pw[int(x) - 1], edges.split('-'))
        char = char[0]
        if char in [lower, upper] and lower != upper:
            t += 1
    print ("Total 2:", t)
    return t


p1()
p2()
