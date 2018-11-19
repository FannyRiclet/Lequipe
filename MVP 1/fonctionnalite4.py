def note_rapport_tests_fonctions(nb_tests,nb_fonctions):
    rapport = nb_tests/nb_fonctions
    if rapport > 1:
        return 10
    else:
        return rapport*10
    
