#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Calcule le produit de deux nombres x et y necessitant plus de 32 bits
et calcule le modulo par p

Opération lente, n'utiliser que si necessaire
"""
def multiply(x, y, p):
    result = 0
    while y:
        if y & 1 :
            result = (result + x) % p
            y  >>= 1
            x = (2*x)%p

    return result;
