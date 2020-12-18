import math
N = ["((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"]

N = list(map(str.strip, open('./in/18.txt').readlines()))

def outer_brackets(s):
    ret = []
    stack = []
    for i, c in enumerate(s):
        if c == "(":
            stack.append(i)
        elif c == ")": 
            if len(stack) == 1:
                ret.append(s[stack.pop(): i + 1])
            else:
                stack.pop()
    return ret

def parse(expr, priority_ops = ['*', '+']):
    subexprs = outer_brackets(expr)
    for sbx in subexprs:
        expr = expr.replace(sbx, str(parse(sbx[1:-1], priority_ops)))

    tokens = expr.split(" ")

    stack = []
    for c in tokens:
        if c.isdigit() and len(stack) >= 2 and stack[-1] in priority_ops:
            op = stack.pop()
            arg2 = int(stack.pop())
            new = str(eval(f'{int(c)} {op} {arg2}'))
            stack.append(new)             
        else: 
            stack.append(c)
    

    k = int(stack.pop())
    while len(stack) > 0:
        op = stack.pop()
        arg2 = stack.pop()
        to_eval = f'{k} {op} {arg2}'
        k = eval(f'{k} {op} {arg2}')

    return k

def p1():
    t = sum(parse(ln) for ln in N)
    print(t)
    return t

def p2():
    t = sum(parse(ln, priority_ops=["+"]) for ln in N)
    print(t)
    return t              

p1()
print('------')
p2()