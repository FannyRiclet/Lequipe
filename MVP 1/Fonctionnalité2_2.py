def count_tests(filepath) :
    with open(filepath,'r') as file :
        lines = file.readlines()
        count=0
        for line in lines :
            if "test" in line :
                count += 1
    print("Le code contient {} tests".format(count))

filepath = 'C:\Utilisateurs\Camille\PycharmProjects\Lequipe\Lequipe\Initialisation\EventCandidatATest.rb'
