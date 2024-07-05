"""
On peut également utiliser la méthode joinpath sur un objet Path.
Ça peut être pratique si vous avez par exemple une liste de dossiers que vous
souhaitez concaténer (grâce à l'unpacking et à l'opérateur splat *) :

"""

from pathlib import Path

home = Path.cwd()
dossier = ["Projets", "Django", "blog"]

result = home.joinpath(*dossier)

print(result)
