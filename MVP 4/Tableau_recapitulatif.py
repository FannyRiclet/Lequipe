import sys
import numpy as np

def les_filepath(Nom_dev,Nom_Candidat): #nom du developpeur et Nom_Candidat chaines de caractères
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

def data_finale(filepath,filpathtest) :
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
    return(dict)

liste_noms_candidats=['CandidatA','CandidatB','CandidatC']

def donnees_brutes_candidat_finales(Nom_dev,Nom_Candidat) :
    filepath,filepathtest = les_filepath(Nom_dev,Nom_Candidat)[0] , les_filepath(Nom_dev,Nom_Candidat)[1]
    data=data_finale(filepath,filepathtest)
    df = pd.DataFrame(data, index=[Nom_Candidat])
    print(df)
    return(df)

def notes_candidat_finales(filepath,filepathtest) :
    notes=data(filepath,filepathtest)
    note=np.array([['','Notes'],
                ['Nombre fonctions',note_functions(donnees_brutes,filepath)],
                ['Rapport test/fonction',note_rapport_tests_fonctions(donnees_brutes)],
                ['Rapport commentaire/ligne',note_rapport_comm_ligne(donnees_brutes)]])
    pd.table=pd.DataFrame(data=table[1:,1:], index=table[1:,0], columns=table[0,1:])
    return(pd.table)
