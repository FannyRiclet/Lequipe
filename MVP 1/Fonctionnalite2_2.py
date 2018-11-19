def count_tests(filepath) :
    """Compte le nombre de tests utilisés dans un fichier ruby
    :param filepath : fichier ruby à analyser
    :return count : nombre de tests du fichier"""
    with open(filepath,'r') as file :
        lines = file.readlines()
        count=0
        for line in lines :
            if "test" in line :
                count += 1
    return(count)

filepath = 'C:\Utilisateurs\Camille\PycharmProjects\Lequipe\Lequipe\Initialisation\EventCandidatATest.rb'
