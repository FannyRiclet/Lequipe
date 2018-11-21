def count_functions(filepath) :
    """Compte le nombre de fonctions utilisées dans un fichier ruby
    :param filepath : fichier ruby à analyser
    :return count : nombre de fonctions du fichier"""
    with open(filepath,'r') as file :
        lines=file.readlines()
        count=0
        for line in lines :
            if "def" in line :
                count+=1
    return(count)

<<<<<<< HEAD
=======

>>>>>>> e048416b02694cf37d94b81caf76c3b0f396cafb
