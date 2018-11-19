def function_size(filepath) :
    """
    Fonction qui retourne le nombre de lignes de chaque fonction ainsi que le nombre de lignes de la plus grande
    fonction du programme et la moyenne de la taille des fonctions
    :param filepath: Adresse du fichier Ruby que le candidat a envoyé
    :return: liste où chaque élement représente le nombre de lignes d'une fonction et le nombres de lignes de la plus
    grande fonction et la moyenne de la taille des fonctions
    """
    with open(filepath,'r') as file :
        lines=file.readlines()
        fct_size=[]
        for k in range(0,len(lines)) :
            if "def" in lines[k] :
                count=1
                i=k+1
                while "def" not in lines[i] and i < len(lines)-1 :
                    count+=1
                    i+=1
                fct_size.append(count)
        L=[fct_size,max(fct_size),sum(fct_size)/len(fct_size)]
        return L




