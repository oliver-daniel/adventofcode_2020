import re

N = open('./in/4.txt').read()

N = N.split('\n\n') # sep by blank lines
N = [ln.strip().replace('\n', ' ') for ln in N]

print(len(N))

FIELDS = 'byr iyr eyr hgt hcl ecl pid'.split()

def p1():
    print(sum(1 for ln in N if all(f'{field}:' in ln for field in FIELDS)))

def hgt_validator(x):
    if not re.fullmatch(r'\d+(cm|in)', x):
        return False
    if x.endswith('cm'):
        return 150 <= int(x[:-2]) <= 193
    return 59 <= int(x[:-2]) <= 76


VALIDATED_FIELDS = {
    'byr': lambda x: re.fullmatch(r'\d{4}', x) and 1920 <= int(x) <= 2002,
    'iyr': lambda x: re.fullmatch(r'\d{4}', x) and 2010 <= int(x) <= 2020,
    'eyr': lambda x: re.fullmatch(r'\d{4}', x) and 2020 <= int(x) <= 2030,
    'hgt': hgt_validator, #re.fullmatch(r'\d+(cm|in)', x) and (150 <= int(x[:-2]) <= 193) if x.endswith('cm') else (59 <= int(x[:-2]) <= 76),
    'hcl': lambda x: re.fullmatch(r'#[0-9a-f]{6}', x),
    'ecl': lambda x: x in 'amb blu brn gry grn hzl oth'.split(),
    'pid': lambda x: re.fullmatch(r'\d{9}', x),
    'cid': lambda x: True
}


def p2():
    t = 0
    for passport in N:
        tokens = [x for x in re.split(r'\b(\w+):(\S+)\b', passport) if x and not re.match('\s+', x)]

        keys = tokens[::2]
        vals = tokens[1::2]

        if not all (field in keys for field in FIELDS):
            continue

        tokens = list(zip(keys, vals))



        for key, val in tokens:
            #print(f'{key}: {val}')
            try:
                if not VALIDATED_FIELDS[key](val):
                    break
            except Exception as e:
                print('Something went wrong with:', key)
                print("val:", val)
                print(e)
                raise SystemExit
        else:
            t += 1
    print(t)
    return t

p1()
p2()