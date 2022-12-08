#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 23:32:05 2021

@author: yassine

"""
from math import sqrt, log

def f(x):
    return x - sqrt(2)

def g(x):
    return 1

def dichotomie(f, a, b, n):
    if f(a) * f(b) > 0:
        return
    else:
        for i in range(n):
            if f((a+b)/2) == 0:
                return (a+b)/2
            elif f((a+b)/2) > 0:
                b = (a+b)/2
                res = b
            elif f((a+b)/2) < 0:
                a = (a+b) / 2
                res = a
        return res

def newton(function, derivate_function, initial_value, iterations):
    for i in range(iterations):
        initial_value =  initial_value - (function(initial_value) / derivate_function(initial_value))
    return initial_value
    
def dichotomie2(function, a, b, e):
    n = log((b-a)/e) / log(2)
    n = int(n)
    return dichotomie(function, a, b, n)

sqrtt_2 = dichotomie(f, 1, 3, 3)
print("3 iterations (dichotomie): ", sqrtt_2);
sqrtt_2 = dichotomie(f, 0, 3, 10);
print("10 iterations (dichotomie): ", sqrtt_2);
sqrtt_2 = dichotomie(f, 0, 3, 30);
print("30 iterations (dichotomie): ", sqrtt_2);
sqrtt_2 = newton(f, g, 3, 3);
print("3 iterations (newton): ", sqrtt_2);
sqrtt_2 = newton(f, g, 3, 10);
print("10 iterations (newton): ", sqrtt_2);
sqrtt_2 = newton(f, g, 3, 30);
print("30 iterations (newton): ", sqrtt_2);
