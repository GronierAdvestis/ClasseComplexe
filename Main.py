from classe_complexe.ClasseComplexe import *

toto = NombreComplexe(1, 2)
tutu = NombreComplexe(2, -1)

# test des différentes méthodes
print("affichage: ", toto)
print("somme: ", toto+tutu)
print("soustraction: ", toto-tutu)
print("multiplication: ", toto*tutu)
print("conjugaison: ", toto.conjugaison_complexe())
print("division: ", toto/tutu)


