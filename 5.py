N = [x.strip() for x in open('./in/5.txt').readlines()]

def coords(code):
        x_low = y_low = 0
        x_high = 7 
        y_high = 127
        for c in code:
            dy = (y_high - y_low + 1) // 2
            dx = (x_high - x_low + 1) // 2

            if c == 'F':
                y_high -= dy
            elif c == 'B':
                y_low += dy
            elif c == 'R':
                x_low += dx
            else: # c == 'L
                x_high -= dx
            #print(f"({x_low}, {y_low}) ~ ({x_high}, {y_high})")
        #print(f"({x_low}, {y_low}) ~ ({x_high}, {y_high})")
        #assert x_low == x_high and y_low == y_high
        return 8 * y_low + x_low

def p1():
    k = max(N, key=coords)
    print(k, coords(k))

def p2():
    flts = list(sorted(map(coords, N)))
    for i, flt in enumerate(flts[1:-1], start=flts[1]):
        if i != flt:
            print(i, flt)
            return i
p1()
p2()
