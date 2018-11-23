#Comparaison des programmes des candidats en comparants les différents blocs

def ligne_end(chaine,k) :
    """Verifie que le ligne comporte le mot "end" à la bonne position dans une chaine de caractere
    :param chaine : chaine de caractere
    :param k : position du "e" du "end"
    :return booleen indiquant la conformite de la ligne"""
    if len(chaine) < k+2 :
        return(False)
    else :
        return(chaine[k] == 'e' and chaine[k+1] == 'n' and chaine[k+2] == 'd' and chaine[k+3] == "\n")


def extraction_blocs(filepath) :
    """Extrait les blocs separes par des sauts de ligne/ou fonctions du programme ruby
    :param filepath : lien du programme ruby
    :return : liste (list) des differents blocs (liste de chaines de caracteres)"""
    with open(filepath,'r') as file :
        lines=file.readlines()
        list_blocs = []
        k = 1
        while k < len(lines) : #parcours des lignes sans considerer la 1ere (la classe)
            bloc = []

            if " def " in lines[k] : #extraction de la fonction :
                position = lines[k].find("def") #indentation du def
                while not ligne_end(lines[k],position) :
                    bloc.append(lines[k])
                    k += 1

                bloc.append(lines[k])
                k += 2

            else :
                while k < len(lines) and not lines[k] == "\n" :
                    bloc.append(lines[k])
                    k += 1
                k += 1

            list_blocs.append(bloc)
        return(list_blocs)


def compare_2_blocs(bloc1,bloc2) :
    """Comparer 2 blocs
    :param bloc1,bloc2 : (list of str)
    :return : (bool) booléen indiquant si les 2 blocs sont identiques ou non (True si les blocs sont identiques)"""
    l1,l2 = len(bloc1),len(bloc2)
    if l1 != l2 :
        return(False)
    else :
        for k in range(0,l1) :
            long1,long2 = len(bloc1[k]),len(bloc2[k])
            if long1 == long2 :
                pos = 0
                while pos < long1 and bloc1[k][pos] == bloc2[k][pos] :
                    pos += 1
                if pos != long1 :
                    return(False)
            else :
                return(False)
        return(True)


def compare_blocs_1_a_2(filepath1,filepath2) :
    """Comparaison du fichier 1 au fichier 2
    :param filepath1, filepath2 : liens des programmes 1 et 2
    :return : proportion de blocs du fichier 1 que l'on retrouve dans le fichier 2"""
    list_blocs1 = extraction_blocs(filepath1)
    list_blocs2 = extraction_blocs(filepath2)
    compteur_True = 0
    for bloc1 in list_blocs1 :
        for bloc2 in list_blocs2 :
            if compare_2_blocs(bloc1,bloc2) :
                compteur_True += 1
    longueur = len(list_blocs1)
    return(compteur_True/longueur)


def compare_blocs_candidats_1_a_2(filepath1,filepathtest1,filepath2,filepathtest2) :
    """Comparaison du programme du candidat 1 à celui du candidat 2
    :param : liens des fichiers contenant les programmes et programmes tests
    :return : proportion des blocs des fichiers 1 que l'on retrouve dans les fichiers 2 (d'abord programme puis programme test)"""
    prop = compare_1_a_2(filepath1,filepath2)
    prop_test = compare_1_a_2(filepathtest1,filepathtest2)
    return(prop,prop_test)

