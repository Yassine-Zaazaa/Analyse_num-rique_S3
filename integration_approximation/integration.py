#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 09:08:33 2021

@author: yassine
"""

from math import ceil, exp, sqrt, log
from scipy.integrate import quad
from sympy import diff

def RectangleDroite(f, a, b, n):
    h = (b-a)/n
    ak = a + h
    sigma = 0
    for i in range(n):
        sigma += f(ak)
        ak += h
    res = h*sigma
    return res

def RectangleGauche(f, a, b, n):
    h = (b-a)/n
    ak = a
    sigma = 0
    for i in range(n):
        sigma += f(ak)
        ak += h
    res = h * sigma
    return res

def Trapeze(f, a, b, n):
    h = (b-a)/n
    ak = a
    sigma = f(ak)/2
    for i in range(n-1):
        ak += h
        sigma += f(ak)
    sigma += f(b) / 2
    res = h * sigma
    return res

def Simpson(f, a, b, n):
    h = (b-a)/n
    ak = a + h
    sigma_zk = 0
    sigma_ak = 0
    z = a + h/2
    for i in range(n-1):
        sigma_ak += f(ak) 
        sigma_zk += f(z)
        z += h
        ak += h
    sigma_zk += f(z)
    return ((h/6)*(f(a)+f(b)+2*sigma_ak+4*sigma_zk))

def function(x):
    return exp((-pow(x,2))/2)

print(Trapeze(lambda x : log(x), 1, 2, 2))
print(quad(lambda x : log(x), 1, 2))


print("On teste la fonction qui s'approche la plus vite de la valeur de l'integrale")
print("On teste avec l'integrale : exp(−t²/2)")
print("Fonction rectangle droite: ", RectangleDroite(function, 0, 1, 100))
print("Fonction rectangle gauche: ", RectangleGauche(function, 0, 1, 100))
print("Fonction trapeze: ", Trapeze(function, 0, 1, 100))
print("Fonction simpson: ", Simpson(function, 0, 1, 100))
print("Voici la valeur de cette integrale avec l'erreur: ", quad(function, 0, 1))
print("On peut donc conclure que la fonction simpson s'approche la plus vite de la valeur de l'integrale.")

def NombreNecessaire(f, a, b, Err, Methode):
    if Methode == "RectangleDroite" or Methode == "RectangleGauche":
        return ((pow(b-a, 2) / (2 * Err)) * max(diff(f,x)))