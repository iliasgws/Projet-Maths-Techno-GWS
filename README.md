# Projet Maths-Techno

Application de bureau pour saisir des notes, calculer les moyennes et enregistrer les résultats dans un fichier Excel.

> Statut : spécification du MVP. Le code reste à développer.

![Maquette de l'application](./Python_program_calculates_school%E2%80%A6_2K_20260917105853.jpeg)

## Le problème

Saisir les notes directement dans Excel peut provoquer des erreurs : texte à la place d'une note, valeur hors limite, formule supprimée ou mauvaise ligne modifiée. L'application sert d'intermédiaire entre l'utilisateur et le fichier Excel afin de contrôler chaque donnée avant son enregistrement.

## Périmètre du MVP

La première version restera volontairement simple :

- une application locale en Python avec Tkinter ;
- un seul fichier Excel, `data/notes.xlsx` ;
- une seule feuille, `Notes` ;
- trois matières fixes : mathématiques, sciences et histoire ;
- une moyenne simple, sans coefficient ;
- l'ajout, la modification et la suppression d'un élève ;
- un tableau dans l'application qui reprend le contenu du fichier Excel.

La recherche, les graphiques, les bulletins PDF, les comptes utilisateurs, les coefficients et le travail à plusieurs ne font pas partie du MVP.

## Données enregistrées

Chaque élève correspond à une ligne de la feuille `Notes`.

| Colonne | Contenu |
| --- | --- |
| `ID` | numéro unique créé automatiquement |
| `Nom` | nom complet de l'élève |
| `Classe` | classe de l'élève |
| `Mathématiques` | note sur 20 |
| `Sciences` | note sur 20 |
| `Histoire` | note sur 20 |
| `Moyenne` | moyenne calculée et arrondie à deux décimales |

La moyenne est calculée ainsi :

```text
moyenne = (mathématiques + sciences + histoire) / 3
```

Un même nom peut exister dans plusieurs classes, mais la combinaison `Nom + Classe` doit rester unique.

## Interface prévue

La fenêtre contient :

- deux champs texte : `Nom` et `Classe` ;
- trois champs de note : `Mathématiques`, `Sciences` et `Histoire` ;
- les boutons `Ajouter`, `Modifier`, `Supprimer` et `Vider` ;
- un tableau affichant tous les élèves et leur moyenne.

Quand l'utilisateur sélectionne une ligne du tableau, ses données sont recopiées dans le formulaire. Il peut alors les modifier ou supprimer l'élève concerné.

## Règles de saisie

Avant tout enregistrement, le programme vérifie que :

- le nom et la classe ne sont pas vides ;
- les trois notes sont renseignées ;
- chaque note est un nombre compris entre 0 et 20 ;
- les nombres décimaux avec une virgule, comme `12,5`, sont acceptés ;
- l'élève n'existe pas déjà dans la même classe.

Si une donnée est incorrecte, un message indique le champ à corriger. Aucune ligne ne doit alors être ajoutée ou modifiée.

## Synchronisation avec Excel

Au démarrage, l'application crée `data/notes.xlsx` s'il n'existe pas, puis charge son contenu dans le tableau.

Pour chaque ajout, modification ou suppression, elle suit cet ordre :

1. vérifier les données du formulaire ;
2. calculer la moyenne ;
3. enregistrer la modification dans Excel ;
4. recharger le tableau depuis le fichier.

L'interface n'est actualisée qu'après une sauvegarde réussie. Si le fichier est ouvert dans Excel, introuvable ou illisible, l'application affiche une erreur claire et reste ouverte.

## Critères de réussite

Le MVP sera considéré comme terminé lorsque les cas suivants fonctionneront :

- une saisie valide apparaît dans Excel et dans le tableau ;
- `10`, `15,5` et `20` sont acceptés comme notes ;
- du texte, une note négative ou une note supérieure à 20 sont refusés ;
- la moyenne affichée est correcte et arrondie à deux décimales ;
- les données sont toujours présentes après la fermeture et le redémarrage de l'application ;
- la modification et la suppression d'un élève produisent le même résultat dans Excel et à l'écran ;
- une erreur d'accès au fichier affiche un message sans fermer brutalement le programme.

## Technologies

- Python 3.10 ou version plus récente
- Tkinter pour l'interface
- `ttk.Treeview` pour le tableau
- openpyxl pour lire et modifier le fichier Excel

## Structure prévue

```text
Projet-Maths-Techno-GWS/
├── main.py
├── requirements.txt
├── data/
│   └── notes.xlsx        # créé automatiquement
└── README.md
```

## Installation prévue

```bash
git clone https://github.com/iliasgws/Projet-Maths-Techno-GWS.git
cd Projet-Maths-Techno-GWS
python -m pip install -r requirements.txt
python main.py
```

Sous certaines distributions Linux, Tkinter doit être installé séparément avec le paquet `python3-tk`.
