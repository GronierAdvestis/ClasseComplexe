from ClasseComplexe import *

toto = NombreComplexe(1, 2)
tutu = NombreComplexe(2, 5)

# test des différentes méthodes
print("affichage: ", toto)
print("somme: ", toto+tutu)
print("soustraction: ", toto-4)
print("multiplication: ", toto*tutu)
print("conjugaison: ", toto.conjugaison_complexe())
print("division: ", toto/tutu)


