from Fonctionnalite1_2_1 import *
from Fonctionnalite1_2_2 import *
from Fonctionnalite1_2_3 import *
from Fonctionnalite1_2_4 import *
from Fonctionnalite1_2_5 import *
from Fonctionnalite1_4 import *
import numpy as np
import pandas as pd

def les_filepath(Nom_dev,Nom_Candidat): #nom du developpeur et Nom_Candidat chaines de caractères
    return(['C:/Users/{}/PycharmProjects/Lequipe/Event{}.rb'.format(Nom_dev,Nom_Candidat),'C:/Users/{}/PycharmProjects/Lequipe/Event{}Test.rb'.format(Nom_dev,Nom_Candidat)])

def data(filepath,filepathtest):
    """Renvoie les données brutes des critères (de MVP1)  pour analyser un fichier Ruby d'un candidat
    :param filepath : fichier ruby à analyser
    :return dict : dictionnaire contenant les critère et leur valeur"""
    dict={}
    dict['Nombre fonctions']=count_functions(filepath)
    dict['Nombre tests']=count_tests(filepathtest)
    dict['Nombre commentaires']=commentaires(filepath)
    dict['Nombre variables']=count_variables(filepath)
    dict['Taille fonctions']=function_size(filepath)[2]
    return(dict)

def dic_note_candidat(filepath,filepathtest) :
    """Renvoie les notes associées aux critères (de MVP1) analyses dans un fichier Ruby d'un candidat
    :param filepath, filepathtest : fichiers ruby à analyser
    :return dico : dictionnaire contenant les critère et leur notes"""
    donnees_brutes=data(filepath,filepathtest)
    dico={}
    dico=['Nombre fonctions'}=note_functions(donnees_brutes,filepath)
    dico=['Rapport test/fonction']= note_rapport_tests_fonctions(donnees_brutes)
    dico=['Rapport variable/fonction']= rapport_variable_fonction(donnees_brutes)
    dico=['Rapport comm/lignes']=note_rapport_comm_ligne(donnees_brutes)
    return dico

def note_candidat(Nom_dev,Nom_Candidat) :
    """Renvoie les notes associées aux critères (de MVP1) analyses dans un fichier Ruby d'un candidat
    :param filepath,filepathtest : fichiers ruby à analyser
    :return df : tableau panda contenant les critères et leur valeur"""
    filepath,filepathtest = les_filepath(Nom_dev,Nom_Candidat)[0] , les_filepath(Nom_dev,Nom_Candidat)[1]
    dico=dic_note_candidat(filepath,filepathtest)
    df=pd.DataFrame(dico, index=[Nom_Candidat])
    print(df)
    return(df)

def donnees_brutes_candidat1(Nom_dev,Nom_Candidat) :
    """Renvoie les données brutes des critères (de MVP1) pour analyser un fichier Ruby d'un candidat dans un tableau panda
    :param filepath,filepathtest : fichiers ruby à analyser
    :return df : tableau panda contenant les critère et leur valeur"""
    filepath,filepathtest=les_filepath(Nom_dev,Nom_Candidat)[0],les_filepath(Nom_dev,Nom_Candidat)[1]
    donnees_brutes=data(filepath,filepathtest)
    df = pd.DataFrame(donnees_brutes, index=[Nom_Candidat])
    print(df)
    return(df)

