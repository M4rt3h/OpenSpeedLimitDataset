# OpenSpeedLimitDataset

Dataset de panneaux de limitation de vitesse (15–90 km/h) pour les tâches de vision par ordinateur et de conduite autonome, notamment dans le simulateur CARLA.

## Aperçu
- **Contenu :** Images réelles et synthétiques de panneaux de 15 à 90 km/h, issues de plusieurs pays et environnements.
- **Objectif :** Fournir un jeu de données simple couvrant spécifiquement les limitations de vitesse, combinant plusieurs sources pour améliorer la diversité et la robustesse des modèles.

## Structure des classes
Les dossiers ou identifiants de classes sont structurés selon la correspondance suivante :
- `0` : 15 km/h  
- `1` : 20 km/h  
- `2` : 30 km/h  
- `3` : 40 km/h  
- `4` : 50 km/h  
- `5` : 60 km/h  
- `6` : 70 km/h  
- `7` : 80 km/h  
- `8` : 90 km/h  

## Cas d'utilisation
- Détection de panneaux de vitesse et classification d'images.
- Entraînement de modèles de vision (YOLO, RT-DETR, etc.).
- Expériences en conduite autonome et tests dans CARLA (mon cas d'utilisation).

## Sources
- [Traffic Signs Dataset](https://www.kaggle.com/datasets/tuanai/traffic-signs-dataset)
- [GTSRB (Roboflow Universe)](https://universe.roboflow.com/gtsrbanno/traffic-sign-detection-gtsrb)
- [CARLA Traffic Signs Images](https://www.kaggle.com/datasets/sachsene/carla-traffic-signs-images)
- [Mapillary](https://www.mapillary.com/) (collecte manuelle complémentaire)

## Préparation des données (`convert.py`)
Script Python (basé sur `pathlib` et `Pillow`) pour homogénéiser les sources du dataset avant annotation ou entraînement :
- Conversion automatique des images (`.jpg`, `.jpeg`, `.ppm`) en `.png`.
- Renommage séquentiel et sans conflit garantissant une structure propre et reproductible dans chaque dossier.

## Licence et crédits
Les données proviennent de sources externes. Chaque jeu de données reste la propriété de ses auteurs respectifs, dont les licences d'origine doivent être respectées.