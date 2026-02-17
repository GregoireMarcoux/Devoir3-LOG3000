from src.operators import add, subtract, multiply, divide


# Teste que l'addition retourne la somme de deux nombres.
def test_add():
    assert add(2, 2) == 4


# Teste que la soustraction calcule bien a - b.
def test_subtract():
    assert subtract(8, 2) == 6


# Teste que la multiplication retourne le produit des deux nombres.
def test_multiply():
    assert multiply(2, 3) == 6


# Teste que la division retourne a/b et un résultat décimal si nécessaire.
def test_divide():
    assert divide(5, 2) == 2.5
    
