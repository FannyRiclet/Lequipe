import pytest
from comparaison_blocs import *

def les_filepath(Nom_dev,Nom_Candidat): #nom du developpeur et Nom_Candidat chaines de caractères
    return(['C:/Users/{}/PycharmProjects/Lequipe/Event{}.rb'.format(Nom_dev,Nom_Candidat),'C:/Users/{}/PycharmProjects/Lequipe/Event{}Test.rb'.format(Nom_dev,Nom_Candidat)])

def test_extraction_blocs(Nom_dev):
    """teste la fonction extraction_blocs
    :param: le développeur """
    assert extraction_blocs(les_filepath(Nom_dev,CandidatA)[0]) != []

def test_compare_2_blocs:
    """teste la fonction extraction_blocs"""
    assert compare_2_blocs('doctolib',"doctolig") == False

def test_compare_1_a_2(Nom_dev):
    """teste la fonction compare_1_a_2"""
    assert compare_1_a_2(les_filepath(Nom_dev,CandidatA)[0],les_filepath(Nom_dev,CandidatB)[0]) == False

def test_compare_candidats_1_a_2(Nom_dev):
    """teste la fonction compare_candidats_1_a_2"""
    assert compare_candidats_1_a_2(les_filepath(Nom_dev,CandidatA)[0],les_filepath(Nom_dev,CandidatB)[0],les_filepath(Nom_dev,CandidatA)[1],les_filepath(Nom_dev,CandidatB)[1]) == (0.0, 0.14285714285714285)

