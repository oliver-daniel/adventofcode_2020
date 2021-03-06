import constraint
import re

N = open('./in/16.txt').read().split('\n\n')

pattern = re.compile(r'(.+): (\d+)-(\d+) or (\d+)-(\d+)')

_fields, your_tx, near_tx = map(lambda n: n.strip().split('\n'), N)

def make_validator(lower, upper):
    def _inner(tx):
        return tx in lower or tx in upper

    return _inner


def parse_range(ln):
    field, l1, u1, l2, u2 = re.fullmatch(pattern, ln).groups()
    return (field, range(int(l1), int(u1) + 1), range(int(l2), int(u2) + 1))

validators = {
    field: make_validator(lower, upper)
    for field, lower, upper in map(parse_range, _fields)
}

def is_valid(tx):
    for val in map(int, tx.split(',')):
        if not any(validator(val) for validator in validators.values()):
            return (False, val)
    return (True, )


def p1():
    t = 0

    for ticket in near_tx[1:]:
        if not (k := is_valid(ticket))[0]:
            val = k[1]
            t += val
            continue
    print(t)
    return t


def AllValidConstraint(txs, col):
    field_names = list(validators.keys())
    def _inner(field):
        for i, tx in enumerate(txs):
            if not validators[field_names[field]](tx[col]):
                #print('Column', col, 'cannot be', field_names[field], f'({field})', 'due to', tx[col], 'at', i)
                return False
        return True
    return _inner

def p2():
    valid_tickets = [list(map(int, x.split(','))) for x in near_tx[1:] if is_valid(x)[0]]
    field_names = list(validators.keys())
    W = len(field_names)

    p = constraint.Problem()
    p.addVariables(["col_"+str(i) for i in range(W)], range(W))
    
    p.addConstraint(constraint.AllDifferentConstraint())

    for col in range(W):
        p.addConstraint(AllValidConstraint(valid_tickets, col), ["col_"+str(col)])

    soln = p.getSolution()

    def sorter(kv):
        return int(kv[0].split('_')[1])
    
    your_t = 1
    your_ticket = map(int, your_tx[1].split(','))
    for val, (col, field) in zip(your_ticket, sorted(soln.items(), key=sorter)):
        if field_names[field].startswith('departure'):
            # print(f'({col})', field_names[field], '=', val)
            your_t *= val
    
    print(your_t)
    return your_t
    


p1()
p2()