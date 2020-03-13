#!/usr/bin/env python

import sys

def add():
    x = int(sys.argv[1])
    y = int(sys.argv[2])

if __name__== "__main__":
        if (len(sys.argv) < 3):
                print("Erreur!")
                print("Le nombre de valeurs inserer doit etre deux.")

        elif (len(sys.argv) > 3):
                print("Erreur!")
                print("Inserer pas plus que de deux valeurs.")

        else:
                print(sys.argv)
                print("La somme est: ") + (str(int(sys.argv[1]) + int(sys.argv[2])))

