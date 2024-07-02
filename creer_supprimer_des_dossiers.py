from pathlib import Path
import shutil

p = Path.home()



p = p / "DossierTest"



p.mkdir(exist_ok=True)

p = p / "1" / "2" / "3"

p = p / "readme.txt"

p.touch()  # créer file

p.unlink()  # supprimer file

p = p.parent

p.rmdir() # supprimer dir

p = p.parent.parent.parent
shutil.rmtree(p) # supprimer un dossier qui contient du contenu


print(p)
