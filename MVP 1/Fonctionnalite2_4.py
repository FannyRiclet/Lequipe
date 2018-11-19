def count_variables(filepath) :
    """Compte le nombre de variables utilisées dans un fichier ruby
    :param filepath : fichier ruby à analyser
    :return count : nombre de variables du fichier"""
    with open(filepath,'r') as file :
        lines=file.readlines()
        count=0 #compteur de variables
        for line in lines :
            if "def" in line : #compte variables définies comme variables d'une fonction
                if "(" and ")" in line : #si au moins une variable est définie dans la fonction
                    count +=1
                    for char in line :
                        if char == "," :
                            count +=1
            elif " = " in line : #compte les autres variables
                count+=1
    return(count)

