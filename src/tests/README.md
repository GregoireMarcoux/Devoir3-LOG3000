# src/tests

## Utilisation
Le dossier *tests* contient les tests unitaires de l'application.
Il permet de vérifier que les opérations mathématiques du module *operators.py* se comportent comme prévu.

## Fichiers principaux
- *test_operators.py* :
  - Rôle : regrouper les tests unitaires des fonctions mathématiques.
  - Responsabilités :
    - Vérifier l'addition avec *add(a, b)*
    - Vérifier la soustraction avec *subtract(a, b)*
    - Vérifier la multiplication avec *multiply(a, b)*
    - Vérifier la division avec *divide(a, b)*
  - Dépendances : *pytest*, *src/operators.py*

- *test_app.py* :
  - Rôle : regrouper les tests unitaires et d'intégration légère du module *app.py*.
  - Responsabilités :
    - Vérifier les cas valides de la fonction *calculate(expr)*
    - Vérifier les erreurs de format et de validation dans *calculate(expr)*
    - Vérifier le comportement des routes Flask en GET et POST
  - Dépendances : *pytest*, *Flask*, *src/app.py*

## Instructions d'exécution des tests
Depuis la racine du projet, exécuter les commandes suivantes :
- Installer l'outil de test :
  - `python -m pip install pytest`
- Lancer tous les tests :
  - `python -m pytest -v`
- Lancer uniquement les tests des opérateurs :
  - `python -m pytest -v src/tests/test_operators.py`
- Lancer un test d'opérateur précis :
  - `python -m pytest -v src/tests/test_operators.py::test_add`
- Lancer uniquement les tests de l'application :
  - `python -m pytest -v src/tests/test_app.py`
- Lancer un test précis de l'application :
  - `python -m pytest -v src/tests/test_app.py::test_index_get_returns_page`

## Couverture actuelle des tests
Les tests actuels couvrent les 4 fonctions exposées dans *src/operators.py* :
- *test_add* : valide le résultat d'une addition.
- *test_subtract* : valide le résultat d'une soustraction.
- *test_multiply* : valide le résultat d'une multiplication.
- *test_divide* : valide le résultat d'une division avec résultat décimal.

Les tests couvrent aussi le module *src/app.py* :
- *calculate(expr)* :
  - Expression valide
  - Expression vide
  - Type invalide (non string)
  - Plusieurs opérateurs dans une expression
  - Expression sans opérateur
  - Opérateur mal positionné
  - Opérandes non numériques
- Route */* :
  - GET : affichage de la page
  - POST valide : affichage du résultat
  - POST invalide : affichage d'un message d'erreur

## Hypothèses
- Python est installé sur la machine.
- Le module *pytest* est installé dans le même environnement Python que celui utilisé pour exécuter les commandes.
