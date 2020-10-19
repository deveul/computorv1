#!/usr/bin/python3
# -*-coding:Utf-8 -*

from basic_operations import square_root

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_solutions_degree_2(solutions, delta):
    if delta < 0:
        print("Discriminant is strictly negative, the two complex solutions are:\n{}\n{}".format(solutions[0], solutions[1]))
    elif delta == 0:
        print("Discriminant is equal 0, the solution is:\n{}".format(solutions[0]))
    else:
        print("Discriminant is strictly positive, the two solutions are:\n{}\n{}".format(solutions[0], solutions[1]))

def print_reduced_form(coef, natural):
    reduced_form = ''
    coefficients = list(coef)

    for index, x in enumerate(coefficients):
        if natural:
            if x == 0:
                coefficients[index] = ''
            elif index == 0:
                coefficients[index] = str(x)
            elif index == 1:
                coefficients[index] = str(x) + 'X'
            else:
                coefficients[index] = str(x) + 'X^{}'.format(index)
        else:
            coefficients[index] = str(x) + ' * X^{}'.format(index)
        if natural and index > 0 and x > 0:
            coefficients[index] = '+' + coefficients[index]
        elif not natural and index > 0 and x >= 0:
            coefficients[index] = '+' + coefficients[index]
        reduced_form += coefficients[index]

    for sign in (('+', ' + '), ('-', ' - ')):
        reduced_form = reduced_form.replace(*sign)

    reduced_form = reduced_form.strip() + ' = 0'

    print("Reduced form: {}".format(reduced_form))

def print_degree(coefficients):
    print("Polynomial degree: {}".format(len(coefficients) - 1))

def print_delta_verbose(a, b, c, delta):
    print(bcolors.HEADER + "Calcul du delta :" + bcolors.ENDC)
    print("\tdelta = {b} * {b} - 4 * {a} * {c}".format(a=a, b=b, c=c))
    print("\tdelta = {b2} - {fac}".format(b2=b * b, fac=4 * a * c))
    print(bcolors.OKGREEN + "\tdelta = {}".format(delta) + bcolors.ENDC)

def print_positive_degree2_verbose(a, b, delta, solutions):
    print(bcolors.HEADER + "Solving for real solutions:" + bcolors.ENDC)
    print("\t" + bcolors.OKBLUE + "Get first solution:" + bcolors.ENDC)
    print("\t\tsolution_1 = (-b - √delta) / (2 * a)")
    print("\t\tsolution_1 = (-({b}) - √{delta}) / (2 * {a})".format(a=a, b=b, delta=delta))
    print("\t\tsolution_1 = ({top}) / {a2}".format(a2=a * 2, top=-1*b - square_root(delta)))
    print(bcolors.OKGREEN + "\t\tsolution_1 = {solution1}".format(solution1=solutions[0]) + bcolors.ENDC)
    print("\t" + bcolors.OKBLUE + "Get second solution:" + bcolors.ENDC)
    print("\t\tsolution_2 = (-b + √delta) / (2 * a)")
    print("\t\tsolution_2 = (-({b}) + √{delta}) / (2 * {a})".format(a=a, b=b, delta=delta))
    print("\t\tsolution_2 = ({top}) / {a2}".format(a2=a * 2, top=-1*b + square_root(delta)))
    print(bcolors.OKGREEN + "\t\tsolution_2 = {solution1}".format(solution1=solutions[1]) + bcolors.ENDC)

def print_zero_degree2_verbose(a, b, solutions):
    print(bcolors.HEADER + "Solving for unique solution:" + bcolors.ENDC)
    print("\tsolution = -b / (2 * a)")
    print("\tsolution = -{b} / (2 * {a})".format(a=a, b=b))
    print("\tsolution = {negb} / {a2}".format(a2=2 * a, negb=-1 * b))
    print(bcolors.OKGREEN + "\tsolution = {solution}".format(solution=solutions[0]) + bcolors.ENDC)
    
def print_negative_degree2_verbose(a, b, delta, pos_delta, real_part, imaginary_part,solutions):
    print(bcolors.HEADER + "Solving for complex solutions:" + bcolors.ENDC)
    print(bcolors.OKBLUE + "\tGet absolute value of delta:" + bcolors.ENDC)
    print("\t\tabs_delta = {}".format(pos_delta))
    print(bcolors.OKBLUE + "\tGet real part:" + bcolors.ENDC)
    print("\t\treal_part = -b / (2 * a)")
    print("\t\treal_part = -({b}) / (2 * {a})".format(a=a, b=b))
    print("\t\treal_part = {b} / {a2}".format(a2=a * 2, b=-1 * b))
    print("\t\treal_part = {r_p}".format(r_p= (-1 * b) / (2 * a)))
    print(bcolors.OKGREEN + "\t\trounded real_part = {real}".format(real=real_part) + bcolors.ENDC)
    print(bcolors.OKBLUE + "\tGet imaginary part:" + bcolors.ENDC)
    print("\t\timaginary_part = (√|delta| / (2 * a)) * i")
    print("\t\timaginary_part = (√{pos_delta} / (2 * {a})) * i".format(pos_delta=pos_delta, a=a))
    print("\t\timaginary_part = (√{sq_delta} / {a2}) * i".format(sq_delta=square_root(pos_delta), a2=2 * a))
    print("\t\timaginary_part = {not_i} * i".format(not_i=square_root(pos_delta) / (2 * a)))
    print(bcolors.OKGREEN + "\t\trounded imaginary_part = {i_p}".format(i_p=imaginary_part) + bcolors.ENDC)
    # print(bcolors.HEADER + "Solution 1 = " + bcolors.ENDC + solutions[0])
    # print(bcolors.HEADER + "Solution 2 = " + bcolors.ENDC + solutions[1])

def print_degree1_verbose(coef, solution):
    print(bcolors.HEADER + "Solving degree 1 :" + bcolors.ENDC)
    print("\tsolution = -a /b")
    print("\tsolution = -({a}) / {b}".format(a=coef[0], b=coef[1]))
    print(bcolors.OKGREEN + "\tsolution = {solution}".format(solution=solution) + bcolors.ENDC)