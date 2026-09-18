# Guide de contribution

Merci de votre interet pour ce projet. Ce document decrit le workflow, les conventions et les verifications a passer avant de proposer une modification.

## Workflow de branches

- `dev` est la branche de travail : les commits directs y sont autorises pour les petites modifications.
- `main` est la branche stable : ne jamais y pousser directement.
- Toute modification destinee a `main` passe par une pull request, fusionnee par l'auteur.

```bash
git checkout dev
# modifications puis
git commit -m "Description courte en francais"
git push
# puis ouvrir une pull request de dev vers main
gh pr create --base main --head dev
```

## Conventions de commit

- Messages courts, en francais, sans em-dash.
- Un commit par modification logique.
- Exemples : `README : correction de l'installation`, `main.py : validation de la lettre`.

## Avant de pousser

1. Verifier la syntaxe :

```bash
python -m py_compile main.py
```

2. S'assurer que la CI reste verte (elle verifie la syntaxe et execute un test de fumee de la logique, sans interface).

3. Tester reellement l'application si la modification touche l'interface ou les donnees.

## Regles de code

- Python 3.10+, bibliotheque standard + openpyxl uniquement. Pas de nouvelle dependance sans en discuter d'abord.
- `data/notes.xlsx` est la seule source de donnees : aucune donnee en dur dans le code.
- La logique (hors interface) reste testable sans affichage : garder les fonctions de donnees separees de la classe `Application`.
- Toute erreur d'acces fichier affiche un message, sans faire planter l'application.
- Textes du depot en francais, sans em-dash.

## Documentation

- Mettre a jour le README si le comportement de l'application change.
- Ajouter une entree au CHANGELOG (section `Non publie`) pour toute modification visible.
- Mettre a jour la page GitHub Pages (`index.html`) si le README change de facon visible.

## Securite

- Ne jamais committer de secret, token ou mot de passe.
- Ne jamais committer `data/notes.xlsx` (donnees personnelles d'eleves) ni `.venv/` : ils sont couverts par `.gitignore`.
