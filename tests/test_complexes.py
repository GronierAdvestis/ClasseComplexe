from classe_complexe.ClasseComplexe import *
import pytest


# creation et affichage
@pytest.mark.parametrize(
    "a, b, affichage",
    [
        (-1, 2, "-1 + i2"),
        (2, -5, "2 - i5")
    ]
)
def test_creation(cache, a, b, affichage):
    print("\nTest de la creation")
    nombre = NombreComplexe(a, b)
    assert nombre.partie_reelle == a
    assert nombre.partie_imaginaire == b
    assert str(nombre) == affichage


# addition
@pytest.mark.parametrize(
    "somme1, somme2",
    [
        ("3.5 + i3", "8 - i2")
    ]
)
def test_addition(cache, somme1, somme2):
    print("\nTest de l'addition")
    nombre1 = NombreComplexe(1, -2)
    nombre2 = NombreComplexe(2.5, 5)
    assert str(nombre1 + nombre2) == somme1
    assert str(nombre1 + 7) == somme2


# soustraction
@pytest.mark.parametrize(
    "residu1, residu2",
    [
        ("-12 + i10.8", "-11 + i3.8")
    ]
)
def test_soustraction(cache, residu1, residu2):
    print("\nTest de la soustraction")
    nombre1 = NombreComplexe(-8, 3.8)
    nombre2 = NombreComplexe(4, -7)
    assert str(nombre1 - nombre2) == residu1
    assert str(nombre1 - 3) == residu2


# multiplication
@pytest.mark.parametrize(
    "produit1, produit2",
    [
        ("-14.5 + i46.0", "3.5 - i2.0")
    ]
)
def test_multiplication(cache, produit1, produit2):
    print("\nTest de la multiplication")
    nombre1 = NombreComplexe(7, -4)
    nombre2 = NombreComplexe(2.5, 8)
    assert str(nombre1 * nombre2) == produit1
    assert str(nombre1 * 0.5) == produit2


# conjugaison
@pytest.mark.parametrize(
    "conjugue",
    [
        "14.5 + i8"
    ]
)
def test_conjugaison(cache, conjugue):
    print("\nTest de la conjugaison")
    nombre = NombreComplexe(14.5, -8)
    assert str(nombre.conjugaison_complexe()) == conjugue


# division
@pytest.mark.parametrize(
    "dividende1, dividende2",
    [
        ("-5.25 + i8.25", "10.0 - i2.0")
    ]
)
def test_division(cache, dividende1, dividende2):
    print("\nTest de la division")
    nombre1 = NombreComplexe(45, -9)
    nombre2 = NombreComplexe(4, 8)
    assert str(nombre1 / nombre2) == dividende1
    assert str(nombre1 / 4.5) == dividende2
