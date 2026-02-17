"""
Application principale de la calculatrice

Rôle :
- Initialiser le serveur Flask
- Recevoir les expressions provenant de l'interface
- Effectuer les calculs
- Retourner le résultat à l'interface

Entrées :
- Requêtes HTTP GET et POST
- Expression mathématique sous forme de string

Sorties :
- Page HTML avec le résultat / un message d'erreur
"""

from flask import Flask, request, render_template
from operators import add, subtract, multiply, divide

# Création de l'app flask
app = Flask(__name__)

# Dictionnaire de conversion des strings en opérations 
OPS = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

def calculate(expr: str):
    """
    Analyse une expression mathématique contenant deux opérandes et un opérateur pour retourner le résultat.

    Entrées :
    - expr (str) : une expression mathématique sous forme de string, ex. "1 + 1"

    Sorties :
    - float : résultat du calcul

    Exceptions :
    - ValueError : si l'expression est vide, invalide ou mal formée
    """

    # Vérification que la chaine n'est pas vide et sous la forme de string
    if not expr or not isinstance(expr, str):
        raise ValueError("empty expression")

    # Retrait des espaces
    s = expr.replace(" ", "")

    op_pos = -1
    op_char = None

    # Recherche de la position de l'opérateur dans la chaine
    for i, ch in enumerate(s):
        if ch in OPS:
            if op_pos != -1:
                # Lance une erreur s'il y a plus d'un opérateur
                raise ValueError("only one operator is allowed")
            op_pos = i
            op_char = ch

    if op_pos <= 0 or op_pos >= len(s) - 1:
        # Lance une erreur si l'opérateur est absent ou mal placé
        raise ValueError("invalid expression format")

    # Défini les opérandes en fonction de la position de l'opérateur
    left = s[:op_pos]
    right = s[op_pos+1:]

    try:
        a = float(left)
        b = float(right)
    except ValueError:
        # Lance une erreur si les opérandes ne sont pas des nombres valides
        raise ValueError("operands must be numbers")

    # Effectue le calcul en appelant la fonction correspondante à l'opérateur trouvé
    return OPS[op_char](a, b)

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Gère les routes dans l'application Flask

    - GET : affiche la page de la calculatrice
    - POST : récupère l'expression, effectue le calcul et retourne le résultat à l'utilisateur

    Entrées :
    - Valeur contenue dans le champ d'affichage

    Sorties :
    - Page HTML avec le résultat ou une erreur
    """

    result = ""
    if request.method == 'POST':
        # Récupération de l'expression
        expression = request.form.get('display', '')
        try:
            result = calculate(expression)
        except Exception as e:
            # Trouve les erreurs (évite un crash) et les retourne à l'utilisateur
            result = f"Error: {e}"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    # Mode debug activé pour le développement
    app.run(debug=True)