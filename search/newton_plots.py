#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 23:46:54 2021

@author: yassine
"""

from matplotlib import pyplot as plt

def f(x):
    return pow(x, 3) - x - 3

def g(x):
    return 3 * pow(x, 2) - 1

def newton(function, derivate_function, initial_value, iterations):
    for i in range(iterations):
        initial_value =  initial_value - (function(initial_value) / derivate_function(initial_value))
    return initial_value

N = [i for i in range(101)]
ALPHA = []
for i in N:
    ALPHA.append(newton(f, g, 0, i))
plt.plot(ALPHA, N)
plt.xlabel("Alpha0 values")
plt.ylabel("Iterations")
plt.show