#!/usr/bin/python3
# -*-coding:Utf-8 -*

import re
from itertools import zip_longest

def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)

class Parse:
    def __init__(self, equation):
        self.equation = ''.join(equation.split())
        self.left = self.get_left()
        self.right = self.get_right()
        self.left_list = self.get_left_list()
        self.right_list = self.get_right_list()
        self.reduced_elements = []

    def get_left(self):
        left = self.equation.split('=')[0]
        if left[0] != '-' and left[0] != '+':
            left = '+' + left
        return left
        
    def get_right(self):
        right = self.equation.split('=')[1]
        if right[0] != '-' and right[0] != '+':
            right = '+' + right
        return right

    def get_left_list(self):
        tmp_list = [w for w in re.split(r'(\-|\+)', self.left) if len(w) > 0]
        return [tmp_list[n] + tmp_list[n + 1] for n in range(0, len(tmp_list), 2)]
        
    def get_right_list(self):
        tmp_list = [w for w in re.split(r'(\-|\+)', self.right) if len(w) > 0]
        return [tmp_list[n] + tmp_list[n + 1] for n in range(0, len(tmp_list), 2)]

    def sort_elements(self):
        self.left_list = sorted(self.left_list, key=lambda elem: elem.split('^')[1])
        self.right_list = sorted(self.right_list, key=lambda elem: elem.split('^')[1])

    def fill_list(self):
        for index, item in enumerate(self.left_list):
            power = int(item.split('^')[1])
            if power > index:
                self.left_list.insert(index, 0)
        print(self.left_list)
        for index, item in enumerate(self.right_list):
            power = int(item.split('^')[1])
            if power > index:
                self.right_list.insert(index, 0)
        print(self.right_list)


    def set_reduced_elements(self, left_list, right_list):
        new_list = list(zip_longest(left_list, right_list, fillvalue=0))
        print(new_list)
        new_list = [self.reducing(x) for x in new_list]
        while (len(new_list) > 1 and new_list[-1] == 0):
            new_list.pop(-1)
        self.reduced_elements = new_list

    def reducing(self, element):
        if element[0] != 0:
            left_elem = element[0].split('*')[0]
        else:
            left_elem = '0'
        if element[1] != 0:
            right_elem = element[1].split('*')[0]
        else:
            right_elem = '0'
        elem = float(left_elem) + float(right_elem) * -1
        return elem if not elem.is_integer() else int(elem)

def check_list(list_eq):
    for item in list_eq:
        # m = re.match(r"^(\+|-)[0-9]+\*?(X|x)(\^?[0-9]+)*$", item)
        m = re.match(r"^(\+|-)[0-9]+\*?(X|x)\^[0-9]+$", item)
        if not m:
            if item[0] == '+' or item[0] == '-':
                item = item[1:]
            print("Item {} is not of the form a * X^x".format(item))
            exit()

def parse_equation(equation):
    eq = Parse(equation)
    check_list(eq.left_list + eq.right_list)
    eq.sort_elements()
    eq.fill_list()
    eq.set_reduced_elements(eq.left_list, eq.right_list)
    return eq