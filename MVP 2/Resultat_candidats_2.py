import pandas as pd
from Fonctionnalite2_2_1 import *
from Fonctionnalite2_2_2 import *
from Fonctionnalite2_2_3 import *
from Fonctionnalite2_2_4 import *
from Fonctionnalite2_2_5 import *

def les_filepath(Nom_dev,Nom_Candidat):
    """Renvoie les liens pour accéder aux programmes d'un candidat
    :param Nom_dev : nom du développeur
    :param Nom_Candidat : nom du Candidat (ex : CandidatA)
    :return (tuple of str) lien du programme du candidat, lien du programme test du candidat"""
    return(['C:/Users/{}/PycharmProjects/Lequipe/Event{}.rb'.format(Nom_dev,Nom_Candidat),'C:/Users/{}/PycharmProjects/Lequipe/Event{}Test.rb'.format(Nom_dev,Nom_Candidat)])

def data2(filepath,filepathtest):
    """Renvoie les donnees brutes des critères pour analyser un fichier Ruby d'un candidat
    :param filepath : fichier ruby à analyser
    :return dict : dictionnaire contenant le critere et sa valeur"""
    dict={}
    dict['Longueur nom fonction']=longueur_nom_fonctions(filepath)[1]
    dict['Longueur nom variable']=longueur_nom_variables(filepath)[1]
    dict['Nombre imbrications']= count_imbrication(filepath)
    dict['Nombre duplications']=nombre_duplications(filepath)
    dict['Nom fonction pertinent']= fonctions_comprehensibles(filepath)
    dict['Nom variable pertinent']= variables_comprehensibles(filepath)
    return(dict)

def donnees_brutes_candidat2(Nom_dev,Nom_Candidat) :
    """Renvoie les donnees brutes des critères pour analyser un fichier Ruby d'un candidat
    :param Nom_dev : nom du développeur
    :param Nom_Candidat : nom du Candidat (ex : CandidatA)
    :return df : tableau panda contenant le critere et sa valeur"""
    filepath,filepathtest=les_filepath(Nom_dev,Nom_Candidat)[0],les_filepath(Nom_dev,Nom_Candidat)[1]
    donnees_brutes=data2(filepath,filepathtest)
    df = pd.DataFrame(donnees_brutes, index=[Nom_Candidat])
    print(df)
    return(df)
