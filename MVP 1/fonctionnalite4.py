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
