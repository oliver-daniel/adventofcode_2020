N = open('./in/8.txt').readlines()

N = [(op, int(val)) for op, val in map(str.split, N)]


def p1():
    visited = set()
    i = 0
    acc = 0
    while i not in visited:
        op, val = N[i]
        visited.add(i)
        if op == "nop":
            i += 1
        elif op == "acc":
            acc += val
            i += 1
        elif op == "jmp":
            i += val
    print("final i:", i)
    print("final acc:", acc)

def p2():
    def terminates(prog):
        visited = set()
        i = 0
        acc = 0
        while i < len(prog):
            if i in visited:
                return None
            visited.add(i)

            op, val = prog[i]
            
            if op == "nop":
                i += 1
            elif op == "acc":
                acc += val
                i += 1
            elif op == "jmp":
                i += val
        return acc
    
    for i, (op, val) in enumerate(N):
        if op == "nop" and (k := terminates(N[:i] + [('jmp', val)] + N[i + 1:])):
            print('accepted by mod nop at', i, k)
            return
        elif op == "jmp" and (k := terminates(N[:i] + [('nop', val)] + N[i + 1:])):
            print('accepted by mod jmp at', i, k)
            return
p1()
p2()