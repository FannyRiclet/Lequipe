#comparer un candidat avec tous les autres en utilisant la fonction comparer deux candidats
import sys
import numpy as np

#comparaison_deux_candidats
#chaque candidat a un dico associé

sys.path.append('../MVP 4')
from Tableau_recapitulatif import *

filepath=
liste_noms_candidats=['CandidatA','CandidatB','CandidatC']
liste_filepath_candidats=['{}/Event{}.rb'.format(filepath,x) for x in liste_noms_candidats]
liste_filepath_test_candidats=['{}/Event{}Test.rb'.format(filepath,x) for x in liste_noms_candidats]
liste_criteres=

sys.path.append('../MVP 3')
from Fonctionnalite3_2 import * #dont comparaison_deux_candidats


def comparaison_globale(fp_candidat, fp_candidat_test):
    T=np.array()
    T[0][0]=0
    T[0].append(liste_noms_candidats) #creation de la premiere ligne
    T[:,0]=liste_criteres
    for j in len(liste_noms_candidats):
        dico=comparaison_deux_candidats(fp_candidat, fp_candidat_test, liste_filepath_candidats[j], liste_filepath_test_candidats[j])
        for i in len(liste_criteres):
            T[i,j]=dico[i]
    return T

