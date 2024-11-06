Description

Radiomics Extractor Tool est un outil Python permettant d'extraire des caractéristiques radiomiques depuis des volumes médicaux au format .nrrd en utilisant des masques d'intérêt ROI (également au format .nrrd). Le projet comprend une interface graphique simple qui permet aux utilisateurs de charger un fichier CSV, sélectionner les catégories de caractéristiques radiomiques à extraire, visualiser les résultats dans un tableau, et exporter ces résultats au format CSV.

Cet outil est particulièrement utile pour les chercheurs en radiologie ou en imagerie médicale qui souhaitent automatiser l'extraction des caractéristiques radiomiques sans avoir à manipuler des fichiers complexes directement depuis le terminal.

Fonctionnalités

Chargement des images et des masques au format .nrrd.
Extraction des caractéristiques radiomiques à l'aide de la bibliothèque PyRadiomics.
Sélection des catégories de caractéristiques radiomiques (firstorder, glcm, gldm, glrlm, glszm, ngtdm, shape).
Affichage des résultats sous forme de tableau scrollable dans l'interface.
Exportation des résultats dans un fichier CSV.
Redimensionnement des masques pour correspondre aux dimensions de l'image.
Messages d'erreurs et de succès affichés dans l'interface pour guider l'utilisateur lors de l'extraction.

Prérequis

Avant d'installer le projet, assurez-vous d'avoir les éléments suivants installés sur votre machine :

Python 3.6 ou supérieur
Git
Pip

Installation

1. Cloner le dépôt GitHub
Clonez le projet sur votre machine locale à l'aide de Git.

git clone git@github.com:Lalucarne51/radiomics_extractor.git
cd radiomics_extractor

2. Installer les dépendances
Toutes les dépendances du projet sont répertoriées dans le fichier requirements.txt. Installez-les en exécutant la commande suivante dans le répertoire du projet :

pip install -r requirements.txt

3. Installation du package
Pour rendre le projet exécutable sur votre machine locale, installez le package en local :

pip install .
Cela installera toutes les dépendances et rendra le package utilisable avec l'interface graphique.

Utilisation

Interface graphique
Exécutez le programme avec la commande suivante :
python -m main.py

Dans l'interface, vous pouvez :

Charger un fichier CSV : Sélectionnez un fichier CSV contenant les associations entre les images et les masques. Le CSV doit avoir deux colonnes : Image et Mask.
Sélectionner les catégories de caractéristiques : Cochez les catégories de caractéristiques radiomiques que vous souhaitez extraire (firstorder, glcm, gldm, etc.).
Lancer l'extraction : Cliquez sur le bouton pour extraire les caractéristiques radiomiques. Les résultats seront affichés dans un tableau.
Exporter les résultats : Utilisez le bouton d'exportation pour sauvegarder les résultats dans un fichier CSV.

Exemple de fichier CSV
Le fichier CSV en entrée doit avoir deux colonnes avec des chemins absolus vers les images et les masques respectifs :

Image,Mask
/home/user/images/image1.nrrd,/home/user/masks/mask1.nrrd
/home/user/images/image2.nrrd,/home/user/masks/mask2.nrrd
