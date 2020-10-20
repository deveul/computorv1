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
        if len(left) == 0:
            print("Left side of the equation is missing.")
            exit()
        if left[0] != '-' and left[0] != '+':
            left = '+' + left
        return left
        
    def get_right(self):
        right = self.equation.split('=')[1]
        if len(right) == 0:
            print("Right side of the equation is missing.")
            exit()
        if right[0] != '-' and right[0] != '+':
            right = '+' + right
        return right

    def get_left_list(self):
        if re.search(r"(\+|-)(\+|-)", self.left):
            print("Two (+|-) signs found next to each other: error.")
            exit()
        tmp_list = [w for w in re.split(r'(\-|\+)', self.left) if len(w) > 0]
        return [tmp_list[n] + tmp_list[n + 1] for n in range(0, len(tmp_list), 2)]
        
    def get_right_list(self):
        if re.search(r"(\+|-)(\+|-)", self.right):
            print("Two (+|-) signs found next to each other: error.")
            exit()
        tmp_list = [w for w in re.split(r'(\-|\+)', self.right) if len(w) > 0]
        return [tmp_list[n] + tmp_list[n + 1] for n in range(0, len(tmp_list), 2)]

    def sort_elements(self):
        self.left_list = sorted(self.left_list, key=lambda elem: elem.split('^')[1])
        self.right_list = sorted(self.right_list, key=lambda elem: elem.split('^')[1])

    def join_elements(self):
        left_elems = [item.split('*X^') for item in self.left_list]
        new_left = [left_elems[0]]
        for elem in left_elems[1:]:
            if elem[1] == new_left[len(new_left) - 1][1]:
                new_left[len(new_left) - 1] = [float(new_left[len(new_left) - 1][0]) + float(elem[0]), elem[1]]
            else:
                new_left.append(elem)
        new_left = ['*X^'.join(map(str, item)) for item in new_left]
        for index, item in enumerate(new_left):
            if item[0] != '-' and item[0] != '+':
                new_left[index] = '+' + new_left[index]
        self.left_list = new_left
        right_elems = [item.split('*X^') for item in self.right_list]
        new_right = [right_elems[0]]
        for elem in right_elems[1:]:
            if elem[1] == new_right[len(new_right) - 1][1]:
                new_right[len(new_right) - 1] = [float(new_right[len(new_right) - 1][0]) + float(elem[0]), elem[1]]
            else:
                new_right.append(elem)
        new_right = ['*X^'.join(map(str, item)) for item in new_right]
        for index, item in enumerate(new_right):
            if item[0] != '-' and item[0] != '+':
                new_right[index] = '+' + new_right[index]
        self.right_list = new_right
        
        

    def fill_list(self):
        for index, item in enumerate(self.left_list):
            power = int(item.split('^')[1])
            if power > index:
                self.left_list.insert(index, 0)
        for index, item in enumerate(self.right_list):
            power = int(item.split('^')[1])
            if power > index:
                self.right_list.insert(index, 0)


    def set_reduced_elements(self, left_list, right_list):
        new_list = list(zip_longest(left_list, right_list, fillvalue=0))
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

def transform_list(list_eq):
    new_list = list(list_eq)
    for index, item in enumerate(list_eq):
        if '*' in item and '^' in item:
            pass
        elif '*' in item:
            if item.count('*') != 1:
                print("Too many '*' in the element: {}".format(item))
                exit()
            parts = item.split('*')
            if parts[1] == 'X':
                new_list[index] = item + '^1'
        elif '^' in item:
            if item.count('^') != 1:
                print("Too many '^' in the element: {}".format(item))
                exit()
            char_before_pow = item[item.index('^') - 1]
            if char_before_pow != 'X':
                print("I can't transform the element '{}' in the form 'a * X^x'".format(item))
                exit()
            before_pow = item.split('{}^'.format(char_before_pow))[0]
            if len(before_pow) == 1:
                new_list[index] = item[:1] + '1*' + item[1:]
            else:
                n = item.index('^') - 1
                new_list[index] = item[:n] + '*' + item[n:]
        else:
            if not 'X' in item:
                try:
                    float(item)
                    new_list[index] = item + '*X^0'
                except ValueError:
                    print("The element {} doesn't seem to be a float.".format(item))
                    exit()
            else:
                if re.match(r"^(\+|-)[0-9]+(?:\.[0-9]+)?X", item):
                    new_list[index] = item[:item.index('X')] + '*' + item[item.index('X'):] + '^1'
                if re.match(r"^(\+|-)X", item):
                    new_list[index] = item[0] + '1*' + item[item.index('X'):] + '^1'
    return new_list

def check_list(list_eq):
    for item in list_eq:
        # m = re.match(r"^(\+|-)[0-9]+\*?(X|x)(\^?[0-9]+)*$", item)
        m = re.match(r"^(\+|-)[0-9]+\*X\^[0-9]+$", item)
        n = re.match(r"^(\+|-)[0-9]+\.?[0-9]+\*X\^[0-9]+$", item)
        if not m and not n:
            if item[0] == '+' or item[0] == '-':
                item = item[1:]
            print("Element {} is not of the form a * X^n".format(item))
            exit()

def parse_equation(equation):
    if '=' not in equation:
        print("It does not seem to be an equation, '=' is missing.")
        exit()
    if equation.count('=') > 1:
        print("It does not seem to be a valid equation, '=' should be present once and only once.")
        exit()
    equation = "".join(['X' if char == 'x' else char for char in equation])
    eq = Parse(equation)
    eq.left_list = transform_list(eq.left_list)
    eq.right_list = transform_list(eq.right_list)
    check_list(eq.left_list + eq.right_list)
    eq.sort_elements()
    eq.join_elements()
    eq.fill_list()
    eq.set_reduced_elements(eq.left_list, eq.right_list)
    return eq