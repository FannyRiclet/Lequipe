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

filepath = r'C:\Users\Camille\PycharmProjects\Lequipe\Lequipe\EventCandidatATest.rb'
print(count_tests (filepath))
