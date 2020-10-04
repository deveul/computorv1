#!/usr/bin/python3
# -*-coding:Utf-8 -*

import sys

from print_computor import print_reduced_form
from print_computor import print_degree
from parse_computor import parse_equation
from solver_computor import solve

if len(sys.argv) < 2:
    print("Equation missing")
    sys.exit()
else:
    eq = parse_equation(sys.argv[1])
    print_reduced_form(eq.reduced_elements)
    print_degree(eq.reduced_elements)
    solve(eq.reduced_elements)

# a = float(input("Entrez a :\n"))
# b = float(input("Entrez b :\n"))
# c = float(input("Entrez c :\n"))
# 
# delta = calculate_delta(a, b, c)
# 
# print("Discriminant de l'équation :", delta)
# 
# solutions = []
# 
# solutions = calculate_solutions(a, b, delta)
# 
# print_solutions(solutions, delta)