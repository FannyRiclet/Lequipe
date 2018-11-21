from Fonctionnalite2_1 import *
from Fonctionnalite2_2 import *
from Fonctionnalite2_3 import *
from Fonctionnalite2_4 import *
from Fonctionnalite2_5 import *

<<<<<<< HEAD
def data(filepath):
=======


def data(filepath,filepathtest):
>>>>>>> brancheClara
    """Renvoie les données brutes des critères pour analyser un fichier Ruby d'un candidat
    :param filepath : fichier ruby à analyser
    :return dict : dictionnaire contenant le critère et sa valeur"""
    dict={}
    dict['Nombre fonctions']=count_functions(filepath)
    dict['Nombre tests']=count_tests(filepathtest)
    dict['Nombre commentaires']=commentaires(filepath)
    dict['Nombre variables']=count_variables(filepath)
    dict['Taille fonctions']=function_size(filepath)
    return(dict)


<<<<<<< HEAD

data(r'C:/Users/Camille/PycharmProjects/Lequipe/Initialisation/EventCandidatA.rb')

=======
data('C:/Users/Gros/PycharmProjects/Lequipe/EventCandidatA.rb','C:/Users/Gros/PycharmProjects/Lequipe/EventCandidatATest.rb')
>>>>>>> brancheClara


