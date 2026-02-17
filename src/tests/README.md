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

## Couverture actuelle des tests
Les tests actuels couvrent les 4 fonctions exposées dans *src/operators.py* :
- *test_add* : valide le résultat d'une addition.
- *test_subtract* : valide le résultat d'une soustraction.
- *test_multiply* : valide le résultat d'une multiplication.
- *test_divide* : valide le résultat d'une division avec résultat décimal.

## Hypothèses
- Python est installé sur la machine.
- Le module *pytest* est installé dans le même environnement Python que celui utilisé pour exécuter les commandes.
