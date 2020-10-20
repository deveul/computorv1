#!/usr/bin/python3
# -*-coding:Utf-8 -*

from print_computor import print_delta_verbose, print_positive_degree2_verbose, print_zero_degree2_verbose, print_negative_degree2_verbose
from basic_operations import square_root

def calculate_delta(a, b, c, verbose):
    delta = b * b - 4 * a * c 
    if verbose:
        print_delta_verbose(a, b, c, delta)
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
            print_negative_degree2_verbose(a, b, delta, pos_delta, real_part, imaginary_part, solutions)
    elif (delta == 0):
        solutions.append(round_float(-b / (2 * a)))
        if verbose:
            print_zero_degree2_verbose(a, b, solutions)
    else:
        solutions.append(round_float((-b - square_root(delta)) / (2 * a)))
        solutions.append(round_float((-b + square_root(delta)) / (2 * a)))
        if verbose:
            print_positive_degree2_verbose(a, b, delta, solutions)

    return solutions