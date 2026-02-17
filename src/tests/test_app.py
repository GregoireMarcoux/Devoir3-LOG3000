import sys
from pathlib import Path

import pytest


# Ajoute le dossier src au PYTHONPATH pour importer app.py et operators.py.
SRC_DIR = Path(__file__).resolve().parents[1]
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

import app as app_module


# Crée un client Flask de test pour valider les routes HTTP.
@pytest.fixture
def client():
    app_module.app.config["TESTING"] = True
    with app_module.app.test_client() as test_client:
        yield test_client


# Vérifie qu'une expression valide est correctement calculée.
def test_calculate_valid_expression():
    assert app_module.calculate("2 + 2") == 4.0


# Vérifie qu'une expression vide déclenche une erreur explicite.
def test_calculate_empty_expression_raises_value_error():
    with pytest.raises(ValueError, match="empty expression"):
        app_module.calculate("")


# Vérifie qu'un type invalide (non string) déclenche une erreur.
def test_calculate_non_string_raises_value_error():
    with pytest.raises(ValueError, match="empty expression"):
        app_module.calculate(None)


# Vérifie que plusieurs opérateurs dans la même expression sont refusés.
def test_calculate_multiple_operators_raises_value_error():
    with pytest.raises(ValueError, match="only one operator is allowed"):
        app_module.calculate("1+2+3")


# Vérifie qu'une expression sans opérateur est considérée invalide.
def test_calculate_missing_operator_raises_value_error():
    with pytest.raises(ValueError, match="invalid expression format"):
        app_module.calculate("123")


# Vérifie qu'un opérateur mal placé est considéré invalide.
def test_calculate_operator_at_end_raises_value_error():
    with pytest.raises(ValueError, match="invalid expression format"):
        app_module.calculate("3+")


# Vérifie que des opérandes non numériques déclenchent une erreur.
def test_calculate_non_numeric_operands_raises_value_error():
    with pytest.raises(ValueError, match="operands must be numbers"):
        app_module.calculate("a+2")


# Vérifie que la route GET renvoie bien la page de la calculatrice.
def test_index_get_returns_page(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Flask Calculator" in response.data


# Vérifie que la route POST affiche le résultat pour une expression valide.
def test_index_post_valid_expression_displays_result(client):
    response = client.post("/", data={"display": "2+2"})
    assert response.status_code == 200
    assert b'value="4.0"' in response.data


# Vérifie que la route POST affiche un message d'erreur en cas d'expression invalide.
def test_index_post_invalid_expression_displays_error(client):
    response = client.post("/", data={"display": "2++2"})
    assert response.status_code == 200
    assert b"Error:" in response.data
