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
    for k in range(2,n1):
        X1.append(Data[k][0])
        Y1.append(Data[k][1])
    for k in range(2,n2):
        X2.append(Note[k][0])
        Y2.append(Note[k][1])
    plt.plot(X1,Y1)
    plt.plot(X2,Y2)
    plt.show()

visualisation_1candidat('Gros','CandidatA')

