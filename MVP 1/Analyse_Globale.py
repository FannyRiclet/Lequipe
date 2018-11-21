import *

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
    print(dict)
    return(dict)



data('/Users/marinewigniolle/PycharmProjects/Codingweek_semaine2/Lequipe/EventCandidatA.rb')


