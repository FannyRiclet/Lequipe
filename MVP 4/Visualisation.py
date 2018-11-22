from Tableau_recapitulatif import *
import numpy as np
import matplotlib.pyplot as plt

def visualisation_1candidat(Nom_dev, Nom_Candidat):
    Data=donnees_brutes_candidat_finales(Nom_dev,Nom_Candidat)
    Note=note_candidat(Nom_dev,Nom_Candidat)
    n1=np.shape(Data)[0]
    n2=np.shape(Note)[0]
    X1=[]
    Y1=[]
    X2=[]
    Y2=[]
    for k in range(3,n1):
        X1.append(Data[k][0])
        Y1.append(Data[k][1])
    for k in range(3,n2):
        X2.append(Note[k][0])
        Y2.append(Note[k][1])
    plt.plot.scatter(X1,Y1, s=40, c='blue', label='Données brutes')
    plt.title('Analyse données code candidat')
    plt.show()

    plt.plot.scatter(X2,Y2, s=40, c='orange', label='Note critères')
    plt.title('Analyse critères code candidat')
    plt.show()


visualisation_1candidat('Gros','CandidatA')

