def commentaires(file):
    """Compte le nombre de commentaires utilisés dans un fichier ruby
    :param filepath : fichier ruby à analyser
    :return count : nombre de commentaires du fichier"""
    i=0
    l=len(file)
    nombre=0
    while i<l:
        if file[i]=='#':
            nombre+=1
        i+=1
    return nombre

print(commentaires(file))
