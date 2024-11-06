from setuptools import setup, find_packages

# Lire les dépendances depuis le fichier requirements.txt
with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="radiomics_extractor",
    version="1.0.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "radiomics-gui=frontend.gui:main",  # Lancer l'interface GUI à partir de la ligne de commande
        ],
    },
    author="Remy LALUC",
    author_email="remy.laluc@reims.unicancer.fr",
    description="Un outil pour l'extraction des paramètres radiomiques à partir d'images médicales au format .nrrd.",
    license="MIT",
    keywords="radiomics medical image processing",
    url="https://github.com/Lalucarne51/radiomics_extractor",  # Remplacez par votre URL GitHub
)
