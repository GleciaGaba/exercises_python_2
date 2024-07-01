chemin = r"C:\Users\Bazinga\Documents\python_2024\formation_python_2\python_est_un_super.txt"

"""Première manière d'ouvrir un fichier : en utilisant 
la fonction open comme ceci, il faut systématiquement utiliser la fonction close pour fermer le fichier."""

f = open(chemin, "r")
f.close()

print(f)

"""Deuxième manière d'ouvrir un fichier : avec with, vous n'avez plus besoin 
de fermer le fichier derrière. Il se ferme tout seul."""

"""
La méthode with open est utilisée pour ouvrir un fichier et garantir qu'il est correctement fermé après
avoir été utilisé, même si une exception se produit. Cela permet de gérer les fichiers de manière plus
sûre et plus propre qu'avec une simple ouverture de fichier.

Voici une explication détaillée de son fonctionnement :

Syntaxe de base
python
Copier le code"""
# Opérations sur le fichier

"""
with open('nom_du_fichier', 'mode') as fichier:
    # opérations sur le fichier
    contenu = fichier.read()

"""



# nom_du_fichier : le chemin du fichier que vous souhaitez ouvrir.
# mode : le mode d'ouverture du fichier. Les modes les plus courants sont :

# 'r' : lecture (par défaut).
# 'w' : écriture (le contenu existant sera écrasé).
# 'a' : ajout (le nouveau contenu sera ajouté à la fin du fichier).
# 'b' : mode binaire (peut être ajouté à d'autres modes, par exemple 'rb' pour lecture binaire).


chemin1 = r"C:\Users\Bazinga\Documents\python_2024\formation_python_2\python_est_un_super.txt"

with open(chemin1) as f:
    contenu = f.read()
    print(contenu)

# output

"""
Python
est
un
super
langage 
de 
programmation
"""

chemin2 = r"C:\Users\Bazinga\Documents\python_2024\formation_python_2\python_est_un_super.txt"

with open(chemin2) as f:
    contenu2 = repr(f.read())
    print(contenu2)

# 'Python\nest\nun\nsuper\nlangage \nde \nprogrammation\n' --- il ajoute \n pour montrer les retour à ma ligne

chemin3 = r"C:\Users\Bazinga\Documents\python_2024\formation_python_2\python_est_un_super.txt"

with open(chemin) as f:
    contenu3 = f.readlines()
    print(contenu3)

# ['Python\n', 'est\n', 'un\n', 'super\n', 'langage \n', 'de \n', 'programmation\n']
# readlines() fonction va creer une liste avec le contenu et representation du fichier.

chemin4 = r"C:\Users\Bazinga\Documents\python_2024\formation_python_2\python_est_un_super.txt"

with open(chemin4, "r") as f:
    contenu4 = f.read().splitlines()
    print(contenu4)

# ['Python', 'est', 'un', 'super', 'langage ', 'de ', 'programmation']
# splitlines() va creer un miste sans la representation de retour à la ligne \n


"""
Note:
Il se peut que sur Windows, vous ayez certains problèmes d'encodage quand vous ouvrez un fichier.

Pour résoudre ces problèmes, vous devez ajouter encoding = 'utf-8' lors de l'ouverture du fichier avec la fonction open:

"""
chemin5 = r"C:\Users\Bazinga\Documents\python_2024\formation_python_2\python_est_un_super.txt"
with open(chemin5, "r", encoding="utf-8") as f:
    contenu5 = f.read()


# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------

# Avec write on peut écrire à l'interieur des fuchiers

chemin6 = r"C:\Users\Bazinga\Documents\python_2024\formation_python_2\write.txt"

# "w" --> writer
# "a" --> append

with open(chemin6, "w") as f:
    f.write("Bonjour")
    f.write("\nAu revoir")
    print(f)

with open(chemin6, "a") as g:
    g.write("\nBonsoir")
    g.write("\nTchau")
    print(f)




# --------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------

chemin7 = r"C:\Users\Bazinga\Documents\python_2024\formation_python_2\python_est_un_super.txt"
with open(chemin7, 'r') as fichier:
    contenu = fichier.read()
    print(contenu)


# --------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------

chemin8 = r"C:\Users\Bazinga\Documents\python_2024\formation_python_2\python_est_un_super.txt"

with open(chemin8, "w") as fichier:
    contenu8 = fichier.write("Bom bia amiguinhos!")
    contenu8 = fichier.write("\nBom bia!")
    print(contenu8)

# --------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------

""" Gestion automatique des ressources: le fichier est automatiquement fermé à la fin du bloc 'with', 
même si une exception est levée"""



# --------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------


# Exemples avancés

# Lecture ligne par ligne

with open('mon_fichier.txt', 'r') as fichier:
    for ligne in fichier:
        print(ligne.strip())

# écriture de multiples lignes

ligne = ["Première ligne\n", "Deuxième ligne\n", "Trisième ligne\n"]
with open("mon_fichier.txt", "w") as fichier:
    fichier.writelines(ligne)



# --------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------






