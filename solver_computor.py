#!/usr/bin/python3
# -*-coding:Utf-8 -*

from math_computor import calculate_delta
from math_computor import calculate_solutions_degree_2
from math_computor import round_float
from print_computor import print_solutions_degree_2

def solve_degree_2(coef):
    delta = calculate_delta(coef[0], coef[1], coef[2])
    solutions = []
    
    solutions = calculate_solutions_degree_2(coef[2], coef[1], delta)
    
    print_solutions_degree_2(solutions, delta)

def solve_degree_1(coef):
    solution = -coef[0] / coef[1]
    # if solution.is_integer():
        # solution = int(solution)
    solution = round_float(solution)
    print("The solution is:\n{}".format(solution))

def solve_degree_0(coef):
    if coef[0] == 0:
        print("All real numbers are solutions")
    else:
        print("There is no solution to this equation")

def solve(coefficients):
    degree = len(coefficients) - 1
    if degree == 0:
        solve_degree_0(coefficients)
    elif degree == 1:
        solve_degree_1(coefficients)
    elif degree == 2:
        solve_degree_2(coefficients)
    else:
        print("The polynomial degree is stricly greater than 2, I can't solve.")