# Mémo Git - Commandes Utiles

Ce fichier contient les commandes essentielles pour utiliser ce dossier sur GitHub.

## Sauvegarder son travail
À faire à la fin de chaque séance ou dès qu'une étape est terminée :

1. **Préparer les fichiers** : `git add .`
2. **Créer la sauvegarde** : `git commit -m "Mon message ici"`
3. **Envoyer sur GitHub** : `git push`

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

### Nettoyer un .venv corrompu
1. Supprimer le dossier `.venv` à la main.
2. `python -m venv .venv` (Recréer)
3. `.\.venv\Scripts\activate` (Activer sur Windows)

---

## Erreurs Classiques
* **"Fatal: origin already exists"** : L'adresse est déjà configurée, utilise `set-url` au lieu de `add`.
* **"Everything up-to-date"** : Tu as oublié de faire `git add` ou `git commit` avant le `push`.
* **"Fatal error in launcher"** : Ton `.venv` a été déplacé, il faut le supprimer et le recréer.

## Astuces VS Code (Markdown)

* **Voir l'aperçu du README** : `Ctrl` + `Shift` + `V`
* **Ouvrir l'aperçu sur le côté (Split View)** : `Ctrl` + `K` puis `V` 
  *(Pratique pour écrire à gauche et voir le résultat à droite !)*