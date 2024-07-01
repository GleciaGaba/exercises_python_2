import json

"""
Note : Chaque fois que l'on utilise le mode 'w' avec la méthode dump,
on écrase les données déjà existantes, comme si l'on créait un nouveau fichier JSON.
Il est possible d'avoir un seul JSON par fichier, mais ce JSON peut contenir plusieurs objets à l'intérieur.

Nous serons donc tentés d'utiliser le mode 'a' pour ajouter,
mais 'a' va créer un deuxième objet de type JSON à l'intérieur d'un fichier,
ce qui n'est pas possible car un fichier ne peut contenir qu'un seul JSON valide.
"""

with open("ajouter_fichier.json", 'w') as fichier:
    json.dump([1, 2, 3], fichier, indent=4)

"""with open("ajouter_fichier.json", 'a') as fichier:
    json.dump([4], fichier, indent=4)"""


# --------------------------------------------------------------------------------------------------------------------

# Si on veux écrire des donées dans un même fichier JSON, il faut les écrire à l'interieu du objet json.

with open("ajouter_fichier.json", "r") as fichier:
    result = json.load(fichier)
result.append(4)
result.extend([5, 6, 7])

with open("ajouter_fichier.json", "w") as fichier:
    json.dump(result, fichier, indent=4)


"""Il faut donc d'abord récupérer les données en mode lecture "r" avec load(),
 puis ajouter les nouvelles données en utilisant la méthode append."""



