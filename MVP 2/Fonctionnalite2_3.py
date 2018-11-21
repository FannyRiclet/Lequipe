def count_imbrication(filepath):
    """Compte le nombre d'imbrication dans chaque fonction utilisee dans un fichier Ruby
    :param filepath : fichier ruby a analyser
    :return count : liste contenant nombre d'imbrications pour chaque fonction"""
    with open(filepath,'r') as file :
        lines=file.readlines()
        L=[]
        k=0
        while k < len(lines):
            if "def" in lines[k]:
                count=0
                k+=1
                while k < len(lines) and not(""" end\n""" in lines[k]) :
                    if " if " in lines[k] or "while" in lines[k] or "for" in lines[k] or "try" in lines[k]:
                        count+=1
                    k+=1
                L.append(count)
                k+=1
            else:
                k+=1
    return(sum(L)/len(L))


