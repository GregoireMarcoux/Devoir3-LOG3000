# Devoir3-LOG3000
## Équipe #13
Ce repo contient le projet du devoir 3 de LOG3000, soit une calculatrice en ligne.

## Objectif
L'objectif du projet est de configurer un projet sur GitHub dans l'optique de faciliter la mise en route du projet pour d'autres membres d'une équipe. Il faut donc configurer le repo, documenter le code, corriger certains bogues et réaliser des tests afin de s'assurer du bon fonctionnement du projet.

## Prérequis d'installation
Avant d'installer le projet, il faut s'assurer d'effectuer les étapes suivantes :
- Créer son compte GitHub
- Installer Git localement
- Installer les paquets Python et Pip
- Installer un logiciel de modification de code (IDE) tel que VSCode

## Instructions d'installation
Afin d'installer le projet, il faut suivre les étapes suivantes :
- Ouvrir l'invite de commande (CMD) dans le répertoire souhaité.
- Cloner le répertoire du projet à l'aide de la commande "git clone https://github.com/GregoireMarcoux/Devoir3-LOG3000.git".
- Ouvrir l'IDE de son choix et y ouvrir le répertoire.
- Installer les dépendables du projet dans le terminal avec Pip "py -m pip install flask".

## Utilisation
Afin d'utiliser le projet, il faut lancer l'application par le fichier *app.py*. Il faut appuyer sur la flèche en haut à droite afin de démarrer le programme. Dans la console apparaîtra l'adresse locale où le projet est lancé. Il faut copier celle-ci et la coller dans le navigateur de son choix, ou cliquer directement sur l'adresse pour l'ouvrir.

Le programme constitue une calculatrice permettant de faire des additions, soustractions, mutiplications et divisions. Pour ce faire, il suffit d'inscrire le nombre de son choix; choisir l'opération désirée; choisir un deuxième nombre; appuyer sur la touche =. La réponse de l'opération sera affichée. Pour nettoyer le champ, il suffit d'appuyer sur la touche C. Si l'opération choisie est impossible, un message d'erreur sera affiché expliquant le problème.

ATTENTION : Une seule opération à la fois peut être réalisée. La calculatrice ne supporte par plusieurs opérations simultanées.

## Tests
Les tests unitaires du projet sont regroupés dans le dossier *src/tests*.

### Prérequis
- Avoir Python installé.
- Installer *pytest* dans l'environnement Python utilisé :
  - `python -m pip install pytest`

### Exécuter les tests
Depuis la racine du projet (*Devoir3-LOG3000*), lancer :
- Tous les tests :
  - `python -m pytest -v`
- Un fichier de test précis :
  - `python -m pytest -v src/tests/test_operators.py`
- Un test précis :
  - `python -m pytest -v src/tests/test_operators.py::test_add`

### Ajouter des tests plus tard
Pour ajouter de nouveaux tests :
- Créer (ou compléter) un fichier `test_*.py` dans *src/tests*.
- Nommer chaque fonction de test avec le préfixe `test_`.
- Utiliser des `assert` pour valider les résultats attendus.

## Contributions
- PlayeerOne (10/20/2025) : Création du projet initial
- GregoireMarcoux (02/17/2026) : Création du repo et rédaction de la documentation initiale 
- OlivierThabet (02/17/2026) : Ajout des tests pour operators.py, app.py et la documentation associée
