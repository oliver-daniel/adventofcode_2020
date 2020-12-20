N = list(map(str.strip, open('./in/18.txt').readlines()))

SYMBOLS = {'+': '__add__', '*': '__mul__'}


def outer_brackets(s):
    ret = []
    stack = []
    for i, c in enumerate(s):
        if c == "(":
            stack.append(i)
        elif c == ")":
            p = stack.pop()
            if len(stack) == 0:
                ret.append(s[p:i + 1])
    return ret


def evaluate(arg1, op, arg2):
    if not isinstance(arg1, int): arg1 = int(arg1)
    if not isinstance(arg2, int): arg2 = int(arg2)
    method = SYMBOLS[op]
    return getattr(arg1, method)(arg2)


def parse(expr, priority_ops=['*', '+']):
    subexprs = outer_brackets(expr)
    for sbx in subexprs:
        expr = expr.replace(sbx, str(parse(sbx[1:-1], priority_ops)))

    tokens = expr.split(" ")

    stack = []
    for c in tokens:
        if len(stack) >= 2 and stack[-1] in priority_ops:
            new = evaluate(c, stack.pop(), stack.pop())
            stack.append(new)
        else:
            stack.append(c)

    k = int(stack.pop())
    while len(stack) > 0:
        k = evaluate(k, stack.pop(), stack.pop())

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