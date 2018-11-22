from Tableau_recapitulatif import *
import numpy as np
import matplotlib.pyplot as plt

def visualisation (name_candidat):
    Tableau1=donnees_brutes_candidat_finales(name_candidat)
    Tableau2=note_candidat(name_candidat)
    n1=np.shape(Tableau1)[0]
    n2=np.shape(Tableau2)[0]
    X1=[]
    Y1=[]
    X2=[]
    Y2=[]
    for x in range(n1):
        X1.append(Tableau1[k][0])
        Y1.append(Tableau1[k][1])
    for x in range(n2):
        X2.append(Tableau2[k][0])
        Y2.append(Tableau2[k][1])
    plt.plot(X1,Y1)
    plt.plot(X2,Y2)
    plt.show()



