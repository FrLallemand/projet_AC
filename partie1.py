#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
sys.setrecursionlimit(10000) # 10000 is an example, try with different values

'''
Calcule le produit de deux nombres x et y necessitant plus de 32 bits
et calcule le modulo par p

Opération lente, n'utiliser que si necessaire.
'''
def multiply(x, y, p):
    result = 0
    while y:
        if y & 1 :
            result = (result + x) % p

        y  >>= 1
        x = (2*x)%p
    return result


'''
Calcule x^k mod p;
Le calcul doit être en O(log K)
'''
def puissance(x, k, p):
    result = 1
    while k:
        if k & 1 :
            result = multiply(result, x , p)
        k >>= 1
        x = multiply(x, x , p)
    return result

print(puissance(125, 687, 15))
