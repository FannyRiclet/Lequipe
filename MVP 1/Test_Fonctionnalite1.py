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
    

