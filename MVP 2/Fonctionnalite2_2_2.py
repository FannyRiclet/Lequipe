#nom des variables

def longueur_nom_variables(filepath):
    with open(filepath,'r') as file :
        lines=file.readlines()
        liste_longueurs=[]
        for line in lines :
            if " def " in line : #compte variables définies comme variables d'une fonction
                if "(" and ")" in line : #si au moins une variable est définie dans la fonction
                    count +=1
                    for char in line :
                        if char == "," :
                            count +=1
            if " = " in line and "where" not in line :
                position=line.find(" = ")
                count=0 #compte le nb de caracteres d'un nom de variable
                i=position-1 #indice qui parcourt la ligne, commence deux indices avant le ' = '
                while i>=0 and line[i]!=' ':
                    count+=1
                    i-=1 #on rebrousse chemin
                liste_longueurs.append(count)
    return([liste_longueurs, sum(liste_longueurs)/100])


