#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from random import randint

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

def puissance(x, k, p, method="iteratif"):
    if method == "iteratif":
        return puissance_iteratif(x,k,p)
    elif method == "recursif":
        return puissance_recursif(x,k,p)

'''
Calcule x^k mod p;
Le calcul doit être en O(log K)
'''
def puissance_iteratif(x, k, p):
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


def pseudoprime(p):
    if (puissance(2, p-1, p) == 1) :
        return True
    return False

def nextprime():
    result = randint(2, pow(2, 31)-1)
    is_prime = pseudoprime(result)
    while not is_prime :
        result = randint(2, pow(2, 31)-1)
        is_prime = pseudoprime(result)
    return result


'''
Calcule le fingerprint de fn
'''
def fingerprint(p, fn):
    f = open(fn, "rb")
    data = f.read()
    f.close()
    data_length = len(data)
    add_result = 0
    for i in range(0, data_length):
        mult_result = modular_multiplication(data[i],
                                             puissance_v2(256,
                                                          data_length-i-1,
                                                          p),
                                             p)
        add_result = modular_addition(add_result,
                                      mult_result,
                                      p)
    return add_result



'''
calcul sans multiply
'''
def puissance_v2(x, k, p):
    result = 1
    while k:
        if k & 1 :
            result = (result*x)%p
        k >>= 1
        x = (x*x)%p
    return result

def modular_addition(a, b, c):
    return ((a%c) + (b%c)) % c

def modular_multiplication(a, b, c):
    return ((a%c) * (b%c)) % c

print(fingerprint(5407, "tests/test1"))
