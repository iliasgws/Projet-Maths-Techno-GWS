# AGENTS.md : consignes pour les agents IA

Ce fichier s'adresse a tout agent (IA) travaillant dans ce depot. A lire avant le premier commit. Il resume le contexte du projet, les conventions et les regles a respecter.

## Contexte du projet

- Application de bureau (Python/Tkinter) qui sert d'intermediaire entre l'utilisateur et le fichier Excel `data/notes.xlsx` : saisie des notes, validation, calcul de la moyenne, enregistrement.
- Projet scolaire (Maths-Techno, GWS), maintenu par l'auteur du projet.
- Pile : Python 3.10+, interface Tkinter avec `ttk.Treeview`, lecture/ecriture Excel via openpyxl (voir `requirements.txt`, seule dependance).
- Fichiers utiles : `main.py` (application complete), `README.md` (documentation utilisateur), `CHANGELOG.md`, `CONTRIBUTING.md`.
- Site de documentation : https://iliasgws.github.io/Projet-Maths-Techno-GWS/ (genere depuis `index.html` a la racine).

## Structure de main.py

- Constantes en tete de fichier : `FICHE` (chemin du classeur), `ENTETES`, `MATIERES`, `CLASSES`, `LETTRES`. Ne pas remettre ces valeurs en dur ailleurs.
- Logique sans interface, testable sans affichage : `parse_note`, `creer_fichier`, `lire_lignes`, `prochain_id`, `sauver_ligne`, `supprimer_ligne`.
- Classe `Application` (interface) : garde la logique de donnees en dehors ; l'interface n'est mise a jour qu'apres une sauvegarde reussie.

## Git et branches

- Branche de travail : `dev`. Les commits directs sur `dev` sont autorises.
- Branche stable : `main`. Ne JAMAIS pousser directement sur `main`.
- Toute modification destinee a `main` passe par une pull request (`gh pr create`).
- Les pull requests sont fusionnees par l'auteur du projet, sauf instruction explicite contraire dans la conversation.
- Un commit par modification logique, messages courts en francais, sans em-dash.

## Conventions de texte

- Tous les textes du depot (README, CHANGELOG, wiki, commits, messages d'interface) sont en francais.
- Ecrire le francais sans accents, comme dans ce fichier : pas de e aigu, grave ou circonflexe, pas de cedille. Le modele GLM 5.3 Flash a tendance a en remettre : verifier ses sorties et retirer les accents avant de committer.
- Jamais d'em-dash (tiret cadratin) dans les textes du depot.

## Code

- Python 3.10+, stdlib + openpyxl uniquement. Pas de nouvelle dependance sans demander d'abord.
- Le fichier Excel `data/notes.xlsx` est la seule source de donnees : ne jamais mettre de donnees en dur dans le code.
- L'interface n'est mise a jour qu'apres une sauvegarde reussie du fichier.
- Toute erreur d'acces fichier (fichier ouvert dans Excel, dossier manquant) doit afficher un message, jamais faire planter l'application.
- Validation obligatoire avant enregistrement : nom non vide, classe + lettre choisies, notes entre 0 et 20 (virgule decimale acceptee), unicite `Nom + Classe`.

## Tests

- `python -m py_compile main.py` doit passer avant chaque commit.
- La logique (hors interface) doit rester testable sans affichage : garder les fonctions de donnees separees de la classe `Application`.
- Le workflow CI (`.github/workflows/ci.yml`) teste chaque push sur `dev` et `main` : il doit rester vert.

## Documentation

- Le README decrit le fonctionnement reel de l'application : le mettre a jour si le comportement change.
- Toute modification visible par l'utilisateur doit avoir une entree dans le CHANGELOG (section "Non publie").
- La page Pages (`index.html`) reflete le README : la mettre a jour en cas de changement visible.
- Le README mentionne l'aide de l'IA (code, images, documentation) : garder cette mention a jour.

## Assets

- `assets/` : icones. Le `.ico` contient deux variantes (detaillee pour 64-256 px, simplifiee pour 16-32 px). Ne pas regenerer les petites tailles depuis la grande.
- `maquette.png` : maquette affichee dans le README. Generer une image seulement sur demande.

## Securite

- Ne jamais committer de secret, token ou mot de passe (les tokens GitHub passent par gh auth, pas par les fichiers).
- Ne jamais committer `data/notes.xlsx` (donnees personnelles d'eleves) ni `.venv/` : deja couverts par `.gitignore`, ne pas les retirer.

## Style de travail

- Faire le minimum demande, proprement. Pas de fonctionnalite non demandee.
- Utiliser les sous-agents quand cela a du sens : refactoring, modification touchant plusieurs fichiers, recherche large dans le depot, revue de code, builds ou tests longs. Garder dans le contexte principal les decisions, les petites modifications et la synthese des resultats.
- Tester reellement (lancer le code, verifier le resultat) avant d'annoncer que c'est fait.
- Signaler ce qui a ete verifie et ce qui ne l'a pas ete.
