def count_functions(filepath) :
    #ne prend pas en compte les fonctions "scope"
    with open(filepath,'r') as file :
        lines=file.readlines()
        count=0
        print(lines)
        for line in lines :
            if "def" in line :
                count+=1
    print("Le code contient {} fonctions".format(count))

filepath='C:/Users/Gros/PycharmProjects/Lequipe/EventCandidatA.rb'

#count_functions(filepath)
