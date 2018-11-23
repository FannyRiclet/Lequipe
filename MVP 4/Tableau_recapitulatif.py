import sys
import numpy as np

def les_filepath(Nom_dev,Nom_Candidat):
    """Renvoie les liens pour accéder aux programmes d'un candidat
    :param Nom_dev : nom du développeur
    :param Nom_Candidat : nom du Candidat (ex : CandidatA)
    :return (tuple of str) lien du programme du candidat, lien du programme test du candidat"""
    return(['C:/Users/{}/PycharmProjects/Lequipe/Event{}.rb'.format(Nom_dev,Nom_Candidat),'C:/Users/{}/PycharmProjects/Lequipe/Event{}Test.rb'.format(Nom_dev,Nom_Candidat)])

sys.path.append('../MVP 1')
from Resultat_candidats import *
from Fonctionnalite1_2_1 import *
from Fonctionnalite1_2_2 import *
from Fonctionnalite1_2_3 import *
from Fonctionnalite1_2_4 import *
from Fonctionnalite1_2_5 import *
from Fonctionnalite1_4 import *


sys.path.append('../MVP 2')
from Resultat_candidats_2 import *
from Fonctionnalite2_2_1 import *
from Fonctionnalite2_2_2 import *
from Fonctionnalite2_2_3 import *
from Fonctionnalite2_2_4 import *
from Fonctionnalite2_2_5 import *

def data_finale(filepath,filepathtest) :
    """Renvoie les données des critères (de MVP1 et MVP2) pour analyser un fichier Ruby d'un candidat dans un dictionnaire
    :param filepath,filepathtest : fichiers ruby à analyser
    :return dict : dictionnaire contenant les critère et leur valeur"""
    donnees_brutes=data(filepath,filepathtest)
    dict={}
    dict['Nombre fonctions']=count_functions(filepath)
    dict['Nombre tests']=count_tests(filepathtest)
    dict['Nombre commentaires']=commentaires(filepath)
    dict['Nombre variables']=count_variables(filepath)
    dict['Taille fonctions']=function_size(filepath)[2]
    dict['Longueur nom fonction']=longueur_nom_fonctions(filepath)[1]
    dict['Longueur nom variable']=longueur_nom_variables(filepath)[1]
    dict['Nombre imbrications']= count_imbrication(filepath)
    dict['Nombre duplications']=nombre_duplications(filepath)
    dict['Nom fonction pertinent']= fonctions_comprehensibles(filepath)
    dict['Nom variable pertinent']= variables_comprehensibles(filepath)
    dict['Note nb fonctions']= note_functions(donnees_brutes,filepath)
    dict['Rapport test/fonction']= note_rapport_tests_fonctions(donnees_brutes)
    dict['Rapport variable/fonction']= rapport_variable_fonction(donnees_brutes)
    dict['Rapport comm/lignes']=note_rapport_comm_ligne(donnees_brutes)
    return(dict)

liste_noms_candidats=['CandidatA','CandidatB','CandidatC']

def donnees_brutes_candidat_finales(Nom_dev,Nom_Candidat) :
    """Renvoie les données des critères (de MVP1et MVP2) pour analyser un fichier Ruby d'un candidat dans un tableau panda
    :param Nom_dev : nom du développeur
    :param Nom_Candidat : nom du Candidat (ex : CandidatA)
    :return df : tableau panda contenant les critère et leur valeur"""
    filepath,filepathtest = les_filepath(Nom_dev,Nom_Candidat)[0] , les_filepath(Nom_dev,Nom_Candidat)[1]
    data=data_finale(filepath,filepathtest)
    df = pd.DataFrame(data, index=[Nom_Candidat])
    return(df)

