from Fonctionnalite2_1 import *
from Fonctionnalite2_2 import *
from Fonctionnalite2_3 import *
from Fonctionnalite2_4 import *
from Fonctionnalite2_5 import *



def data(filepath):
    """Renvoie les données brutes des critères pour analyser un fichier Ruby d'un candidat
    :param filepath : fichier ruby à analyser
    :return dict : dictionnaire contenant le critère et sa valeur"""
    dict={}
    dict['Nombrefonctions']=count_functions(filepath)
    dict['Nombretests']=count_tests(filepath)
    dict['Nombrecommentaires']=commentaires(filepath)
    dict['Nombrevariables']=count_variables(filepath)
    dict['Taillefonctions']=function_size(filepath)
    dict['Nombrelignes']=num_lines
    return dict

data('C:/Users/Gros/PycharmProjects/Lequipe/EventCandidatA.rb')



with open(filepath, 'r') as f:
    lines = f.readlines()
    num_lines = len([l for l in lines if l.strip(' \n') != ''])
