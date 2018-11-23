from Tableau_recapitulatif import *
from Comparaison_candidats import *
import matplotlib.pyplot as plt

def visualisation_1candidat(Nom_dev, Nom_Candidat):
    df=donnees_finales(Nom_dev,Nom_Candidat).transpose()
    df.plot()
    plt.show()

liste_noms_candidats=['CandidatA','CandidatB','CandidatC']

def visualisation_candidats(Nom_dev,liste_noms_candidats) :
    df=data_candidats(Nom_dev, liste_noms_candidats).transpose()
    df.plot()
    plt.show()

visualisation_1candidat('Gros','CandidatC')
visualisation_candidats('Gros',liste_noms_candidats)
