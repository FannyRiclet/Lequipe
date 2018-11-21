#nom des variables

def longueur_nom_variables(filepath):
    with open(filepath,'r') as file :
        lines=file.readlines()
        for line in lines :
            if "=" in line :
                position=line.find("=")
                count=0 #compte le nb de caracteres d'un nom de variable
                i=position-2 #indice qui parcourt la ligne, commence deux indices avant le '='
                while i>=0 and line[i]!=' ':
                    count+=1
                    i-=1 #on rebrousse chemin
                print(count)

filepath='C:/Users/Arnaud et Lydie/Desktop/Lison/CS/SIP/Coding_weeks/Doctolib/Lequipe/EventCandidatA.rb'


