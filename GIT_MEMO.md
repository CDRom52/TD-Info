# Mémo Git - Commandes Utiles

Ce fichier contient les commandes essentielles pour utiliser ce dossier sur GitHub.

## Astuces VS Code (Markdown)

* **Voir l'aperçu du README** : `Ctrl` + `Shift` + `V`

## Synchronisation (Plusieurs PC)

### 1. Première fois sur un nouvel ordi (Récupérer tout le projet)
À faire une seule fois pour installer le dossier sur le nouveau PC :
* `git clone https://github.com/CDRom52/TD-Info.git`

### 2. Au début de chaque séance (Mettre à jour le code)
Si j'ai déjà le dossier mais que j'ai fait des modifs ailleurs :
* `git pull`
  *(Cette commande "tire" les dernières nouveautés de GitHub vers mon PC actuel).*
* `git fetch`
  *(Cette commande me montre les changements apportés sans les intégrer sur mon PC actuel).*

### 3. À la fin de chaque séance (Sauvegarder)
* `git add .`
* `git commit -m "Fin de séance"`
* `git push`
---

## Python & Environnement (.venv)

### Gérer les bibliothèques
* `pip install <nom_de_la_bibliotheque>` : Installer une bibliothèque sur l'environnement actuel.
* `pip list` : Voir ce qui est installé dans mon environnement actuel.
* `pip freeze > requirements.txt` : Sauvegarder la liste des bibliothèques pour GitHub.
* `pip install -r requirements.txt` : Réinstaller toutes les bibliothèques d'un coup (sur un nouveau PC).

### Créer un .venv
1. `python -m venv .venv` (Créer)
2. `.\.venv\Scripts\activate` (Activer sur Windows)
3. Créer un fichier .gitignore
4. Ajouter la ligne `.venv/`

---