
# Challenge Triple A

## Description

Le Challenge Triple A consiste à développer un outil simple de
monitoring avec un dashboard web qui affiche en temps réel les statistiques
d'une machine virtuelle Linux. Ce projet fait appel à trois compétences précises :

- Administration : Gestion d'une machine virtuelle Linux
- Algorithmique : Développement Python pour la collecte de données système
- Affichage : Création d'une interface web avec HTML5/CSS3

Le script Python collecte différentes informations système (CPU, mémoire, processus, fichiers) et génère automatiquement un fichier `index.html` à partir d’un template HTML.

## Prérequis

- Une machine Linux, Windows ou macOS
- Python 3
- Git
- Un navigateur web moderne

## Installation


### 1. Cloner le projet

```bash
git clone https://github.com/lorenzo-brissardnavarro/AAA.git
cd AAA
```

### 2. Installer Python 3

#### Sous Linux (Debian / Ubuntu)

```bash
sudo apt update
sudo apt install python3 python3-pip
```

#### Sous macOS (via Homebrew)

```bash
brew install python
```

#### Sous Windows

Télécharger et installer Python 3 depuis le site officiel : [https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/)

### 3. Installer la bibliothèque `psutil`

#### Sous Linux / macOS

```bash
pip3 install psutil
```

#### Sous Windows

```bash
pip install psutil
```

## Utilisation

### Lancer le script de monitoring

#### Depuis le dossier du projet, exécuter : 

```bash
python3 monitor.py
```

#### ou sous Windows : 

```bash
python monitor.py
```

### Ouvrir le dashboard dans le navigateur

Ouvrir le fichier `index.html` dans un navigateur web :

- Double-clic sur le fichier
ou
- Clic droit → Ouvrir avec → navigateur

Le tableau de bord affiche alors les données collectées.

## Fonctionnalités
 
### Informations processeur

- Nombre de cœurs
- Fréquence actuelle du CPU
- Pourcentage d’utilisation du CPU

### Mémoire

- Mémoire utilisée (en Go)
- Mémoire totale (en Go)
- Pourcentage d’utilisation de la RAM

### Système

- Nom de la machine
- Système d’exploitation et version
- Date et heure de démarrage
- Temps de fonctionnement (uptime)
- Adresse IP
- Nombre d’utilisateurs connectés

### Processus

- Liste des processus consommant du CPU
- Liste des processus consommant de la mémoire
- Top 3 des processus les plus gourmands en CPU

### Analyse de fichiers

- Analyse d’un dossier spécifique :

```bash
/home/projetubuntu/Documents
```
- Nombre total de fichiers
- Comptage et pourcentage des fichiers :
  - .txt
  - .py
  - .pdf
  - .jpg

## Captures d'écran


## Difficultées rencontrées

- Compréhension et prise en main de la bibliothèque `psutil`
- Maintien de la lisibilité du dashboard malgré un volume important d’informations
- Récupération de l’adresse IP correcte sur des machines disposant de plusieurs interfaces réseau

## Améliorations possibles

- Sélection dynamique du dossier à analyser
- Historique des statistiques système
- Export des données collectées (CSV ou JSON)

## Auteurs

- Killian Fourré-Boulay
- Florian Gelin
- Lorenzo Brissard-Navarro