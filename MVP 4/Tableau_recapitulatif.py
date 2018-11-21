import sys

sys.path.append('../MVP 2')
from Resultat_candidats_2 import *
sys.path.pop()
sys.path.append('../MVP 1')
from Resultat_candidats import *

filepath='C:/Users/Gros/PycharmProjects/Lequipe/EventCandidatA.rb'
filepathtest='C:/Users/Gros/PycharmProjects/Lequipe/EventCandidatATest.rb'

df1=donnees_brutes_candidat(filepath,filepathtest)
df2=donnees_brutes_candidat2(filepath,filepathtest)

print(df1+df2)
