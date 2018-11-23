import sys

sys.path.append('../MVP 4')
from Tableau_recapitulatif import *

def les_filepath(Nom_dev,Nom_Candidat): #nom du developpeur et Nom_Candidat chaines de caractères
    return(['C:/Users/{}/PycharmProjects/Lequipe/Event{}.rb'.format(Nom_dev,Nom_Candidat),'C:/Users/{}/PycharmProjects/Lequipe/Event{}Test.rb'.format(Nom_dev,Nom_Candidat)])

def comparaison_deux_candidats(Nom_dev, Nom_Candidat1, Nom_Candidat2) :
    filepath1,filepathtest1=les_filepath(Nom_dev,Nom_Candidat1)[0] , les_filepath(Nom_dev,Nom_Candidat1)[1]
    filepath2, filepathtest2 =les_filepath(Nom_dev,Nom_Candidat2)[0] , les_filepath(Nom_dev,Nom_Candidat2)[1]
    """Compare un fichier  d'un candidats sur les criteres determines en mvp1 et mvp2
    :param filepath1: fichier ruby du candidat1
    :param filepathtest1 : fichier test ruby du candidat1
    :param filepath2: fichier ruby du candidat2
    :param filepathtest2 : fichier test ruby du candidat2
    :return: Un dictionnaire contenant le nom du critere et le taux de ressemblance pour ce critere
    """
    liste_criteres = data_finale(filepath1,filepathtest1).keys()
    dict1=data_finale(filepath1,filepathtest1)
    dict2=data_finale(filepath2, filepathtest2)
    print(dict1['Taille fonctions'])
    dico={}
    for x in liste_criteres :
        if type(dict1[x]) == float or type(dict1[x]) == int :
            if max(dict1[x],dict2[x]) == 0 :
                dico[x]=0
            else :
                dico[x]=min(dict1[x],dict2[x])/max(dict1[x],dict2[x])*100
    return(dico)
