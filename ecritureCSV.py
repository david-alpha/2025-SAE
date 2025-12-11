#!/usr/bin/env python
# -*-coding: utf-8 -*

entetes = [
     u'Colonne1',
     u'Colonne2',
     u'Colonne3',
     u'Colonne4',
     u'Colonne5'
]

valeurs = [
     [u'Valeur1', u'Valeur2', u'Valeur3', u'Valeur4', u'Valeur5'],
     [u'Valeur6', u'Valeur7', u'Valeur8', u'Valeur9', u'Valeur10'],
     [u'Valeur11', u'Valeur12', u'Valeur13', u'Valeur14', u'Valeur15']
]

f = open('monFichier.csv', 'w')
ligneEntete = ";".join(entetes) + "\n"
f.write(ligneEntete)
for valeur in valeurs:
     ligne = ";".join(valeur) + "\n"
     f.write(ligne)

f.close()