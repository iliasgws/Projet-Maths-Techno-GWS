# Changelog

Toutes les modifications notables de ce projet sont documentees dans ce fichier.

Le format s'inspire de [Keep a Changelog](https://keepachangelog.com/fr/1.1.0/) et le versionnement suit [SemVer](https://semver.org/lang/fr/).

## [Non publie]

### Ajoute

- Dossier `tests/` avec un test d'interface pilote par programme (13 cas, sans clics).
- Workflow de release : executables Windows (`.exe`), macOS et Linux construits a chaque tag `v*` et publies en release GitHub.

### Change

- README : reorganisation pour le rendre plus clair et plus accessible aux etudiants et aux utilisateurs finaux (demarrage rapide, premiers pas, depannage). Ajout d'une mention sur l'aide de l'IA.
- `index.html` : mise a jour pour refleter le nouveau README et les nouvelles sections.
- `AGENTS.md` : mention d'auteur remplacee par une formulation neutre (l'auteur du projet).

## [0.1.0] - 2026-09

### Ajoute

- MVP fonctionnel : saisie des notes (mathematiques, sciences, histoire) avec validation avant enregistrement.
- Calcul de la moyenne simple, arrondie a deux decimales.
- Enregistrement, modification et suppression des eleves dans `data/notes.xlsx`.
- Creation automatique du fichier de donnees au premier lancement.
- Messages d'erreur clairs si le fichier Excel est inaccessible.
- Tableau des eleves synchronise avec le fichier Excel.
- Icone de la fenetre (assets/).
- Integration continue : verification de la syntaxe et test de fumee de la logique.

[Non publie]: https://github.com/iliasgws/Projet-Maths-Techno-GWS/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/iliasgws/Projet-Maths-Techno-GWS/releases/tag/v0.1.0
