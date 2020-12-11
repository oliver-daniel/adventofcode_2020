N = [x.strip() for x in open('./in/7.txt').readlines()]

def parse(instr):
    tokens = instr.split()
    from_clr = " ".join(tokens[:2])
    if instr.endswith('no other bags.'):
        return from_clr, None
    children = [tokens[i: i + 3] for i in range(4, len(tokens), 4)]
    children_fmt = [(" ".join(name), weight) for weight, *name in children]
    return from_clr, children_fmt

def p1():
    SAURON = {}

    def dfs(node, seen=None):
        if seen is None:
            seen = set()
        if node == "shiny gold":
            return True
        seen.add(node)
        for child, _ in SAURON[node]:
            if child not in seen and dfs(child, seen):
                return True
        return False

    for color, children in map(parse, N):
        if color not in SAURON:
            SAURON[color] = []
        SAURON[color].extend(children or [])

    print (sum(1 for color in SAURON.keys() if color != "shiny gold" and dfs(color)))

def p2():
    SAURON = {}

    for color, children in map(parse, N):
        if color not in SAURON:
            SAURON[color] = []
        SAURON[color].extend(children or [])

    def recur(node):
        s = 0 if node == "shiny gold" else 1
        for child, quant in SAURON[node]:
            quant = int(quant)
            s += quant * recur(child)
        return s
    print(recur('shiny gold'))
p1()
p2()
