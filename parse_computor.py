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
        self.reduced_elements = self.get_reduced_elements()

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

    def get_reduced_elements(self):
        new_list = list(zip_longest(self.left_list, self.right_list, fillvalue=0))
        new_list = [self.reducing(x) for x in new_list]
        while (len(new_list) > 1 and new_list[-1] == 0):
            new_list.pop(-1)
        return new_list

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

def parse_equation(equation):
    return Parse(equation)