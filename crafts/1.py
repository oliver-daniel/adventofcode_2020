import constraint
from math import prod
N="""1721
979
366
299
675
1456"""

N = open("./in/1.txt").readlines()

N = [int(x) for x in N]

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