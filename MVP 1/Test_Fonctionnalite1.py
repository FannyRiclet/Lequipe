import pytest

def les_filepath(Nom_dev,Nom_Candidat): #nom du developpeur et Nom_Candidat chaines de caractères
    return(['C:/Users/{}/PycharmProjects/Lequipe/Event{}.rb'.format(Nom_dev,Nom_Candidat),'C:/Users/{}/PycharmProjects/Lequipe/Event{}Test.rb'.format(Nom_dev,Nom_Candidat)])

sys.path.append('../MVP 1')

from Fonctionnalite1_2_2 import *
from Fonctionnalite1_2_3 import *
from Fonctionnalite1_2_4 import *
from Fonctionnalite1_2_5 import *


def test_count_functions(Nom_dev) :
    """test la fonction count_functions
    :param emplacement_projet : lien pour accéder au projet Lequipe (ex : C:/Users/Kumquat/Document/ ou C:/Users/Gros/PycharmProjects/)"""
    assert count_functions(les_filepath(Nom_dev,"CandidatA")[0]) == 10

def test_count_tests(Nom_dev) :
    assert count_tests(les_filepath(Nom_dev,"CandidatA")[1]) == 13

def test_commentaires(Nom_dev) :
    assert commentaires(les_filepath(Nom_dev,"CandidatB")[0]) == 21

def test_count_variables(Nom_dev) :
    assert count_variables(les_filepath(Nom_dev,"CandidatA")[0]) == 10

def test_function_size(Nom_dev) :
    assert function_size(les_filepath(Nom_dev,"CandidatB")[0]) == ([13,6,9,12,8,8,8], 13, 64/7)
    

from Resultat_candidats import *

def test_data(Nom_dev,Nom_Candidat) :
    assert data(les_filepath(Nom_dev,Nom_Candidat)) != {}

def test_note_candidat(Nom_dev,Nom_Candidat) :
    assert not note_candidat(les_filepath(Nom_dev,Nom_Candidat)).empty

def test_donnees_brutes_candidat(Nom_dev,Nom_Candidat) :
    assert not donnees_brutes_candidat(les_filepath(Nom_dev,Nom_Candidat)).empty


from Fonctionnalite1_4 import *

def test_note_functions(Nom_dev,Nom_Candidat) :
    assert note_functions(data(les_filepath(Nom_dev,Nom_Candidat)),filepath) <= 10

def test_note_rapport_tests_fonctions(Nom_dev,Nom_Candidat) :
    assert 0 <= note_rapport_tests_fonctions(data(les_filepath(Nom_dev,Nom_Candidat)),filepath) <= 10

def test_note_rapport_comm_ligne(Nom_dev,Nom_Candidat) :
    assert 0 <= note_rapport_comm_ligne(data(les_filepath(Nom_dev,Nom_Candidat)),filepath) <= 10

def test_rapport_variable_fonction(Nom_dev,Nom_Candidat) :
    assert 0 <= rapport_variable_fonction(data(les_filepath(Nom_dev,Nom_Candidat)),filepath) <= 10
