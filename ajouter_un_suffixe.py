from pathlib import Path

p = Path.cwd() / "text.txt"
p.touch()
#print(p)

p2 = p.parent / (p.stem + "-lowres" + p.suffix)

# C:\Users\Bazinga\Documents\python_2024\formation_python_2\text-lowres.txt

print(p2)