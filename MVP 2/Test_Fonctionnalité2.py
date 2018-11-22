import pytest

from Fonctionnalite2_2_1 import *
from Fonctionnalite2_2_2 import *
from Fonctionnalite2_2_3 import *
from Fonctionnalite2_2_4 import *
from Fonctionnalite2_2_5 import *

def test_longueur_nom_fonctions(emplacement_projet):
    """teste la fonction longueur_nom_fonctions
    :param: l'emplacement du projet pour completer le filepath"""
    assert longueur_nom_fonctions(emplacement_projet + "Lequipe\EventCandidatA.rb") == [[8,12,19,40,48,42,48,46,20],21]

def test_longueur_nom_variables(emplacement_projet):
    """teste la fonction longueur_nom_varaiables
    :param: l'emplacement du projet pour completer le filepath"""
    assert longueur_nom_variables(emplacement_projet + "Lequipe\EventCandidatA.rb") ==  [[15, 4, 10, 8, 14, 8, 12, 5], 0.76]

def test_count_imbrication(emplacement_projet):
    """teste la fonction count_imbrication
    :param: l'emplacement du projet pour completer le filepath"""
    assert count_imbrications(emplacement_projet + "Lequipe/EventCandidatA.rb") == 0.5

def test_nombre_duplications(emplacement_projet):
     """teste la fonction count_duplications
     :param: l'emplacement du projet pour completer le filepath"""
     assert count_duplications(emplacement_projet + "Lequipe/EventCandidatA.rb") == 0

def test_singulier(emplacement_projet):
    """teste la fonction singulier
    :param: l'emplacement du projet pour completer le filepath"""
    assert singulier('weathers')== 'weather'

def





