#!/usr/bin/python3
# -*-coding:Utf-8 -*

from math_computor import calculate_delta
from math_computor import calculate_solutions_degree_2
from math_computor import round_float
from print_computor import print_solutions_degree_2

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def solve_degree_2(coef, verbose):
    delta = calculate_delta(coef[2], coef[1], coef[0], verbose)
    solutions = []
    
    solutions = calculate_solutions_degree_2(coef[2], coef[1], delta, verbose)
    
    print_solutions_degree_2(solutions, delta)

#revoir !!!
def solve_degree_1(coef, verbose):
    solution = -coef[0] / coef[1]
    solution = round_float(solution)
    if verbose:
        print(bcolors.HEADER + "Solving degree 1 :" + bcolors.ENDC)
        print("\tsolution = -a /b")
        print("\tsolution = -{a} / {b}".format(a=coef[0], b=coef[1]))
        print("\tsolution = {solution}".format(solution=solution))
    print("The solution is:\n{}".format(solution))

def solve_degree_0(coef):
    if coef[0] == 0:
        print("All real numbers are solutions")
    else:
        print("There is no solution to this equation")

def solve(coefficients, verbose):
    degree = len(coefficients) - 1
    if degree == 0:
        solve_degree_0(coefficients)
    elif degree == 1:
        solve_degree_1(coefficients, verbose)
    elif degree == 2:
        solve_degree_2(coefficients, verbose)
    else:
        print("The polynomial degree is stricly greater than 2, I can't solve.")