from Fonctionnalite1_2_1 import *
from Fonctionnalite1_2_2 import *
from Fonctionnalite1_2_3 import *
from Fonctionnalite1_2_4 import *
from Fonctionnalite1_2_5 import *
from Fonctionnalite1_4 import *
import numpy as np
import pandas as pd

def data(filepath,filepathtest):
    """Renvoie les données brutes des critères (de MVP1)  pour analyser un fichier Ruby d'un candidat
    :param filepath : fichier ruby à analyser
    :return dict : dictionnaire contenant les critère et leur valeur"""
    dict={}
    dict['Nombre fonctions']=count_functions(filepath)
    dict['Nombre tests']=count_tests(filepathtest)
    dict['Nombre commentaires']=commentaires(filepath)
    dict['Nombre variables']=count_variables(filepath)
    dict['Taille fonctions']=function_size(filepath)
    return(dict)

def note_candidat(filepath,filepathtest) :
    """Renvoie les notes associées aux critères (de MVP1) analyses dans un fichier Ruby d'un candidat
    :param filepath, filepathtest : fichiers ruby à analyser
    :return dict : dictionnaire contenant les critère et leur notes"""
    donnees_brutes=data(filepath,filepathtest)
    table=np.array([['','Notes'],
                ['Nombre fonctions',note_functions(donnees_brutes,filepath)],
                ['Rapport test/fonction',note_rapport_tests_fonctions(donnees_brutes)],
                ['Rapport commentaire/ligne',note_rapport_comm_ligne(donnees_brutes)]])
    pd.table=pd.DataFrame(data=table[1:,1:], index=table[1:,0], columns=table[0,1:])
    return(pd.table)


def donnees_brutes_candidat(filepath,filepathtest) :
    """Renvoie les données brutes des critères (de MVP1) pour analyser un fichier Ruby d'un candidat dans un tableau panda
    :param filepath,filepathtest : fichiers ruby à analyser
    :return pd.table : tableau panda contenant les critère et leur valeur"""
    donnees_brutes=data(filepath,filepathtest)
    table=np.array([['','Données brutes'],
                ['Nombre fonctions',donnees_brutes['Nombre fonctions']],
                ['Nombre tests',donnees_brutes['Nombre tests']],
                ['Nombre commentaires',donnees_brutes['Nombre commentaires']],
                ['Nombre variables', donnees_brutes['Nombre variables']],
                ['Taille fonction moyenne', donnees_brutes['Taille fonctions'][2]]])
    pd.table = pd.DataFrame(data=table[1:,1:], index=table[1:,0], columns=table[0,1:])
    return(pd.table)


