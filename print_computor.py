#!/usr/bin/python3
# -*-coding:Utf-8 -*

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