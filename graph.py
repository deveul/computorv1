#!/usr/bin/python3
# -*-coding:Utf-8 -*
import matplotlib.pyplot as plt
import numpy as np 

def degree_2_graph(a, b, c):
    results = np.array([a * (x*x) + (b * x) + c for x in np.arange(-10.0, 10.0, 0.1)])
    small_results = np.array([a * (x*x) + (b * x) + c for x in np.arange(-2.0, 2.0, 0.1)])

    plt.axes = ([-10.0, 10.0, min(results), max(results)])
    axes = plt.gca()
    axes.set_xlim([-2.0, 2.0])
    axes.set_ylim([min(small_results) - 0.5, max(small_results) + 0.5])
    plt.axhline(0, color='grey')
    plt.axvline(0, color='grey')
    plt.plot(np.array(np.arange(-10.0, 10.0, 0.1)), results, 'r-')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Polynomial Curve of y = {}x² + {}x + {}'.format(a,b,c))
    
    plt.show()

def degree_1_graph(a, b):
    results = np.array([a * x + b for x in np.arange(-10.0, 10.0, 0.1)])
    small_results = np.array([a * x + b for x in np.arange(-2.0, 2.0, 0.1)])

    plt.axes = ([-10.0, 10.0, min(results), max(results)])
    axes = plt.gca()
    axes.set_xlim([-2.0, 2.0])
    axes.set_ylim([min(small_results) - 0.5, max(small_results) + 0.5])
    plt.axhline(0, color='grey')
    plt.axvline(0, color='grey')
    plt.plot(np.array(np.arange(-10.0, 10.0, 0.1)), results, 'r-')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Polynomial Curve of y = {}x + {}'.format(a,b))
    
    plt.show()

def poly_graph(coefficients):
    degree = len(coefficients) - 1
    if degree == 2:
        degree_2_graph(coefficients[2], coefficients[1], coefficients[0])
    elif degree == 1:
        degree_1_graph(coefficients[1], coefficients[0])
    else:
        print("Cannot represent a graph for the degree {}".format(degree))