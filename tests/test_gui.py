"""Tests de l'interface Tkinter, pilotes par programme (sans clics).

Lance la vraie fenetre, simule les saisies et les clics, et verifie
les resultats dans l'interface et dans le fichier Excel.

Usage : python tests/test_gui.py
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import main  # noqa: E402

if os.path.exists(main.FICHE):
    os.remove(main.FICHE)
main.creer_fichier()

app = main.Application()
app.update()
resultats = []


def verifier(label, condition):
    resultats.append((label, bool(condition)))


def saisir(nom, classe, lettre, notes):
    app.vider()
    app.champ_nom.insert(0, nom)
    app.champ_classe.set(classe)
    app.champ_lettre.set(lettre)
    for matiere, valeur in zip(main.MATIERES, notes):
        app.champs_notes[matiere].insert(0, valeur)


# 1. Erreur si nom vide
messages = []
main.messagebox.showerror = lambda *a, **k: messages.append(a[1])
app.ajouter()
verifier("nom vide refuse", any("nom" in m.lower() for m in messages))

# 2. Ajout complet d'un eleve via l'interface
saisir("Karim", "1AC", "B", ["12", "15,5", "8"])
messages.clear()
app.ajouter()
app.update()
lignes = main.lire_lignes()
verifier("eleve ajoute via GUI", len(lignes) == 1
         and lignes[0][1] == "Karim" and lignes[0][2] == "1AC-B")
verifier("moyenne calculee (12+15,5+8)/3",
         lignes and abs(lignes[0][6] - 11.83) < 0.01)
verifier("tableau rempli", len(app.tree.get_children()) == 1)
verifier("formulaire vide apres ajout", app.champ_nom.get() == "")

# 3. Doublon refuse
saisir("Karim", "1AC", "B", ["5", "5", "5"])
messages.clear()
app.ajouter()
verifier("doublon refuse", any("deja" in m for m in messages))
verifier("pas de nouvelle ligne", len(main.lire_lignes()) == 1)

# 4. Note invalide refusee
saisir("Sara", "TCS", "A", ["25", "10", "10"])
messages.clear()
app.ajouter()
verifier("note > 20 refusee", any("20" in m for m in messages))

# 5. Selection recharge le formulaire
app.vider()
app.tree.selection_set(app.tree.get_children()[0])
app.update()
verifier("selection -> formulaire",
         app.champ_nom.get() == "Karim" and app.champ_classe.get() == "1AC"
         and app.champ_lettre.get() == "B"
         and app.champs_notes["Sciences"].get() == "15.5")

# 6. Modification via GUI
app.champ_nom.delete(0, "end")
app.champ_nom.insert(0, "Karim Modifie")
messages.clear()
app.modifier()
app.update()
verifier("modification sauvegardee", main.lire_lignes()[0][1] == "Karim Modifie")

# 7. Suppression via GUI
main.messagebox.askyesno = lambda *a, **k: True
app.tree.selection_set(app.tree.get_children()[0])
app.update()
app.supprimer()
app.update()
verifier("suppression via GUI",
         len(main.lire_lignes()) == 0 and len(app.tree.get_children()) == 0)

# 8. Interface mise a jour seulement apres une sauvegarde reussie
def sauver_ko(*args, **kwargs):
    raise PermissionError()

sauver_reel = main.sauver_ligne
main.sauver_ligne = sauver_ko
main.messagebox.showerror = lambda *a, **k: None
saisir("Nouveau", "2BAC", "C", ["5", "5", "5"])
app.ajouter()
app.update()
main.sauver_ligne = sauver_reel
verifier("echec de sauvegarde : rien dans le tableau",
         len(app.tree.get_children()) == 0)
verifier("echec de sauvegarde : saisie conservee",
         app.champ_nom.get() == "Nouveau")

app.destroy()

echecs = [label for label, ok in resultats if not ok]
for label, ok in resultats:
    print(("PASS" if ok else "FAIL"), "-", label)
print()
print("Test GUI %s (%d/%d)" % ("OK" if not echecs else "ECHEC",
                               len(resultats) - len(echecs), len(resultats)))

if os.path.exists(main.FICHE):
    os.remove(main.FICHE)
sys.exit(1 if echecs else 0)
