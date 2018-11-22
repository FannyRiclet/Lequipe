import pytest

from Fonctionnalite2_2_1 import *
from Fonctionnalite2_2_2 import *
from Fonctionnalite2_2_3 import *
from Fonctionnalite2_2_4 import *
from Fonctionnalite2_2_5 import *
def les_filepath(Nom_dev,Nom_Candidat): #nom du developpeur et Nom_Candidat chaines de caractères
    return(['C:/Users/{}/PycharmProjects/Lequipe/Event{}.rb'.format(Nom_dev,Nom_Candidat),'C:/Users/{}/PycharmProjects/Lequipe/Event{}Test.rb'.format(Nom_dev,Nom_Candidat)])

def test_longueur_nom_fonctions(Nom_dev,Nom_Candidat):
    """teste la fonction longueur_nom_fonctions
    :param: le nom du développeur et le nom du candidat dont on analyse le code"""
    assert longueur_nom_fonctions(les_filepath(Nom_dev,Nom_Candidat)[0]) == [[8,12,19,40,48,42,48,46,20],21]

def test_longueur_nom_variables(Nom_dev,Nom_Candidat):
    """teste la fonction longueur_nom_varaiables
    :param: le nom du développeur et le nom du candidat dont on analyse le code"""
    assert longueur_nom_variables(les_filepath(Nom_dev,Nom_Candidat)[0]) ==  [[15, 4, 10, 8, 14, 8, 12, 5], 0.76]

def test_count_imbrication(Nom_dev,Nom_Candidat):
    """teste la fonction count_imbrication
    :param: le nom du développeur et le nom du candidat dont on analyse le code"""
    assert count_imbrications(les_filepath(Nom_dev,Nom_Candidat)[0]) == 0.5

def test_nombre_duplications(Nom_dev,Nom_Candidat):
     """teste la fonction count_duplications
     :param: le nom du développeur et le nom du candidat dont on analyse le code"""
     assert count_duplications(les_filepath(Nom_dev,Nom_Candidat)[0]) == 0

def test_singulier():
    """teste la fonction singulier"""
    assert singulier('weathers')== 'weather'

def test_proportion_True():
    """teste la fonction proportion_True"""
    assert proportion_True( ['True','False','False','True']) == 0.5


def test_fonctions_comprehensibles(Nom_dev,Nom_Candidat):
    """teste la fonction fonctions_comprehensibles
    :param: le nom du développeur et le nom du candidat dont on analyse le code"""
    assert type(fonctions_comprehensibles(les_filepath(Nom_dev,Nom_Candidat)[0])) == float


def test_variables_comprehensibles(Nom_dev,Nom_Candidat):
    """teste la fonction varaibles_comprehensibles
    :param: le nom du développeur et le nom du candidat dont on analyse le code"""
    assert type(variables_comprehensibles(les_filepath(Nom_dev,Nom_Candidat)[0])) == float

