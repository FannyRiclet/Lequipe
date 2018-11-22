import pytest

from Fonctionnalite1_2_1 import *
from Fonctionnalite1_2_2 import *
from Fonctionnalite1_2_3 import *
from Fonctionnalite1_2_4 import *
from Fonctionnalite1_2_5 import *


def test_count_functions(emplacement_projet) :
    """test la fonction count_functions
    :param emplacement_projet : lien pour accéder au projet Lequipe (ex : C:/Users/Kumquat/Document/ ou C:/Users/Gros/PycharmProjects/)"""
    assert count_functions(emplacement_projet + "Lequipe\EventCandidatA.rb") == 10

def test_count_tests(emplacement_projet) :
    assert count_tests(emplacement_projet + "Lequipe\EventCandidatATest.rb") == 13

def test_commentaires(emplacement_projet) :
    assert commentaires(emplacement_projet + "Lequipe\EventCandidatB.rb") == 21

def test_count_variables(emplacement_projet) :
    assert count_variables(emplacement_projet + "Lequipe\EventCandidatA.rb") == 10

def test_function_size(emplacement_projet) :
    assert function_size(emplacement_projet + "Lequipe\EventCandidatB.rb") == ([13,6,9,12,8,8,8], 13, 64/7)
    

from Resultat_candidats import *

def test_data(emplacement_projet) :
    assert data(emplacement_projet + "Lequipe\EventCandidatB.rb", emplacement_projet + "Lequipe\EventCandidatBTest.rb") != {}

def test_note_candidat(emplacement_projet) :
    assert not note_candidat(emplacement_projet + "Lequipe\EventCandidatB.rb", emplacement_projet + "Lequipe\EventCandidatBTest.rb").empty

def test_donnees_brutes_candidat(emplacement_projet) :
    assert not donnees_brutes_candidat(emplacement_projet + "Lequipe\EventCandidatB.rb", emplacement_projet + "Lequipe\EventCandidatBTest.rb").empty


from Fonctionnalite1_4 import *

def test_note_functions(emplacement_projet) :
    filepath,filepathtest = emplacement_projet + "Lequipe\EventCandidatA.rb", emplacement_projet + "Lequipe\EventCandidatATest.rb"
    assert note_functions(data(filepath,filepathtest),filepath) <= 10

def test_note_rapport_tests_fonctions(emplacement_projet) :
    filepath,filepathtest = emplacement_projet + "Lequipe\EventCandidatA.rb", emplacement_projet + "Lequipe\EventCandidatATest.rb"
    assert 0 <= note_rapport_tests_fonctions(data(filepath,filepathtest),filepath) <= 10

def test_note_rapport_comm_ligne(emplacement_projet) :
    filepath,filepathtest = emplacement_projet + "Lequipe\EventCandidatA.rb", emplacement_projet + "Lequipe\EventCandidatATest.rb"
    assert 0 <= note_rapport_comm_ligne(data(filepath,filepathtest),filepath) <= 10

def test_rapport_variable_fonction(emplacement_projet) :
    filepath,filepathtest = emplacement_projet + "Lequipe\EventCandidatA.rb", emplacement_projet + "Lequipe\EventCandidatATest.rb"
    assert 0 <= rapport_variable_fonction(data(filepath,filepathtest),filepath) <= 10
