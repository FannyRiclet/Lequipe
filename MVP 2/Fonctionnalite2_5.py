import nltk
nltk.download() #choisir words dans Corpora
from nltk.corpus import words
word_list = words.words()

alphabet = 'abcdefghijklmnopqrstuvwxyz'


#Car tous les pluriels ne sont pas dans word_list
def singulier(mot) :
    """Met un mot au singulier s'il est au pluriel
    :param mot : mot à mettre au singulier
    :return mot_singulier : mot au singulier"""
    if mot[len(mot) - 1] == 's' :
        mot_singulier = ""
        if mot[len(mot) - 2] == 'e' :
            if mot[len(mot) - 3] == 'i' :#mots finissant par "ies"
                for k in range(0, len(mot) - 3) :
                    mot_singulier += mot[k]
                mot_singulier += "y"
            else :#mots finissant par "es"
                for k in range(0, len(mot) - 2) :
                    mot_singulier += mot[k]
        else :#mots finissant par "s"
            for k in range(0,len(mot)-1) :
            mot_singulier += mot[k]
    else :
        mot_singulier = mot
    return(mot_singulier)


def name_in_english(variable) :
    """Vérifier qu'une varibale est bien constituée de mots en anglais
    :param variable : nom de la variable à tester
    :return booléen indiquant si ce nom est en anglais ou non"""
    pos = 0
    while pos < len(variable) :
        mot = ""
        while pos < len(variable) and variable[pos] in alphabet :
            mot += variable[pos]
            pos += 1
        if mot != "" and mot not in word_list and singulier(mot) not in word_list:
            return(False)
        pos += 1
    return(True)


def proportion_True(liste) :
    """retourne la proportion d'élements True dans la liste
    :param liste : (list) liste de booléens à tester
    :return proportion d'élements True"""
    p = 0
    for bool in liste :
        if bool :
            p += 1
    return(p/len(liste))


def variables_comprehensibles(filepath) :
    """Vérifie que les noms des variables utilisées dans le programme utilisent des mots anglais
    :param filepath : lien du programme à tester
    :return proportion de variables correctes"""
    with open(filepath,'r') as file :
        lines=file.readlines()
        words_in_english=[]
        for line in lines :
            if "def" in line : #considère les variables définies comme variables d'une fonction
                if "(" and ")" in line : #si au moins une variable est définie dans la fonction
                    pos = line.find("(") + 1 #position de la première variable
                    while pos < len(line) :
                        nom_var = ""
                        while pos < len(line) and line[pos] not in [")",",", "="] : #extraction du nom complet de la variable :
                            nom_var += line[pos]
                            pos += 1
                        if pos < len(line) and line[pos] == "=" : #cas où une variable est définie comme égale à quelque chose
                            while pos < len(line) and line[pos] not in [",",")"] :
                                pos += 1
                        pos += 1
                        if not nom_var == "\n" :
                            words_in_english.append(name_in_english(nom_var))
            elif " = " in line and "where" not in line: #considère les autres variables
                pos = 0
                nom_var = ''
                while pos < len(line) and line[pos] != "=" :
                    nom_var += line[pos]
                    pos +=1
                if not nom_var == "\n" :
                    words_in_english.append(name_in_english(nom_var))
        return(proportion_True(words_in_english))


