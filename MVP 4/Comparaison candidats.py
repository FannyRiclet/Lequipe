import numpy as np

import sys
import numpy as np

from Tableau_recapitulatif import *

sys.path.append('../MVP 1')
from Resultat_candidats import *
from Fonctionnalite1_2_1 import *
from Fonctionnalite1_2_2 import *
from Fonctionnalite1_2_3 import *
from Fonctionnalite1_2_4 import *
from Fonctionnalite1_2_5 import *
from Fonctionnalite1_4 import *

sys.path.append('../MVP 2')
from Resultat_candidats_2 import *
from Fonctionnalite2_2_1 import *
from Fonctionnalite2_2_2 import *
from Fonctionnalite2_2_3 import *
from Fonctionnalite2_2_4 import *
from Fonctionnalite2_2_5 import *

liste_noms_candidats=['CandidatA','CandidatB','CandidatC']

def data_candidats(Nom_dev, liste_noms_candidats) :
    table=donnees_brutes_candidat_finales(Nom_dev,liste_noms_candidats[0])
    for k in range(1,len(liste_noms_candidats)) :
        column=donnees_brutes_candidat_finales(Nom_dev,liste_noms_candidats[k])[:,1]
        table=np.c_[table,column]
    print(pd.DataFrame(data=table[1:,1:], index=table[1:,0], columns=table[0,1:]))
    return(table)

data_candidats('Gros', liste_noms_candidats)
