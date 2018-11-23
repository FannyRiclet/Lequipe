#comparer un candidat avec tous les autres en utilisant la fonction comparer deux candidats
#j'utilise aussi le tableau recapitulatif de la MVP 4
import pandas as pd
import sys
import numpy as np

sys.path.append('../MVP 4')
from Tableau_recapitulatif import * #dont data_candidats


liste_noms_candidats=['CandidatA','CandidatB','CandidatC']


sys.path.append('../MVP 3')
from Fonctionnalite3_2 import * #dont comparaison_deux_candidats


def comparaison_globale(Nom_dev,filepath,filepathtest):
    """Compare les codes d'un candidat avec les codes de tous les autres candidats
    en utilisant la fonction comparant deux candidats
    :param filepath : filepath du candidat voulu
    :param filepathtest : filepath test du candidat voulu
    :return : un tableau double entree qui, dans chaque colonne,
    donne le taux de ressemblance du code du candidat avec un autre
    candidat X, pour differents criteres (les lignes)"""
    liste_criteres=data_candidats(Nom_dev,liste_noms_candidats)[:,0][3:]
    T=np.array()
    T[0][0]=0
    T[0].append(liste_noms_candidats) #creation de la premiere ligne
    T[:,0]=liste_criteres
    for j in len(liste_noms_candidats):
        filepath_j=data_candidats(Nom_dev,liste_noms_candidats)[1][j]
        filepathtest_j=data_candidats(Nom_dev,liste_noms_candidats)[2][j]
        dico=comparaison_deux_candidats(filepath, filepathtest, filepath_j, filepathtest_j)
        for i in len(liste_criteres):
            T[i,j]=dico[i]
    return T
