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

def calculate_delta(a, b, c):
    delta = b * b - 4 * a * c 
    print(bcolors.HEADER + "Calcul du delta :" + bcolors.ENDC)
    print("\tDelta = {b} * {b} - 4 * {a} * {c}".format(a=a, b=b, c=c))
    print("\tDelta = {b2} - {fac}".format(b2=b * b, fac=4 * a * c))
    print("\tDelta = {}".format(delta))
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

def calculate_solutions_degree_2(a, b, delta):
    solutions = []
    if (delta < 0):
        print(bcolors.HEADER + "Solving complex form :" + bcolors.ENDC)
        pos_delta = -delta
        print("Absolute value of delta : {}".format(pos_delta))
        print(bcolors.HEADER + "Calculate real part :" + bcolors.ENDC)
        real_part = round_float(-b / (2 * a))
        print("real_part = -{b} / (2 * {a})".format(a=a, b=b))
        print("real_part = {b} / {a2}".format(a2=a * 2, b=-1 * b))
        print("real_part = {real}".format(real=real_part))
        print(bcolors.HEADER + "Calculate imaginary part :" + bcolors.ENDC)
        imaginary_part = round_float(square_root(pos_delta) / (2 * a)) + 'i'
        print("imaginary_part = (√{pos_delta} / (2 * {a})) * i".format(pos_delta=pos_delta, a=a))
        print("imaginary_part = (√{sq_delta} / {a2}) * i".format(sq_delta=square_root(pos_delta), a2=2 * a))
        print("imaginary_part = {not_i} * i".format(not_i=square_root(pos_delta) / (2 * a)))
        print("rounded imaginary_part = {i_p}".format(i_p=imaginary_part))
        print(bcolors.HEADER + "Solution 1 = " + bcolors.ENDC + "{} + {}".format(real_part, imaginary_part))
        print(bcolors.HEADER + "Solution 2 = " + bcolors.ENDC + "{} - {}".format(real_part, imaginary_part))
        solutions.append(real_part + '+' + imaginary_part)
        solutions.append(real_part + '-' + imaginary_part)
    elif (delta == 0):
        print(bcolors.HEADER + "Solving unique form :" + bcolors.ENDC)
        solutions.append(round_float(-b / (2 * a)))
    else:
        solutions.append(round_float((-b - square_root(delta)) / (2 * a)))
        solutions.append(round_float((-b + square_root(delta)) / (2 * a)))
    return solutions