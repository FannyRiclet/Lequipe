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


def comparaison_globale(Nom_dev,Nom_Candidat,liste_noms_candidats):
    """Compare les codes d'un candidat avec les codes de tous les autres candidats
    en utilisant la fonction comparant deux candidats
    :param Nom_Candidat : nom candidat voulu
    :param Nom_dev : nom developeur pour trouver le filepath
    :return : un tableau double entree qui, dans chaque colonne,
    donne le taux de ressemblance du code du candidat avec un autre
    candidat X, pour differents criteres (les lignes)"""

    data=comparaison_deux_candidats(Nom_dev, Nom_Candidat, liste_noms_candidats[0])
    df=pd.DataFrame(data, index=[liste_noms_candidats[0]])
    liste_noms_candidats.remove(Nom_Candidat)
    for k in range(1,len(liste_noms_candidats)) :
        data2=comparaison_deux_candidats(Nom_dev, Nom_Candidat, liste_noms_candidats[k])
        df2 = pd.DataFrame(data2, index=[liste_noms_candidats[k]])
        df=df.append(df2)
    print(df)
    return df
