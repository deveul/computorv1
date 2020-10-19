#!/usr/bin/python3
# -*-coding:Utf-8 -*

import sys

from print_computor import print_reduced_form
from print_computor import print_degree
from parse_computor import parse_equation
from solver_computor import solve
from graph import poly_graph

verbose = False
display_help = False
natural = False
graph = False

if len(sys.argv) < 2:
    print("Equation missing")
    sys.exit()
elif len(sys.argv) > 2:
    for elem in sys.argv:
        if elem == '-v':
            verbose = True
        elif elem == '-h':
            display_help = True
        elif elem == '-n':
            natural = True
        elif elem == '-g':
            graph = True
elif len(sys.argv) == 2 and sys.argv[1] == '-h':
    display_help = True

if display_help:
    print("Utilisation de computor : ")
    print('\t"python3 computor.py equation options"')
    print('\tequation de la forme : "c*X^0 + c*X^1 + a*X^2 = f*X^0 + e*X^1 + d*X^2"')
    print('\toptions :')
    print('\t\t-h: display the help')
    print('\t\t-v: display the details of the maths')
    print('\t\t-n: display reduced form as natural writing')
    print('\t\t-g: display a graph of the equation')
else:
    eq = parse_equation(sys.argv[1])
    print_reduced_form(eq.reduced_elements, natural)
    print_degree(eq.reduced_elements)
    solve(eq.reduced_elements, verbose)
    
    if graph:
        poly_graph(eq.reduced_elements)