from functools import cache
from itertools import product
from tqdm.auto import tqdm

N, data = open('./in/19.txt').read().split('\n\n')

deps = {}
for ln in map(str.strip, N.split('\n')):
    num, args = ln.split(': ')
    num = int(num)
    args = [[int(arg) if arg.isdigit() else arg[1:-1] for arg in part.split()]
            for part in args.split(' | ')]
    deps[num] = args


@cache
def build(node):
    if node == []: return set()

    g = deps[node]
    if len(g) == 1 and type(g[0][0]) is str:
        return set(g[0])
    ret = set()
    for ruleset in g:
        A, *others = map(build, ruleset)
        for x in map(''.join, product(A, *others)):
            ret.add(x)
    return ret





@cache
def crawl(node, target=0, orig=False):
    if node in build(target):
        return True

    if target == 0:
        for prefix, suffix in product(build(42), build(31)):
            if node.startswith(prefix) and node.endswith(suffix):
                mid = node[len(prefix):-len(suffix)]
                assert node == prefix + mid + suffix
                # try lopping off both affixes and trying again,
                # this time at nonzero depth
                if crawl(mid, 0):
                    return True
        else:
            # if we're at a nonzero depth, we want to fall through
            # (since we knocked off all the suffixes)
            if orig: return False
    
    for prefix in build(42):
        if node.startswith(prefix):
            after = node[len(prefix):]
            assert node == prefix + after
            # lop off the prefix and try looking again
            if crawl(after, 8):
                return True
    return False

def p1():
    k = build(0)
    X = {x.strip() for x in data.split('\n')}
    Xk = X.intersection(k)

    print(len(Xk))
    return (len(Xk))

def p2():
    X = [x.strip() for x in data.split('\n')]
    
    ret = []
    for x in tqdm(X, leave=False):
        if crawl(x, 0, True):
            ret.append(x)

    print(len(ret))
    return len(ret)


p1()
p2()
