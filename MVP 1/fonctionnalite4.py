<<<<<<< HEAD
<<<<<<< HEAD
from Fonctionnalite2_5 import *

def note_functions(dict,filepath):
    if 4<=dict['Nombrefonctions']<=6:
        note=10
        for k in range(len(function_size(filepath)[0])):
            if not 4<=function_size(filepath)[0][k]<=8:
                note-=0,5
        if note <0:
            return 0
    if 2<=dict['Nombrefonctions']<4 or 6<dict['Nombrefonctions']<=8:
        note=8
        for k in range(len(function_size(filepath)[0])):
            if not 4<=function_size(filepath)[0][k]<=8:
                note-=0,5
        if note <0:
            return 0
    if 0<=dict['Nombrefonctions']<2 or 8<dict['Nombrefonctions']:
        note=5
        for k in range(len(function_size(filepath)[0])):
            if not 4<=function_size(filepath)[0][k]<=8:
                note-=0,5
        if note <0:
            return 0


=======
def note_rapport_tests_fonctions(nb_tests,nb_fonctions):
    rapport = nb_tests/nb_fonctions
    if rapport > 1:
        return 10
    else:
        return rapport*10
>>>>>>> 9c55c1339d071178371e989ca28f207faf9e238c

=======
#rapport
'''Rapport lignes comm/lignes total :
0 : 0
1 : 0,02
2 : 0,04
3 : 0,06
4 : 0,08
5 : 0,1
6 : 0,12
7 : 0,14
8 : 0,16
9 : 0,18
10 : 0,2'''

from Analyse_Globale import *

def note_rapport_comm_ligne(dict):
    nb_comm=dict['Nombrecommentaires']
    nb_lignes=dict['Nombrelignes']
    r=nb_comm/nb_lignes
    return (r*1000)/2

print(note_rapport_comm_ligne(data(filepath)))
>>>>>>> branche_lison
