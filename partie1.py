#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse

from random import randint
import sys

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
    result = randint(2, pow(2, 23)-1)
    is_prime = pseudoprime(result)
    while not is_prime :
        result = randint(2, pow(2, 23)-1)
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

'''
Calcule le fingerprint d'un bloc.
'''
def fingerprint_blocs(bloc_length, data , p):
    add_result = 0
    (begining, end) = bloc_length
    for i in range(begining, end):
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
Vérifie si le fichier parent_file contient le fichier child_file
'''
def is_in_file(parent_file, child_file):
    result = False
    p = nextprime()
    child_fingerprint = fingerprint(p, child_file)

    f = open(child_file, "rb")
    child_data = f.read()
    f.close()
    child_data_length = len(child_data)

    f = open(child_file, "rb")
    parent_data = f.read()
    f.close()
    parent_data_length = len(child_data)

    #Calcul du nombre de blocs dans le parent : on retire la taille d'un bloc enfant et ajoute le premier bloc
    blocs_number = parent_data_length - child_data_length + 1

    #Calcul du fingerprint pour le premier bloc.

    begining = 0
    end = begining + child_data_length
    fingerprint = fingerprint_blocs((begining, end), parent_data, p)
    for i in range(1, blocs_number):
        """
        ((fingerprint - parent_data[begining]*256^(child_data_length-1))*256 + parent_data[end+1]) mod p
        end sera incrémenté en début de tour
        Décomposition du calcul en une série de modulos
        """
        if fingerprint == child_fingerprint:
            result = True
            break

        end++

        m1 = modular_multiplication(parent_data[begining],
                                     puissance_v2(256,
                                                  child_data_length-1,
                                                  p),
                                     p)

        m2 = modular_addition(fingerprint, (-m1), p)
        m3 = modular_multiplication(m2, 256, p)
        fingerprint = modular_addition(m3, parent_data[end], p)
        begining++

    return result



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Calcule le fingerprint d'un fichier donné.")
    parser.add_argument('-p', '--prime', metavar='P', type=int, nargs='?',
                        help='Nombre premier', required=False)
    parser.add_argument('-f', '--filename', metavar='File', type=str, nargs='?',
                        help="Fichier d'entrée")
    args = parser.parse_args()
    if not args.prime :
        args.prime = nextprime()

    args.prime = nextprime()
    f2 = fingerprint(args.prime, args.filename)

    print("\n")
    print("Prime     : " + str(args.prime))
    print("Fichier 2 : " + str(f2))
