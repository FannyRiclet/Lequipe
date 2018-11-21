#nom des variables

def longueur_nom_variables(filepath):
    with open(filepath,'r') as file :
        lines=file.readlines()
        liste_longueurs=[]
        for line in lines :
            if " = " in line :
                position=line.find(" = ")
                count=0 #compte le nb de caracteres d'un nom de variable
                i=position-1 #indice qui parcourt la ligne, commence deux indices avant le ' = '
                while i>=0 and line[i]!=' ':
                    count+=1
                    i-=1 #on rebrousse chemin
                liste_longueurs.append(count)
    return(max(liste_longueurs),min(liste_longueurs))
