from pathlib import Path

p = Path.cwd() / "Pathlib"

p = p / "readme.txt"

p.touch()

p.write_text("Bonjour")

pa = p.read_text()


print(pa)



