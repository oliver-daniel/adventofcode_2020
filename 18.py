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

def parse1(expr):
    subexprs = outer_brackets(expr)
    for sbx in subexprs:
        expr = expr.replace(sbx, parse1(sbx[1:-1]))

    #print('Evaluating', expr, end = " ")

    tokens = expr.split(" ")

    stack = []
    for c in tokens:
        if c.isdigit() and len(stack) >= 2 and type(stack[-1]) is str: 
            op = stack.pop()
            arg2 = int(stack.pop())
            new = str(eval(f'{int(c)} {op} {arg2}'))
            stack.append(new)
        else: 
            stack.append(c)
    #print("=", stack[0])
    return stack[0]

def parse2(expr):
    subexprs = outer_brackets(expr)
    for sbx in subexprs:
        expr = expr.replace(sbx, parse2(sbx[1:-1]))

    #print('Evaluating', expr, end = " ")

    tokens = expr.split(" ")

    stack = []
    for c in tokens:
        if c.isdigit() and len(stack) >= 2 and stack[-1] == "+": 
            op = stack.pop()
            arg2 = int(stack.pop())
            new = str(eval(f'{int(c)} {op} {arg2}'))
            stack.append(new)             
        else: 
            stack.append(c)
    k = str(math.prod(int(x) for x in stack if x.isdigit()))
    #print("=", k)
    return k
                
            
def p1():
    t = 0
    for ln in N:
        t += int(parse1(ln))
    print(t)
    return t

def p2():
    t = 0
    for ln in N:
        t += int(parse2(ln))
    print(t)
    return t

p1()
print('------')
p2()