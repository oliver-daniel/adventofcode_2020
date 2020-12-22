from collections import Counter
N = open('./in/21.txt').readlines()

ctr = Counter()
allergens = {}

lists = []
notices = []

# first pass: get all tokens and all hypotheses
for ln in map(str.strip, N):
    tokens, algs = ln.split(' (contains ')
    tokens = set(tokens.split())
    ctr.update(tokens)

    lists.append(tokens)

    algs = algs[:-1].replace(',', '').split()
    notices.append(algs)

    for alg in algs:
        if alg not in allergens:
            allergens[alg] = set()


for ings, ntcs in zip(lists, notices):
    for allergen in allergens:
        if allergen in ntcs:
            if len(allergens[allergen]) > 0:
                allergens[allergen] &= ings
            else:
                allergens[allergen] = ings.copy()


while not all(len(val) == 1 for val in allergens.values()):
    for alg, hypotheses in allergens.items():
        if len(hypotheses) == 1:
            for other_allergen in allergens:
                if other_allergen is alg: continue
                allergens[other_allergen] -= hypotheses
            

def p1():
    safe = set(ctr)
    for tokens in allergens.values():
        safe -= tokens
    print(sum(ctr[x] for x in safe))

def p2():
    keys = sorted(allergens.keys())
    ret = [next(iter(allergens[key])) for key in keys]
    print(','.join(ret))

p1()
p2()

