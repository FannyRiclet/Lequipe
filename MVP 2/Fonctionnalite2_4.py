def nombre_duplications (filepath):
    """Compte le nombre de duplication de code dans un fichier ruby
    :param filepath : fichier ruby à analyser
    :return count : nombre de tests du fichier"""
    with open(filepath,'r') as file :
        lines = file.readlines()
        liste_lignes=[]
        count = 0
        for line in lines:
            if not("end" in line):
                liste_lignes.append(line)
        liste_lignes.sort()           #on trie la liste par odre alphabétique pour que ce soit plus simple à comparer
        for i in range (len(liste_lignes)-1):
            if liste_lignes[i]== liste_lignes[i + 1]:
                count += 1
            # on n'a pas beosin de regarder les lignes suivantes car on parcourt toute la liste:
            #  si 3 lignes sont identiques (i, i+1 et i+2) cela fait 2 duplications:
            #  la fonction va en compter une car l[i] = l[i+1] et un autre car l[i+1]= l[i+2]: on a le bon compte
    return count


nombre_duplications('C:/Users/Gros/PycharmProjects/Lequipe/EventCandidatA.rb')
