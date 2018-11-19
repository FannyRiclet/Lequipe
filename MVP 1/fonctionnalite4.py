def rapport_variable_fonction(dico) :
    """Attribue une note au rapport du nombre de variables sur le nombre de fonctions
    :param dico : dictionnaire issu du la fonction data """
    nb_variable = dico['Nombrevariables']
    nb_fonctions = dico['Nombrefonctions']
    rapport = nb_variable/nb_fonctions
    if rapport in range(2,5) :
        return(10)
    elif rapport == 1 or rapport == 5 :
        return(8)
    else :
        return(0)

