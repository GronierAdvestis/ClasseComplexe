# classe representant un nombre complexe sous forme algebrique


class NombreComplexe:
    """Classe representant les nombres complexes sous forme algebrique"""

    def __init__(self, partie_reelle, partie_imaginaire):
        self._partie_reelle = partie_reelle  # partie reelle du nombre complexe
        self._partie_imaginaire = partie_imaginaire  # partie imaginaire du nombre complexe

    # ##########################################################################################
    # Operations complexes
    # ##########################################################################################

    def __add__(self, nombre):  # methode d'addition au sens des nombre complexes, le premier doit etre complexe
        if not isinstance(nombre, NombreComplexe):  # si le second nombre n'est pas complexe...
            nombre = cplx(nombre)  # ... il est converti

        partie_reelle = self.partie_reelle + nombre.partie_reelle  # calcul de la partie reelle de la somme
        partie_imaginaire = self.partie_imaginaire + nombre.partie_imaginaire  # calcul de la partie imaginaire de la somme
        somme_complexe = NombreComplexe(partie_reelle, partie_imaginaire)
        return somme_complexe

    def __sub__(self, nombre):  # methode de soustraction au sens des nombres complexes, le premier doit etre complexe
        if not isinstance(nombre, NombreComplexe):  # si le second nombre n'est pas complexe...
            nombre = cplx(nombre)  # ... il est converti

        partie_reelle = self.partie_reelle - nombre.partie_reelle  # calcul de la partie reelle de la soustraction
        partie_imaginaire = self.partie_imaginaire - nombre.partie_imaginaire  # calcul de la partie imaginaire de la soustraction
        residu_complexe = NombreComplexe(partie_reelle, partie_imaginaire)

        return residu_complexe

    def __mul__(self, nombre):  # methode de multiplication au sens des nombres complexes, le premier doit etre complexe
        if not isinstance(nombre, NombreComplexe):  # si le second nombre n'est pas complexe...
            nombre = cplx(nombre)  # ... il est converti

        partie_reelle = self.partie_reelle * nombre.partie_reelle + self._partie_imaginaire * nombre.partie_imaginaire  # calcul de la partie reelle du produit
        partie_imaginaire = self.partie_imaginaire * nombre.partie_reelle + self.partie_reelle * nombre.partie_imaginaire  # calcul de la partie imaginaire de la somme
        produit_complexe = NombreComplexe(partie_reelle, partie_imaginaire)
        return produit_complexe

    def conjugaison_complexe(self):
        """methode de conjugaison au sens des nombres complexes"""
        partie_reelle = self.partie_reelle
        partie_imaginaire = - self.partie_imaginaire
        conjugue = NombreComplexe(partie_reelle, partie_imaginaire)
        return conjugue

    def __truediv__(self, nombre):  # methode de division au sens des nombres complexes, le premier nombre doit etre complexe et le second non nul
        if not isinstance(nombre, NombreComplexe):  # si le second nombre n'est pas complexe...
            nombre = cplx(nombre)  # ... il est converti

        # calcul intermediaire de la fraction
        numerateur = (self * nombre.conjugaison_complexe())
        denominateur = nombre.partie_reelle ** 2 - nombre.partie_imaginaire ** 2

        partie_reelle = numerateur.partie_reelle / denominateur  # calcul de la partie reelle de la division
        partie_imaginaire = numerateur.partie_imaginaire / denominateur  # calcul de la partie imaginaire de la somme
        div_complexe = NombreComplexe(partie_reelle, partie_imaginaire)
        return div_complexe

    # ##########################################################################################
    # Lecture et affichage
    # ##########################################################################################

    @property
    def partie_reelle(self):
        """acces a la partie reelle"""
        return self._partie_reelle

    @property
    def partie_imaginaire(self):
        """acces a la partie imaginaire"""
        return self._partie_imaginaire

    def __str__(self):
        """affichage du nombre complexe sous forme algebrique"""
        if self.partie_imaginaire == 0:
            signe = 0
        else:
            if abs(self.partie_imaginaire)/self.partie_imaginaire > 0:  # si la partie imagnaire est positive
                signe = "+"
            else:  # si la partie imaginaire est negative
                signe = "-"
        forme_algebrique = str(self.partie_reelle) + " " + signe + " i" + str(abs(self.partie_imaginaire))
        # f"{self.partie_reelle} {signe} i{abs(self.partie_imaginaire)}"
        return forme_algebrique


def cplx(nombre):
    """convertit un nombre reel en nombre complexe"""
    nombre = NombreComplexe(nombre, 0)
    return nombre

