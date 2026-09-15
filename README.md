# TP OOP

Ce dépôt contient les exercices du TP d'introduction à la programmation
orientée objet en Python. Les exemples portent sur la manipulation de tuples,
d'ensembles et de dictionnaires, ainsi que sur la remise au propre d'une
fonction.

## Contenu de `tp0/`

| Fichier | Contenu |
| --- | --- |
| [`tuples.py`](tp0/tuples.py) | Manipulation du journal de bord d'un robot : affichage d'un relevé et recalibrage d'un capteur. |
| [`ensembles.py`](tp0/ensembles.py) | Opérations sur les ensembles de robots : missions communes, union, robots affectés à une seule mission, ajout et retrait. |
| [`dictionnaires.py`](tp0/dictionnaires.py) | Gestion d'un stock de pièces détachées par modèle de robot. |
| [`qualite.py`](tp0/qualite.py) | Version propre de la fonction de calcul du coût d'un déplacement selon le terrain. |
| [`test.py`](tp0/test.py) | Tests unitaires `unittest` pour le recalibrage, les ensembles et l'inventaire. |

## Prérequis

- Python 3.11 ou une version compatible avec Python 3 ;
- aucune bibliothèque externe n'est nécessaire pour exécuter les exemples et
  les tests.

Le dépôt fournit également un environnement Conda reproductible dans
[`environment.yml`](environment.yml).

## Installation de l'environnement Conda

Si Conda est installé, créez l'environnement à partir du fichier fourni :

```bash
conda env create -f environment.yml
conda activate tp_oop
```

## Lancer les fichiers du TP

Depuis la racine du dépôt, exécutez un fichier avec Python :

```bash
python3 tp0/tuples.py
python3 tp0/ensembles.py
python3 tp0/dictionnaires.py
python3 tp0/qualite.py
```

Ces fichiers contiennent des exemples et des assertions. Une exécution sans
message d'erreur indique que leurs vérifications intégrées sont satisfaites.

## Lancer les tests unitaires

Pour exécuter tous les tests définis dans `tp0/test.py` :

```bash
python3 -m unittest tp0.test -v
```

Ou, depuis le dossier `tp0/` :

```bash
cd tp0
python3 -m unittest test -v
```

Le fichier de tests vérifie notamment que `recalibrer` :

- remplace la valeur du capteur demandé en conservant son unité ;
- laisse les autres relevés inchangés ;
- conserve la liste d'origine et renvoie une nouvelle liste ;
- ne modifie rien lorsque le capteur demandé est absent.