#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 14:37:41 2021

@author: yassine
"""

import numpy as np

def PolyLagrange(X, x, i):
   #Y = np.concatenate((X[:i], X[i+1:]), axis = None)
    res = 1
    for j in range(len(X)):
        if j != i:
            res = res * ((x - X[j]) / (X[i] - X[j]))
    return res

def InterpLagrange(X, f, x):
    res = 0
    Y = []
    for i in range(len(X)):
        Y.append(f(X[i]))
        res = res + (PolyLagrange(X,x,i) * Y[i])
    return res

