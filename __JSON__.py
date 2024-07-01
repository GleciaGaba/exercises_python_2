import json

"""
Pour ouvrir et manipuler des fichiers JSON en Python en utilisant la méthode 'with open', vous utiliserez également
le module 'json' pour lire et écrire de données en format JSON
"""

# Ex: écrire de données dans un fichier JSON avec
chemin = r"C:\Users\Bazinga\Documents\python_2024\formation_python_2\fichier.json"

with open(chemin, "w") as f:
    json.dump(list(range(10)), f, indent=4)

# ex 1:
chemin = r"C:\Users\Bazinga\Documents\python_2024\formation_python_2\fichier.json"

donnees = {
    "non": "Jean",
    "age": 30,
    "ville": "Paris"
}

with open(chemin, 'w') as fichier:
    json.dump(donnees, fichier, indent=4)

# --------------------------------------------------------------------------------------------------------------------

# Ex: lire de donées dans un fichier JSON
chemin1 = r"C:\Users\Bazinga\Documents\python_2024\formation_python_2\fichier.json"
with open(chemin1, "r") as f:
    liste = json.load(f)
    print(liste)

# EX 1: Lire avec load

chemin2 = r"C:\Users\Bazinga\Documents\python_2024\formation_python_2\fichier.json"

with open(chemin2, "r") as fichier:
    donnees = json.load(fichier)
    print(donnees)

# Note: c'est aussi possible de créer un fichier (ou de l'écraser s'il existe déjà un fichier avec le même nom).

donnees1 = {
    "non": "Jean",
    "age": 30,
    "ville": "Paris"
}

with open("fichier_json.json", 'w') as fichier:
    json.dump(donnees, fichier, indent=4)


"""
Note : Chaque fois que l'on utilise le mode 'w' avec la méthode dump,
on écrase les données déjà existantes, comme si l'on créait un nouveau fichier JSON.
Il est possible d'avoir un seul JSON par fichier, mais ce JSON peut contenir plusieurs objets à l'intérieur.

Nous serons donc tentés d'utiliser le mode 'a' pour ajouter,
mais 'a' va créer un deuxième objet de type JSON à l'intérieur d'un fichier,
ce qui n'est pas possible car un fichier ne peut contenir qu'un seul JSON valide.
"""
# --------------------------------------------------------------------------------------------------------------------
# Gestion des erreus:

"""
1ère erreur :

Il n'est pas possible de lire un fichier JSON vide. Il faut donc écrire quelque 
chose dans le fichier JSON avant d'essayer de le lire avec read().
Le plus simple est d'écrire une liste vide ou une chaîne de caractères vide.
"""
with open('donnees.json', 'w') as fichier:
    json.dump([], fichier)


"""
2ème erreur :
Quand on doit écrire quelque chose à l'intérieur du fichier JSON qui contient des caractères spéciaux,
 il faut s'assurer que ces caractères sont correctement échappés pour éviter des erreurs de syntaxe JSON.

"""

donnees = {
    "message": "Bonjour, c'est un test avec des caractères spéciaux : é, è, à, &, \" et '",
    "utilisateur": "Jean \"L'utilisateur\" Dupont",
    "chemin": "C:\\Utilisateurs\\Jean\\Documents"
}

# Écrire les données dans un fichier JSON
with open('donnees_speciales.json', 'w') as fichier:
    json.dump(donnees, fichier, ensure_ascii=False, indent=4)


# pour éviter les erreurs causés par les caractères spéciaux il faut ajouter l'option ensure_ascii = False.

"""
Echappement automatique : La fonction json.dump() 
gère automatiquement l'échappement des caractères spéciaux pour garantir que le fichier JSON reste valide.
Option ensure_ascii : L'option ensure_ascii=False permet de conserver les caractères spéciaux non-ASCII 
dans le fichier, ce qui est utile pour les caractères accentués.

"""