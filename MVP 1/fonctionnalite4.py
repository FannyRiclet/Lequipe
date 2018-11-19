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



def note_rapport_tests_fonctions(nb_tests,nb_fonctions):
    rapport = nb_tests/nb_fonctions
    if rapport > 1:
        return 10
    else:
        return rapport*10


