from Fonctionnalite2_5 import *
from Resultat_candidats import *

def note_functions(dict, filepath):
    if 4<=dict['Nombre fonctions']<=6:
        note=10
        for k in range(len(function_size(filepath)[0])):
            if not 4<=function_size(filepath)[0][k]<=8:
                note-=0.5
        if note <0:
            return 0
    if 2<=dict['Nombre fonctions']<4 or 6<dict['Nombre fonctions']<=8:
        note=8
        for k in range(len(function_size(filepath)[0])):
            if not 4<=function_size(filepath)[0][k]<=8:
                note-=0.5
        if note <0:
            return 0
    if 0<=dict['Nombre fonctions']<2 or 8<dict['Nombre fonctions']:
        note=5
        for k in range(len(function_size(filepath)[0])):
            if not 4<=function_size(filepath)[0][k]<=8:
                note-=0.5
        if note <0:
            return 0
    return(note)


def note_rapport_tests_fonctions(dict):
    nb_tests,nb_fonctions = dict['Nombre tests'],dict['Nombre fonctions']
    rapport = nb_tests/nb_fonctions
    if rapport > 1:
        return 10
    else:
        return rapport*10


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

<<<<<<< HEAD

=======
>>>>>>> f04dd30791a5032a126f2f26a092b7a56fd8c9be
def note_rapport_comm_ligne(dict):
    nb_comm=dict['Nombre commentaires']
    nb_lignes=sum(dict['Taille fonctions'][0])
    r=nb_comm/nb_lignes
    return (r*1000)/2
<<<<<<< HEAD

=======
>>>>>>> f04dd30791a5032a126f2f26a092b7a56fd8c9be


def rapport_variable_fonction(dico) :
    """Attribue une note au rapport du nombre de variables sur le nombre de fonctions
    :param dico : dictionnaire issu du la fonction data """
    nb_variable = dico['Nombrevariables']
    nb_fonctions = dico['Nombrefonctions']
    rapport = nb_variable/nb_fonctions
    if rapport in range(2,5) :
        return(10)
    elif rapport == 1 or rapport == 5 :
        return(8)
    else :
        return(0)
