# AGENTS.md : regles du depot

Ce fichier s'adresse a tout agent (IA) travaillant dans ce depot. A lire avant le premier commit.

## Contexte du projet

Application de bureau (Python/Tkinter) pour saisir des notes d'eleves et les enregistrer dans `data/notes.xlsx`. Projet scolaire (Maths-Techno, GWS). Auteur principal : Ilias Mouhcine.

## Git et branches

- Branche de travail : `dev`. Les commits directs sur `dev` sont autorises.
- Branche stable : `main`. Ne JAMAIS pousser directement sur `main`.
- Toute modification destinee a `main` passe par une pull request (`gh pr create`).
- Les pull requests sont fusionnees par l'auteur (Ilias), sauf instruction explicite contraire dans la conversation.
- Un commit par modification logique, messages courts en francais, sans em-dash.

## Code

- Python 3.10+, stdlib + openpyxl uniquement (voir `requirements.txt`).
- Tkinter pour l'interface, `ttk.Treeview` pour le tableau.
- Le fichier Excel `data/notes.xlsx` est la seule source de donnees : ne jamais mettre de donnees en dur dans le code.
- L'interface n'est mise a jour qu'apres une sauvegarde reussie du fichier.
- Toute erreur d'acces fichier (fichier ouvert dans Excel, dossier manquant) doit afficher un message, jamais faire planter l'application.
- Validation obligatoire avant enregistrement : nom non vide, classe + lettre choisies, notes entre 0 et 20 (virgule decimale acceptee), unicite `Nom + Classe`.
- Pas de nouvelle dependance sans demander d'abord.

## Tests

- `python -m py_compile main.py` doit passer avant chaque commit.
- La logique (hors interface) doit rester testable sans affichage : garder les fonctions de donnees separees de la classe `Application`.
- Le workflow CI (`.github/workflows/ci.yml`) teste chaque push sur `dev` et `main` : il doit rester vert.

## Assets et documentation

- `assets/` : icones. Le `.ico` contient deux variantes (detaillee pour 64-256 px, simplifiee pour 16-32 px). Ne pas regenerer les petites tailles depuis la grande.
- `maquette.png` : maquette affichee dans le README. Generer une image seulement sur demande.
- Le README mentionne l'aide de l'IA (code, images, documentation) : garder cette mention a jour.
- Le wiki (https://github.com/iliasgws/Projet-Maths-Techno-GWS/wiki) documente le fonctionnement : le mettre a jour si le comportement de l'application change.
- Tous les textes du depot (README, wiki, commits, messages d'interface) sont en francais, sans em-dash.

## Securite

- Ne jamais committer de secret, token ou mot de passe (les tokens GitHub passent par gh auth, pas par les fichiers).
- Ne jamais committer `data/notes.xlsx` (donnees personnelles d'eleves) ni `.venv/` : deja couverts par `.gitignore`, ne pas les retirer.

## Style de travail

- Faire le minimum demande, proprement. Pas de fonctionnalite non demandee.
- Tester reellement (lancer le code, verifier le resultat) avant d'annoncer que c'est fait.
- Signaler ce qui a ete verifie et ce qui ne l'a pas ete.
