import sys

sys.path.append('../MVP 4')
from Tableau_recapitulatif import *


def comparaison_deux_candidats(filepath1,filepathtest1, filepath2, filepathtest2):
    """Compare un fichier  d'un candidats sur les criteres determines en mvp1 et mvp2
    :param filepath1: fichier ruby du candidat1
    :param filepathtest1 : fichier test ruby du candidat1
    :param filepath2: fichier ruby du candidat2
    :param filepathtest2 : fichier test ruby du candidat2
    :return: Un dictionnaire contenant le nom du critere et le taux de ressemblance pour ce critere
    """
    liste_criteres = data_finale(filepath1,filepathtest1).keys()
    dict1=data_finale(filepath1,filepathtest1)
    dict2=data_finale(filepath2, filepathtest2)
    dico={}
    c=0
    for x in liste_criteres :
        if type(dict1[x]) == float or type(dict1[x]) == int :
            if max(dict1[x],dict2[x]) == 0 :
                dico[x]=0
            else :
                dico[x]=min(dict1[x],dict2[x])/max(dict1[x],dict2[x])*100
        else :
            avg1,avg2=dict1[x][1],dict2[x][1]
            if max(avg1,avg2) == 0 :
                dico[x]=0
            else :
                dico[x]=min(avg1,avg2)/max(avg1,avg2)*100
    return(dico)

import numpy as np
