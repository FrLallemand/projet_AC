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
'''
def puissance(x, k, p):
    result = 1
    while k:
        if k & 1 :
            result = multiply(result, x , p)
        k >>= 1
        x = multiply(x, x , p)
    return result

'''
Calcule x^k mod p de façon récursive
'''
def puissance_recursion(x, k, p):
    result = x % p;
    if k == 0:
        return 1
    elif k == 1:
        return result
    elif k%2 == 0:
        return puissance_recursion(multiply(result, result, p), k//2, p)
    else :
        return multiply(result, puissance_recursion(result, k-1, p), p)

print(puissance_recursion(125, 687, 15))
