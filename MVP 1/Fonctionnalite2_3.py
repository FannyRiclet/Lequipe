def commentaires(file):
    """Compte le nombre de commentaires utilisés dans un fichier ruby
    :param filepath : fichier ruby à analyser
    :return count : nombre de commentaires du fichier"""
    with open(file,'r') as file :
        lines=file.readlines()
        i=0
        nombre=0
        while i<len(lines):
            if lines[i][0]=='#':
                nombre+=1
            i+=1
    return nombre

print(commentaires('C:/Users/Gros/PycharmProjects/Lequipe/EventCandidatA.rb'))
