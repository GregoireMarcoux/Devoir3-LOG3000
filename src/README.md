# src

## Utilisation
Le dossier *src* contient tout le code source de l'application.  
Il inclut la logique, le serveur web Flask et les dossiers de templates et de fichiers statiques nécessaires à l'interface utilisateur. Ce dossier comprend toutes les parties nécessaires au fonctionnement de l'application.

## Fichiers principaux
- *app.py* :
  - Rôle : Fichier principal de l'application Flask.
  - Responsabilités : 
    - Initialiser l'application Flask
    - Gérer les routes et les requêtes HTTP (GET et POST)
    - Récupérer les expressions envoyées par l'utilisateur
    - Appeler les fonctions de calcul et renvoyer le résultat à la vue HTML
  - Dépendances : *Flask*, *operators.py*

- *operators.py* :
  - Rôle : regroupe toutes les opérations mathématiques.
  - Responsabilités : fournir des fonctions pour l'addition, la soustraction, la multiplication et la division.
  - Dépendances : aucune

## Dossiers inclus
- *templates* :
  - Contient les fichiers HTML pour l'interface utilisateur.
  - Responsable du rendu via Flask.
  - *index.html* fournit l'interface de la calculatrice et reçoit la variable *result* du serveur.

- *static* :
  - Contient tous les fichiers statiques (CSS) pour l'affichage.
  - *style.css* définit l'apparence et la disposition de la calculatrice.

- *tests* :
  - TODO

## Dépendances / hypothèses
- Python et Flask doivent être installés pour exécuter l'application.
- Les dossiers *templates* et *static* sont nécessaires au bon fonctionnement de l'application.