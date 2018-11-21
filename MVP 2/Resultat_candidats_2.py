import numpy as np
import pandas as pd
from Fonctionnalite2_1 import *
from Fonctionnalite2_2 import *
from Fonctionnalite2_3 import *
from Fonctionnalite2_4 import *
from Fonctionnalite2_5 import *

def data2(filepath,filepathtest):
    """Renvoie les données brutes des critères pour analyser un fichier Ruby d'un candidat
    :param filepath : fichier ruby à analyser
    :return dict : dictionnaire contenant le critère et sa valeur"""
    dict={}
    dict['Longueur nom fonction']=longueur_nom_fonctions(filepath)
    dict['Longueur nom variable']=longueur_nom_variables(filepath)
    dict['Nombre imbrications']= count_imbrication(filepath)
    dict['Nombre duplications']=nombre_duplications(filepath)
    dict['Nom fonction pertinent']= fonctions_comprehensibles(filepath)
    dict['Nom variable pertinent']= variables_comprehensibles(filepath)
    return(dict)

filepath='C:/Users/Gros/PycharmProjects/Lequipe/EventCandidatA.rb'
filepathtest='C:/Users/Gros/PycharmProjects/Lequipe/EventCandidatATest.rb'


def donnees_brutes_candidat2(filepath,filepathtest) :
    donnees_brutes=data2(filepath,filepathtest)
    table=np.array([['','Données brutes'],
                ['Longueur nom fonction',donnees_brutes['Longueur nom fonction'][1]],
                ['Longueur nom variable',donnees_brutes['Longueur nom variable'][1]],
                ['Nombre imbrications',donnees_brutes['Nombre imbrications']],
                ['Nombre duplications', donnees_brutes['Nombre duplications']],
                ['Pertinence nom fonction', donnees_brutes['Nom fonction pertinent']],
                ['Pertinence nom variable', donnees_brutes['Nom variable pertinent']]
                     ])
    pd.table = pd.DataFrame(data=table[1:,1:], index=table[1:,0], columns=table[0,1:])
    return(pd.table)
