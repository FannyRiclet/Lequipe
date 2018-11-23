from Tableau_recapitulatif import *
from Comparaison_candidats import *
import matplotlib.pyplot as plt

def visualisation_1candidat(Nom_dev, Nom_Candidat):
    df=donnees_finales(Nom_dev,Nom_Candidat).transpose()
    plt.style.use('ggplot')
# figure
    fig = plt.figure(figsize=(158, 16))
    ax = fig.add_subplot(111)
    ax.set_title('Résultats {}'.format(Nom_Candidat), color="#555555")
# plot the differents quantities
    ax.plot(df.index, df[Nom_Candidat], marker="o", label=Nom_Candidat, linestyle="--", linewidth=.5)
# format and style
    ax.set_xlabel("Critères")
    ax.set_ylabel("")
    ax.legend()
    plt.show()

liste_noms_candidats=['CandidatA','CandidatB','CandidatC']

def visualisation_candidats(Nom_dev,liste_noms_candidats) :
    df=data_candidats(Nom_dev, liste_noms_candidats).transpose()
    plt.style.use('ggplot')
# figure
    fig = plt.figure(figsize=(158, 16))
    ax = fig.add_subplot(111)
    ax.set_title('Comparaison des critères entre candidats', color="#555555")
# plot the differents quantities
    for candidat in liste_noms_candidats :
        ax.plot(df.index, df[candidat], marker="o", label=candidat, linestyle="--", linewidth=.5)
# format and style
    ax.set_xlabel("Critères")
    ax.set_ylabel("")
    ax.legend()
    plt.show()

visualisation_1candidat('Gros','CandidatC')
visualisation_candidats('Gros',liste_noms_candidats)
