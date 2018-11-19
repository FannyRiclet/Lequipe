#commentaires
with open('C:/Users/Arnaud et Lydie/Desktop/Lison/CS/SIP/Coding_weeks/Doctolib/Lequipe/EventCandidatA.rb','r') as file :
   file=file.read()
   #print(file)

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
