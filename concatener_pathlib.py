from pathlib import Path

"""
Pour concaténer des chemins de fichiers ou de répertoires avec pathlib, vous pouvez utiliser l'opérateur /,
qui rend le code plus lisible et plus intuitif que les méthodes traditionnelles. Voici comment faire :
"""

p = Path.home()

p1 = p / "Documents" / "python_2024"

# C:\Users\Bazinga\Documents\python_2024


# Exemple de concaténation de chemins avec pathlib


base_path = Path('/some/directory')
sub_directory = 'subdir'
file_name = 'file.txt'

# Concaténer les chemins
full_path = base_path / sub_directory / file_name

# Affiche /some/directory/subdir/file.txt


"""
Exemple pratique
Imaginons que vous vouliez créer une structure de répertoires et y ajouter un fichier.
Voici comment vous pourriez procéder :
"""

# Chemin de base


base_path = Path('/some/directory')

# Concaténation pour créer un chemin complet

subdir_path = base_path / 'subdir'
file_path = subdir_path / 'file.txt '

# Créer le sous-répertoire

subdir_path.mkdir(parents=True, exist_ok=True)

# écrire dans le fichier

file_path.write_text('Contenu du fichier')

"""
Autres opérations courantes avec pathlib
Obtenir le chemin absolu
Pour obtenir le chemin absolu d'un fichier ou d'un répertoire :

"""
absolute_path = file_path.resolve()

print(absolute_path)

"""
Joindre plusieurs chemins de manière dynamique
Vous pouvez également joindre plusieurs chemins de manière dynamique en utilisant une boucle :
"""

paths = ["folder1", "folder2", "folder3"]

base_path = Path("/some/directory")

for folder in paths:
    base_path /= folder

#  # Affiche /some/directory/folder1/folder2/folder3


"""
Avantages de cette méthode

Lisibilité : Utiliser l'opérateur / pour concaténer les chemins est beaucoup plus lisible que d'utiliser
 des chaînes de caractères et des opérateurs de concaténation traditionnels.

Sécurité : pathlib gère automatiquement les séparateurs de chemin en fonction du système d'exploitation,
ce qui réduit les erreurs.

Flexibilité : Les objets Path offrent de nombreuses méthodes pratiques pour manipuler les chemins,
ce qui simplifie beaucoup de tâches courantes en gestion de fichiers.


Avec pathlib, la manipulation et la concaténation des chemins deviennent à la fois plus simples
et plus robustes, ce qui en fait un outil incontournable pour tout développeur Python.

"""

# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------

# joinpath

"""
La méthode joinpath est une autre manière de concaténer les chemins de fichiers ou de répertoires, 
et elle est équivalente à l'utilisation de l'opérateur /.
"""
# chemin de base
base_path = Path('/some/directory')

# utilisation de joinpath pour concaténer les chemins

full_path = base_path.joinpath("subdir", "file.txt")

print(file_path)

# \some\directory\subdir\file.txt

# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------

pa = Path("C:/Users/Bazinga/Documents/python_2024/formation_python_2/write.txt")

print(pa.name)  # write.txt
print(pa.parent)  # C:\Users\Bazinga\Documents\python_2024\formation_python_2
print(pa.stem)  # write
print(pa.suffix)  # .txt
print(pa.suffixes)  # ['.txt']
print(pa.parts)  # ('C:\\', 'Users', 'Bazinga', 'Documents', 'python_2024', 'formation_python_2', 'write.txt')
print(pa.exists())  # True
print(pa.is_dir())  # False
print(pa.is_file())  # True
print(pa.parent.parent)
print(dir(pa))



