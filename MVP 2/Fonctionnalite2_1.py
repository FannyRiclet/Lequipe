#nom des fonctions

def longueur_nom_fonctions(filepath):
    with open(filepath,'r') as file :
        lines=file.readlines()
        for line in lines :
            if "def" in line :
                position=line.find("def")
                count=0 #compte le nb de caracteres d'un nom de fonction
                i=position+4 #indice qui parcourt la ligne, commence apres le def
                while i<(len(line)-1) and line[i]!='(': # len(line)-1 sinon ca compte le retour a la ligne dans le cas sans parentheses
                    if line[i]!=' ':
                        count+=1
                    i+=1
                print(count)

filepath='C:/Users/Arnaud et Lydie/Desktop/Lison/CS/SIP/Coding_weeks/Doctolib/Lequipe/EventCandidatA.rb'

'''
TEST
8
12
19
40
48
42
48
46
20
21
None'''
