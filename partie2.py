#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse

from random import randint
import sys
import math

'''
retourne le nombre de boites dans le cas où les objets sont découpables.
'''
def fractionalPacking(objets, taille_boite):
    total = 0
    for obj in objets :
        total += obj
    return  math.ceil(total / taille_boite)

def firstFitPacking(objets, taille_boite):
    # Mise en ordre de la liste, dans l'ordre décroissant
    #objets.sort(reverse=True)
    remplissage = [(0, [])]
    objets_utilises = []
    boite_actuelle = 0
    #print("Boite : " + str(taille_boite))
    for obj in objets :
        fitted = False
        #print("Objet : " + str(obj))
        for i in range(0, len(remplissage)):
            # L'objet va dans la boite
            if remplissage[i][0]+obj <= taille_boite:
                remplissage[i][1].append(obj)
                remplissage[i] = (remplissage[i][0] + obj, remplissage[i][1])
                fitted = True
                break
        if not fitted :
            nouvelle_boite = (obj, [obj])
            remplissage.append(nouvelle_boite)

    return remplissage

def bestFitPacking(objets, taille_boite):
    # Mise en ordre de la liste, dans l'ordre décroissant
    #objets.sort(reverse=True)
    remplissage = [(0, [])]
    objets_utilises = []
    boite_actuelle = 0
    #print("Boite : " + str(taille_boite))
    for obj in objets :
        fitted = False
        bestFit = -1
        best_capacite = 0
        # On regarde si on trouve une boite
        for i in range(0, len(remplissage)):
            capacite = taille_boite - (remplissage[i][0]+obj)
            if capacite > best_capacite :
                best_capacite = capacite
                bestFit = i

        if bestFit == -1 :
            nouvelle_boite = (obj, [obj])
            remplissage.append(nouvelle_boite)
        else:
            remplissage[bestFit][1].append(obj)
            remplissage[bestFit] = (remplissage[bestFit][0] + obj, remplissage[bestFit][1])

    return remplissage

if __name__ == '__main__':
    objets = [4, 6, 9, 10, 2, 10, 3, 16]
    taille_boite = 27
    print(firstFitPacking(objets, taille_boite))
    print(bestFitPacking(objets, taille_boite))
