import sys
import numpy as np

def les_filepath(filepath,Nom_Candidat): #filepath et Nom_Candidat chaines de caractères
    return ('{}/Event{}.rb'.format(filepath,Nom_Candidat),'{}/Event{}Test.rb'.format(filepath,Nom_Candidat))

sys.path.append('../MVP 1')
from Resultat_candidats import *
from Fonctionnalite1_2_1 import *
from Fonctionnalite1_2_2 import *
from Fonctionnalite1_2_3 import *
from Fonctionnalite1_2_4 import *
from Fonctionnalite1_2_5 import *
from Fonctionnalite1_4 import *


#sys.path.remove('../MVP 1')

sys.path.append('../MVP 2')
from Resultat_candidats_2 import *
from Fonctionnalite2_2_1 import *
from Fonctionnalite2_2_2 import *
from Fonctionnalite2_2_3 import *
from Fonctionnalite2_2_4 import *
from Fonctionnalite2_2_5 import *

def data_finale(filepath,filepathtest) :
    dict={}
    dict['Nombre fonctions']=count_functions(filepath)
    dict['Nombre tests']=count_tests(filepathtest)
    dict['Nombre commentaires']=commentaires(filepath)
    dict['Nombre variables']=count_variables(filepath)
    dict['Taille fonctions']=function_size(filepath)
    dict['Longueur nom fonction']=longueur_nom_fonctions(filepath)
    dict['Longueur nom variable']=longueur_nom_variables(filepath)
    dict['Nombre imbrications']= count_imbrication(filepath)
    dict['Nombre duplications']=nombre_duplications(filepath)
    dict['Nom fonction pertinent']= fonctions_comprehensibles(filepath)
    dict['Nom variable pertinent']= variables_comprehensibles(filepath)
    return(dict)


def donnees_brutes_candidat_finales(name_candidat) :
    filepath,filepathtest=file_candidate(name_candidat)
    donnees_brutes=data_finale(filepath,filepathtest)
    print(donnees_brutes)
    print(donnees_brutes['Longueur nom fonction'])
    print(type(donnees_brutes['Longueur nom fonction'][1]))
    table=np.array([['name_candidat','Donnees brutes'],
                ['Nombre fonctions',donnees_brutes['Nombre fonctions']],
                ['Nombre tests',donnees_brutes['Nombre tests']],
                ['Nombre commentaires',donnees_brutes['Nombre commentaires']],
                ['Nombre variables', donnees_brutes['Nombre variables']],
                ['Taille fonction moyenne', donnees_brutes['Taille fonctions'][2]],
                ['Longueur nom fonction',donnees_brutes['Longueur nom fonction'][1]],
                ['Longueur nom variable',donnees_brutes['Longueur nom variable'][1]],
                ['Nombre imbrications', donnees_brutes['Nombre imbrications']],
                ['Nombre duplications', donnees_brutes['Nombre duplications']],
                ['Pertinence nom fonction', donnees_brutes['Nom fonction pertinent']],
                ['Pertinence nom variable', donnees_brutes['Nom variable pertinent']]
                    ])
    pd.table = pd.DataFrame(data=table[1:,1:], index=table[1:,0], columns=table[0,1:])
    print(pd.table)
    return(pd.table)
