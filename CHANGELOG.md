# Changelog

Toutes les modifications notables de ce projet sont documentees dans ce fichier.

Le format s'inspire de [Keep a Changelog](https://keepachangelog.com/fr/1.1.0/) et le versionnement suit [SemVer](https://semver.org/lang/fr/).

## [Non publie]

### Ajoute

- Documentation complete : README reecrit, guide de contribution, changelog, licence MIT et page GitHub Pages.
- Workflow de deploiement de la page de documentation sur GitHub Pages.

### Change

- README aligne sur le fonctionnement reel de l'application : choix de la classe et de la lettre en listes, format de classe `2BAC-B`, identifiant attribue automatiquement.

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
