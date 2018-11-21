from fonctionnalite4 import *
import numpy as np
import pandas as pd

def note_candidat(filepath,filepathtest) :
    donnees_brutes=data(filepath,filepathtest)
    table=np.array([['','Notes'],
                ['Nombre fonctions',note_functions(donnees_brutes,filepath)],
                ['Rapport test/fonction',note_rapport_tests_fonctions(donnees_brutes)],
                ['Rapport commentaire/ligne',note_rapport_comm_ligne(donnees_brutes)]])
    pd.table=pd.DataFrame(data=table[1:,1:], index=table[1:,0], columns=table[0,1:])
    print(pd.table)
    return(pd.table)

def donnees_brutes_candidat(filepath,filepathtest) :
    donnees_brutes=data(filepath,filepathtest)
    table=np.array([['','Données brutes'],
                ['Nombre fonctions',donnees_brutes['Nombre fonctions']],
                ['Nombre tests',donnees_brutes['Nombre tests']],
                ['Nombre commentaires',donnees_brutes['Nombre commentaires']],
                ['Nombre variables', donnees_brutes['Nombre variables']],
                ['Taille fonction moyenne', donnees_brutes['Taille fonctions'][2]]])
    pd.table = pd.DataFrame(data=table[1:,1:], index=table[1:,0], columns=table[0,1:])
    print(pd.table)
    return(pd.table)

note_candidat('C:/Users/Gros/PycharmProjects/Lequipe/EventCandidatA.rb','C:/Users/Gros/PycharmProjects/Lequipe/EventCandidatATest.rb')
donnees_brutes_candidat('C:/Users/Gros/PycharmProjects/Lequipe/EventCandidatA.rb','C:/Users/Gros/PycharmProjects/Lequipe/EventCandidatATest.rb')
