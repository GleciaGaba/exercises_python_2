from pathlib import Path

"""
La librairie pathlib est un module de la bibliothèque standard de Python qui fournit une 
interface orientée objet pour travailler avec les chemins de fichiers et de répertoires.
Introduite dans Python 3.4, elle simplifie la manipulation des chemins de fichiers par 
rapport aux modules plus anciens comme os et os.path.

"""

"""
Classe principale Path :
La classe Path est au cœur de pathlib. Elle permet de manipuler les 
chemins de manière intuitive. Les instances de Path peuvent représenter
des chemins de fichiers ou de répertoires.
"""
p = Path('/some/directory')

p1 = Path.home()

# C:\Users\Bazinga

p2 = Path.cwd()

# 2:\Users\Bazinga\Documents\python_2024\formation_python_2


"""
Manipulation des chemins :
pathlib permet de manipuler facilement les chemins, par exemple pour accéder aux parents,
nom de fichier, suffixe, etc.
"""


p3 = Path('/some/directory/file.txt')
print(p3.parent)  # /some/directory
print(p3.name)    # file.txt
print(p3.suffix)  # .txt


"""
Création, suppression et vérification :
Vous pouvez créer des répertoires, des fichiers, et vérifier leur existence.

"""

p4 = Path('/some/directory')

# Créer un répertoire
p4.mkdir(parents=True, exist_ok=True)

# Vérifier l'existence
print(p4.exists())  # True ou False

# Supprimer un fichier
file_path = p4 / 'file.txt'
file_path.unlink()


"""
Itération sur les fichiers :
pathlib permet d'itérer sur les fichiers dans un répertoire de manière élégante.
"""

for file in p.iterdir():
    print(file)

"""
Lecture et écriture de fichiers :
Il est possible de lire et écrire des fichiers directement avec pathlib.

"""

# Lire un fichier
content = file_path.read_text()

# Écrire dans un fichier
file_path.write_text('Nouveau contenu')


""" 
Exemple pratique
Voici un exemple pratique montrant comment utiliser pathlib pour rechercher tous les fichiers .
txt dans un répertoire et ses sous-répertoires, puis lire leur contenu.
"""

from pathlib import Path

# Chemin de base
base_path = Path('/some/directory')

# Rechercher tous les fichiers .txt
txt_files = base_path.rglob('*.txt')

# Lire le contenu de chaque fichier
for txt_file in txt_files:
    print(f'Contenu de {txt_file.name}:')
    print(txt_file.read_text())
    print('---')