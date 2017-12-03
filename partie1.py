#!/usr/bin/env python3
# -*- coding: utf-8 -*-


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

https://fr.wikipedia.org/wiki/Exponentiation_modulaire#La_m%C3%A9thode_la_plus_efficace
'''
def puissance(x, k, p):
    result = 1;
    while k > 0:
        if (k & 1) > 0  :
            result = (result * x) % p
        k  >>= 1
        x = (x*x)%p

    return result

print(puissance(3, 2, 2))
