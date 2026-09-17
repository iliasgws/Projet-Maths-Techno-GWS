# Projet Maths-Techno :
## une application pour gérer les notes

Pour notre projet, nous sommes partis d’un problème courant à l’école : quand on saisit directement des notes dans Excel, une simple erreur de frappe peut fausser une moyenne ou modifier une formule sans qu’on s’en rende compte.

Notre idée est de créer une petite application en Python avec Tkinter. L’élève ou le professeur remplira un formulaire avec le nom de l’élève, sa classe et ses notes. Avant d’enregistrer les informations, le programme vérifiera que les champs sont bien remplis et que les notes sont des nombres compris entre 0 et 20. Si une donnée est incorrecte, un message expliquera ce qu’il faut corriger au lieu de faire planter le programme.

L’application calculera ensuite la moyenne automatiquement. Elle pourra utiliser une moyenne simple ou une moyenne avec coefficients :

Moyenne pondérée = somme des notes × leurs coefficients ÷ somme des coefficients

Les résultats seront enregistrés dans un fichier Excel grâce à la bibliothèque openpyxl. Un tableau dans l’interface permettra aussi de consulter les élèves, leurs notes et leurs moyennes sans ouvrir Excel. L’utilisateur pourra ajouter un élève, modifier ses résultats ou supprimer une ligne.

La partie la plus délicate sera de synchroniser correctement l’interface et le fichier Excel. Par exemple, si une note est modifiée à l’écran, le programme devra mettre à jour la bonne cellule dans le fichier, enregistrer le changement, puis actualiser le tableau. Il faudra également prévoir les problèmes possibles, comme un fichier déjà ouvert, une donnée manquante ou une erreur pendant l’enregistrement. Nous utiliserons donc des contrôles de saisie, des messages d’erreur et des sauvegardes pour éviter de perdre les données.

Ce projet mélange les mathématiques, avec le calcul des moyennes et des coefficients, et la technologie, avec la programmation, l’interface graphique et la gestion d’un fichier Excel. Si nous avons le temps, nous pourrons aussi ajouter une recherche par nom, le classement des élèves, la moyenne générale de la classe ou un graphique des résultats.

Le but n’est pas de remplacer Excel, mais de rendre son utilisation plus simple et de limiter les erreurs.
