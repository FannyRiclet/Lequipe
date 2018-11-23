#Comparaison des programmes des candidats en comparant les noms des fonctions et ds variables

def noms_fonctions(filepath):
    """Extrait les noms de fonctions d'un programme ruby
    :param filepath : lien du programme ruby
    :return (list of str) liste des noms de fonctions"""
    with open(filepath,'r') as file :
        lines=file.readlines()
        liste_noms=[]
        for line in lines :
            if " def " in line :
                position=line.find("def")
                i=position+4 #indice qui parcourt la ligne, commence apres le def
                nom_fct = ""
                while i<(len(line)-1) and line[i]!='(': # len(line)-1 sinon ca compte le retour a la ligne dans le cas sans parentheses
                    if line[i]!=' ':
                        nom_fct += line[i]
                    i+=1
                liste_noms.append(nom_fct)
    return(liste_noms)

def inverse_char(char) :
    """Inverse une chaine de caractere
    :param char : chaine de caractere a inverser
    :return chaine de caractere inversee"""
    char_inverse = ""
    for i in range(len(char) -1, -1, -1) :
        char_inverse += char[i]
    return(char_inverse)

def noms_variables(filepath):
    """Extraits les noms des variables d'un programme ruby
    :param filepath : lien du programme ruby
    :return (list of str) : liste des noms de variables"""
    with open(filepath,'r') as file :
        lines=file.readlines()
        liste_noms=[]
        for line in lines :
            if " def " in line : #compte variables définies comme variables d'une fonction
                if "(" and ")" in line : #si au moins une variable est définie dans la fonction
                    start = line.find("(") + 1
                    end = line.find(")")
                    nom_var = ""
                    for i in range(start,end) :
                        if line[i] == "," :
                            liste_noms.append(nom_var)
                            nom_var = ""
                        elif line[i] != " " :
                            nom_var += line[i]
            if " = " in line and "where" not in line :
                position = line.find(" = ")
                i = position-1 #indice qui parcourt la ligne, commence deux indices avant le ' = '
                nom_var = ""
                while i>=0 and line[i]!=' ':
                    nom_var += line[i]
                    i-=1 #on rebrousse chemin
                liste_noms.append(inverse_char(nom_var))
    return(liste_noms)


def ordre_alphabetique() :
    """Renvoie un dictionnaire définissant l'ordre alphabetique"""
    alphabet = "abcdefghijklmnopqrstuvwxyz.?_:@=[](), "
    dico_alphabet = {}
    for i in range(0,len(alphabet)) :
        dico_alphabet[alphabet[i]] = i
    return(dico_alphabet)

def plus_petit(ch1,ch2) :
    """Compare deux chaines de caractere
    :param : 2 chaines de caractere (str)
    :return : True si ch1 <= ch2 selon l'ordre alphabetique, False sinon"""
    dico = ordre_alphabetique()
    l1,l2 = len(ch1),len(ch2)
    ch1 = ch1.lower()
    ch2 = ch2.lower()
    for i in range(0,min(l1,l2)) :
        if dico[ch1[i]] != dico[ch2[i]] :
            return(dico[ch1[i]] < dico[ch2[i]])
    if l1 <= l2 :
        return(True)
    else :
        return(False)

def compare_listes_ordonnees(L1,L2) :
    """Compare 2 listes ordonnees
    :param : (list of str) listes ordonnées par ordre croissant
    :return : proportion de chaine de caracteres de L1 présentes dans L2"""
    p = 0
    j = 0
    if len(L1) == 0 :
        return(0)
    for i in range(0,len(L2)) :
        while j < len(L1) and plus_petit(L1[j],L2[i]) :
            if L1[j] == L2[i] :
                p += 1
            j += 1
    return(p/len(L1))


def compare_noms(filepath1,filepathtest1,filepath2,filepathtest2) :
    """Compare les noms des fonctions et variables
    :param : liens des différents programmes ruby pour 2 candidats différents
    :return : pourcentage de ressemblance pour : nom des fonctions, noms des variables, noms des fonctions dans les test, noms des variables dans les tests, moyenne"""
    list_noms_fct1 = sorted(noms_fonctions(filepath1))
    list_noms_var1 = sorted(noms_variables(filepath1))
    list_noms_fct2 = sorted(noms_fonctions(filepath2))
    list_noms_var2 = sorted(noms_variables(filepath2))
    list_noms_fct_test1 = sorted(noms_fonctions(filepathtest1))
    list_noms_var_test1 = sorted(noms_variables(filepathtest1))
    list_noms_fct_test2 = sorted(noms_fonctions(filepathtest2))
    list_noms_var_test2 = sorted(noms_variables(filepathtest2))

    p_fct = compare_listes_ordonnees(list_noms_fct1,list_noms_fct2)
    p_var = compare_listes_ordonnees(list_noms_var1,list_noms_var2)
    p_fct_test = compare_listes_ordonnees(list_noms_fct_test1,list_noms_fct_test2)
    p_var_test = compare_listes_ordonnees(list_noms_var_test1,list_noms_var_test2)

    return(p_fct,p_var,p_fct_test,p_var_test, (p_fct + p_var + p_fct_test + p_var_test)/4)

