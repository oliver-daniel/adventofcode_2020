N = open('./in/6.txt').read()

groups = [n.strip().split('\n') for n in N.split('\n\n')]


def p1():
    s = 0
    for group in groups:
        X = set()
        for answers in group:
            for qn in answers:
                X.add(qn)
        s += len(X)
    print(s)
    return(s)

def p2():
    s = 0
    for group in groups:
        seen = {}
        for i, answers in enumerate(group):
            for qn in answers:
                if qn not in seen:
                    seen[qn] = []
                seen[qn].append(i)
        vals = [val for key, val in seen.items() if len(val) == len(group)]
        #print(len(vals), vals)
        s += len(vals)
    print(s)
    return s
p1()
p2()