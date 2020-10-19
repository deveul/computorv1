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