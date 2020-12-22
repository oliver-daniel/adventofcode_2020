import constraint
from math import prod

N = list(map(int, open("./in/1.txt").readlines()))

def p(n):
    p = constraint.Problem()
    p.addVariables(range(n), N)
    p.addConstraint(constraint.AllDifferentConstraint())
    p.addConstraint(constraint.ExactSumConstraint(2020))
    
    try:
        print(prod(p.getSolution().values()))
    except:
        print("")




p(2)
p(3)