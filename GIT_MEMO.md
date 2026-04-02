# Mémo Git - Commandes Utiles

Ce fichier contient les commandes essentielles pour utiliser ce dossier sur GitHub.

## Astuces VS Code (Markdown)

* **Voir l'aperçu du README** : `Ctrl` + `Shift` + `V`
* **Ouvrir l'aperçu sur le côté (Split View)** : `Ctrl` + `K` puis `V` 
  *(Pratique pour écrire à gauche et voir le résultat à droite !)*

## Synchronisation (Plusieurs PC)

### 1. Première fois sur un nouvel ordi (Récupérer tout le projet)
À faire une seule fois pour installer le dossier sur le nouveau PC :
* `git clone https://github.com/CDRom52/TD-Info.git`

### 2. Au début de chaque séance (Mettre à jour le code)
Si j'ai déjà le dossier mais que j'ai fait des modifs ailleurs :
* `git pull`
  *(Cette commande "tire" les dernières nouveautés de GitHub vers mon PC actuel).*

### 3. À la fin de chaque séance (Sauvegarder)
* `git add .`
* `git commit -m "Fin de séance"`
* `git push`
---

## Commandes de secours & Vérification

### Voir l'état du dépôt
* `git status` : Pour savoir quels fichiers ont été modifiés et s'ils sont prêts à être commités.
* `git log --oneline` : Pour voir l'historique simplifié de tes sauvegardes.

### Gérer l'adresse distante (GitHub)
* `git remote -v` : Vérifier l'adresse de mon dépôt GitHub.
* `git remote set-url origin URL_ICI` : Changer l'adresse si elle est fausse.

### Gérer la branche
* `git branch -M main` : Renommer la branche actuelle en "main".

---

## Python & Environnement (.venv)

### Gérer les bibliothèques
* `pip list` : Voir ce qui est installé dans mon environnement actuel.
* `pip freeze > requirements.txt` : Sauvegarder la liste des bibliothèques pour GitHub.
* `pip install -r requirements.txt` : Réinstaller toutes les bibliothèques d'un coup (sur un nouveau PC).

### Créer un .venv
1. `python -m venv .venv` (Créer)
2. `.\.venv\Scripts\activate` (Activer sur Windows)

---