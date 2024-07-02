from pathlib import Path

"""
La méthode iterdir() de la classe Path dans la bibliothèque pathlib est utilisée pour
itérer sur les éléments d'un répertoire. Elle retourne un itérateur sur les objets
Path représentant les fichiers et les sous-répertoires dans le répertoire spécifié.
"""

Path.cwd().iterdir()

#for file in Path.cwd().iterdir():
    #print(file.name)

p = [file for file in Path.cwd().iterdir() if file.is_dir()]
p1 = [file for file in Path.cwd().iterdir() if file.is_file()]
print(p)
print(p1)

