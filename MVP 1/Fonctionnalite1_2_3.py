def commentaires(file):
    """Compte le nombre de commentaires utilises dans un fichier ruby
    :param filepath : fichier ruby à analyser
    :return count : nombre de commentaires du fichier"""
    with open(file,'r') as file :
        lines=file.readlines()
        i=0
        nombre=0
        while i<len(lines):
            if '#' in lines[i]:
                nombre+=1
            i+=1
    return nombre
