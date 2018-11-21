def data_finale(filepath,filepathtest) :
    dict={}
    dict['Nombre fonctions']=count_functions(filepath)
    dict['Nombre tests']=count_tests(filepathtest)
    dict['Nombre commentaires']=commentaires(filepath)
    dict['Nombre variables']=count_variables(filepath)
    dict['Taille fonctions']=function_size(filepath)

