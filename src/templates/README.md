# templates

## Raison d'être du module
Le dossier *templates* contient les fichiers HTML utilisés par Flask pour générer la page web. Ces fichiers définissent la structure, le contenu et le comportement de l'interface utilisateur.

Dans ce projet, il contient uniquement *index.html*, la page principale de la calculatrice Flask. Ce template est rendu par Flask à chaque requête GET ou POST et reçoit la variable *result* pour afficher le résultat du calcul.

## Principaux fichiers
- *index.html* :
  - Rôle : fournir l'interface utilisateur de la calculatrice
  - Contenu : 
    - Champ d'affichage pour l'expression et le résultat (*#display*)
    - Grille de boutons pour les chiffres et les opérateurs
    - Scripts JavaScript pour ajouter des valeurs au champ d'affichage (*appendToDisplay*)
    - Scripts JavaScript pour vider le champ d'affichage (*clearDisplay*)
  - La page utilise la feuille de styles *style.css* du dossier *static* pour l'apparence et la mise en page

## Dépendances / hypothèses
- Dépend de Flask pour le rendu du template et insérer la variable *result* dans le HTML.
- Dépend du fichier CSS *style.css* pour les effets visuels et l'apparence.
- Compatible avec les navigateurs modernes supportant HTML5 et JavaScript.
