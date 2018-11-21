import sys
sys.path.append('../MVP 4 ')
from Tableau_recapitulatif import *

liste_criteres = ['Nombre fonctions','Nombre tests', 'Nombre commentaires', 'Nombre variables', 'Taille fonctions', 'Longueur nom fonction', 'Longueur nom variable', 'Nombre imbrications', 'Nombre duplications' ]

def comparaison_deux_candidats(filepath1,filepathtest1, filepath2, filepathtest2,liste_criteres):
    """Compare un fichier  d'un candidats sur les criteres determines en mvp1 et mvp2
    :param filepath1: fichier ruby du candidat1
    :param filepathtest1 : fichier test ruby du candidat1
    :param filepath2: fichier ruby du candidat2
    :param filepathtest2 : fichier test ruby du candidat2
    :param liste_critere : liste des criteres de comparaison
    :return: Un dictionnaire contenant le nom du critere et le taux de ressemblance pour ce critere
    """
    dict1=data_finale(filepath1,filepathtest1)
    dict2=data_finale(filepath2, filepathtest2)
    dico={}
    for x in liste_criteres :
        dico[x]=min(dict1[x],dict2[x])/max(dict1[x],dict2[x])*100
    return dico




