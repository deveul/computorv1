#!/usr/bin/python3
# -*-coding:Utf-8 -*

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
    delta = float(b) * float(b) - 4 * float(a) * float(c) 
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
        pos_delta = -delta
        real_part = round_float(-b / (2 * a))
        imaginary_part = round_float(square_root(pos_delta) / (2 * a)) + 'i'
        solutions.append(real_part + '+' + imaginary_part)
        solutions.append(real_part + '-' + imaginary_part)
    elif (delta == 0):
        solutions.append(round_float(-b / (2 * a)))
    else:
        solutions.append(round_float((-b - square_root(delta)) / (2 * a)))
        solutions.append(round_float((-b + square_root(delta)) / (2 * a)))
    return solutions