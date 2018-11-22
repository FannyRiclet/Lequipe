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
    liste_criteres = data_finale(filepath1,filepathtest1)
    dict1=data_finale(filepath1,filepathtest1)
    dict2=data_finale(filepath2, filepathtest2)
    dico={}
    for x in liste_criteres :
        dico[x]=min(dict1[x],dict2[x])/max(dict1[x],dict2[x])*100
    return dico




