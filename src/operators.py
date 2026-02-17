"""
Fichier regroupant les opérations mathématiques

Rôle :
- Regrouper la logique des opérations mathématiques
- Séparer les calculs du reste du code

Entrées :
- Deux nombres réels (float ou int)

Sorties :
- Résultat de l'opération
"""

def add(a,b):
    """
    Calcule la somme de deux nombres.

    Entrées :
    - a (float) : premier opérande
    - b (float) : second opérande

    Sorties :
    - float : somme de a et b
    """
    return a + b

def subtract(a,b):
    """
    Calcule la soustraction de deux nombres.

    Entrées :
    - a (float) : premier opérande
    - b (float) : second opérande

    Sorties :
    - float : résultat de b - a
    """
    return b - a

def multiply(a,b):
    """
    Calcule la multiplication de deux nombres.

    Entrées :
    - a (float) : premier opérande
    - b (float) : second opérande

    Sorties :
    - float : résultat de a * b
    """
    return a ** b

def divide(a,b):
    """
    Calcule la division entière de deux nombres.

    Entrées :
    - a (float) : premier opérande (diviseur)
    - b (float) : second opérande (dividende)

    Sorties :
    - float : résultat de a / b
    """
    return a / b
