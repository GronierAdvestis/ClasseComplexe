# classe représentant un nombre complexe sous forme algébrique


class NombreComplexe:
    """Classe représentant les nombres complexes sous forme algébrique"""

    def __init__(self, partie_reelle, partie_imaginaire):
        self._partie_reelle = partie_reelle  # partie réelle du nombre complexe
        self._partie_imaginaire = partie_imaginaire  # partie imaginaire du nombre complexe

    # ##########################################################################################
    # Opérations complexes
    # ##########################################################################################

    def __add__(self, nombre):  # méthode d'addition au sens des nombre complexes, le premier doit être complexe
        if not isinstance(nombre, NombreComplexe):  # si le second nombre n'est pas complexe...
            nombre = cplx(nombre)  # ... il est converti

        partie_reelle = self.partie_reelle + nombre.partie_reelle  # calcul de la partie réelle de la somme
        partie_imaginaire = self.partie_imaginaire + nombre.partie_imaginaire  # calcul de la partie imaginaire de la somme
        somme_complexe = NombreComplexe(partie_reelle, partie_imaginaire)
        return somme_complexe

    def __sub__(self, nombre):  # méthode de soustraction au sens des nombres complexes, le premier doit être complexe
        if not isinstance(nombre, NombreComplexe):  # si le second nombre n'est pas complexe...
            nombre = cplx(nombre)  # ... il est converti

        partie_reelle = self.partie_reelle - nombre.partie_reelle  # calcul de la partie réelle de la soustraction
        partie_imaginaire = self.partie_imaginaire - nombre.partie_imaginaire  # calcul de la partie imaginaire de la soustraction
        residu_complexe = NombreComplexe(partie_reelle, partie_imaginaire)
        return residu_complexe

    def __mul__(self, nombre):  # méthode de multiplication au sens des nombres complexes, le premier doit être complexe
        if not isinstance(nombre, NombreComplexe):  # si le second nombre n'est pas complexe...
            nombre = cplx(nombre)  # ... il est converti

        partie_reelle = self.partie_reelle * nombre.partie_reelle + self._partie_imaginaire * nombre.partie_imaginaire  # calcul de la partie réelle du produit
        partie_imaginaire = self.partie_imaginaire * nombre.partie_reelle + self.partie_reelle * nombre.partie_imaginaire  # calcul de la partie imaginaire de la somme
        produit_complexe = NombreComplexe(partie_reelle, partie_imaginaire)
        return produit_complexe

    def conjugaison_complexe(self):  # méthode de conjugaison au sens des nombres complexes
        partie_reelle = self.partie_reelle
        partie_imaginaire = - self.partie_imaginaire
        conjugue = NombreComplexe(partie_reelle, partie_imaginaire)
        return conjugue

    def __truediv__(self, nombre):  # méthode de division au sens des nombres complexes, le premier nombre doit être complexe et le second non nul
        if not isinstance(nombre, NombreComplexe):  # si le second nombre n'est pas complexe...
            nombre = cplx(nombre)  # ... il est converti

        # calcul intermediaire de la fraction
        numerateur = (self * nombre.conjugaison_complexe())
        denominateur = nombre.partie_reelle ** 2 - nombre.partie_imaginaire ** 2

        partie_reelle = numerateur.partie_reelle / denominateur  # calcul de la partie réelle de la division
        partie_imaginaire = numerateur.partie_imaginaire / denominateur  # calcul de la partie imaginaire de la somme
        div_complexe = NombreComplexe(partie_reelle, partie_imaginaire)
        return div_complexe

    # ##########################################################################################
    # Lecture et affichage
    # ##########################################################################################

    @property
    def partie_reelle(self):
        """accès à la partie réelle"""
        return self._partie_reelle

    @property
    def partie_imaginaire(self):
        """accès à la partie imaginaire"""
        return self._partie_imaginaire

    def __str__(self):  # affichage du nombre complexe sous forme algébrique
        if abs(self.partie_imaginaire)/self.partie_imaginaire > 0:  # si la partie imagnaire est positive
            signe = "+"
        else:  # si la parti imaginaire est négative
            signe = "-"

        return str(self.partie_reelle) + " " + signe + " i" + str(abs(self.partie_imaginaire))


def cplx(nombre):
    """convertit un nombre réel en nombre complexe"""
    nombre = NombreComplexe(nombre, 0)
    return nombre

