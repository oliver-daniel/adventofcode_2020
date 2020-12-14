import re
import itertools

N = [ln.strip() for ln in open('./in/14.txt').readlines()]

pattern = re.compile(r'mem\[(\d+)\] = (\d+)')

def p1():
    ADDRS = {} # better for sparse arrays like this
    mask = "X"*36
    def parse(val):
        val = "{0:0>36}".format(bin(val)[2:])
        return sum(int(m if m != 'X' else v) << i for i, (v, m) in enumerate(zip(reversed(val), reversed(mask))))
    
    for ln in N:
        if ln.startswith('mask'):
            mask = ln.split()[2]
        else:
            addr, val = map(int,re.fullmatch(pattern, ln).groups())
            ADDRS[addr] = parse(val)
    
    k = sum(ADDRS.values())
    print(k)
    return k


def p2():
    ADDRS = {}
    MASKS = []
    
    def parse(mask, addr):
        addr = "{0:0>36}".format(bin(addr)[2:])
        t = 0
        for i, (a, m) in enumerate(zip(reversed(addr), reversed(mask))):
            if m == 'Z':
                continue # 0
            elif m == '1':
                t += 1 << i
            else:
                t += int(a) << i
        return t
    
    def set_masks(mask):
        MASKS.clear()
        X = mask.count('X')
        for p in itertools.product(*['Z1']*X):
            new_mask = mask[:]
            for c in p:
                new_mask = new_mask.replace('X', c, 1)
            MASKS.append(new_mask)
    for ln in N:
        if ln.startswith('mask'):
            set_masks(ln.split()[2])
        else:
            addr, val = map(int,re.fullmatch(pattern, ln).groups())
            for mask in MASKS:
                ADDRS[parse(mask, addr)] = val
    
    k = sum(ADDRS.values())
    print(k)
    return k

            




p1()
p2()