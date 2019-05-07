"""
If p is the perimeter of a right angle triangle with integral length sides,
{a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""
from math import sqrt

limit = 1000

max_solutions_p, nb_solutions = 0, 0
for p in range(3, limit + 1):
    solutions = set()
    for a in range(1, int((p + 1) / 2)):
        b = (p * (p - 2*a)) / (2 * (p - a))
        c = sqrt(pow(a, 2) + pow(b, 2))
        if b.is_integer() and c.is_integer() and (a+b+c) == p:
            solutions.add(frozenset({a, int(b), int(c)}))
    if len(solutions) > nb_solutions:
        max_solutions_p, nb_solutions = p, len(solutions)
        print("p=", p, ", ", [list(x) for x in solutions], sep="")

print(max_solutions_p, nb_solutions)
