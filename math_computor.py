#!/usr/bin/python3
# -*-coding:Utf-8 -*

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def square_root(b):
    a = 1
    e = 1
    calc = lambda x : (x + b / x)/ 2

    if b == 0: return 0
    while (e > 0.001):
        fa = calc(a)
        if (fa > a):
            e = fa - a
        else:
            e = a - fa
        a = fa
    return a

def calculate_delta(a, b, c, verbose):
    delta = b * b - 4 * a * c 
    if verbose:
        print(bcolors.HEADER + "Calcul du delta :" + bcolors.ENDC)
        print("\tdelta = {b} * {b} - 4 * {a} * {c}".format(a=a, b=b, c=c))
        print("\tdelta = {b2} - {fac}".format(b2=b * b, fac=4 * a * c))
        print("\tdelta = {}".format(delta))
    return delta

def round_float(nb):
    nb *= 1000000
    entier, flotant = str(nb).split('.')
    flotant = int(flotant[:1])
    entier = int(entier)
    if flotant >= 5 and entier >= 0:
        entier = entier + 1
    elif flotant >= 5 and entier < 0:
        entier = entier - 1
    nb = entier / 1000000
    return (str(nb))

def calculate_solutions_degree_2(a, b, delta, verbose):
    solutions = []
    if (delta < 0):
        pos_delta = -delta
        real_part = round_float(-b / (2 * a))
        imaginary_part = round_float(square_root(pos_delta) / (2 * a)) + 'i'
        if float(imaginary_part[:-1]) > 0:
            solutions.append(real_part + '+' + imaginary_part)
            solutions.append(real_part + '-' + imaginary_part)
        else:
            solutions.append(real_part + imaginary_part)
            solutions.append(real_part + '+' + imaginary_part[1:])
        if verbose:
            print(bcolors.HEADER + "Solving for complex solutions:" + bcolors.ENDC)
            print("Absolute value of delta : {}".format(pos_delta))
            print(bcolors.HEADER + "Calculate real part :" + bcolors.ENDC)
            print("\treal_part = -b / (2 * a)")
            print("\treal_part = -{b} / (2 * {a})".format(a=a, b=b))
            print("\treal_part = {b} / {a2}".format(a2=a * 2, b=-1 * b))
            print("\treal_part = {real}".format(real=real_part))
            print(bcolors.HEADER + "Calculate imaginary part :" + bcolors.ENDC)
            print("\timaginary_part = (√|delta| / (2 * a)) * i")
            print("\timaginary_part = (√{pos_delta} / (2 * {a})) * i".format(pos_delta=pos_delta, a=a))
            print("\timaginary_part = (√{sq_delta} / {a2}) * i".format(sq_delta=square_root(pos_delta), a2=2 * a))
            print("\timaginary_part = {not_i} * i".format(not_i=square_root(pos_delta) / (2 * a)))
            print("\trounded imaginary_part = {i_p}".format(i_p=imaginary_part))
            # print(bcolors.HEADER + "Solution 1 = " + bcolors.ENDC + solutions[0])
            # print(bcolors.HEADER + "Solution 2 = " + bcolors.ENDC + solutions[1])
    elif (delta == 0):
        solutions.append(round_float(-b / (2 * a)))
        if verbose:
            print(bcolors.HEADER + "Solving for unique solution:" + bcolors.ENDC)
            print("\tsolution = -b / (2 * a)")
            print("\tsolution = -{b} / (2 * {a})".format(a=a, b=b))
            print("\tsolution = {negb} / {a2}".format(a2=2 * a, negb=-1 * b))
            print("\tsolution = {solution}".format(solution=solutions[0]))
    else:
        solutions.append(round_float((-b - square_root(delta)) / (2 * a)))
        solutions.append(round_float((-b + square_root(delta)) / (2 * a)))
        if verbose:
            print(bcolors.HEADER + "Solving for real solutions:" + bcolors.ENDC)
            print("\tsolution_1 = (-b - √delta) / (2 * a)")
            print("\tsolution_1 = (-{b} - √{delta}) / (2 * {a})".format(a=a, b=b, delta=delta))
            print("\tsolution_1 = ({top}) / {a2}".format(a2=a * 2, top=-1*b - square_root(delta)))
            print("\tsolution_1 = {solution1}".format(solution1=solutions[0]))
            print("\tsolution_2 = (-b + √delta) / (2 * a)")
            print("\tsolution_2 = (-{b} + √{delta}) / (2 * {a})".format(a=a, b=b, delta=delta))
            print("\tsolution_2 = ({top}) / {a2}".format(a2=a * 2, top=-1*b + square_root(delta)))
            print("\tsolution_2 = {solution1}".format(solution1=solutions[1]))

    return solutions