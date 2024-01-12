import os
from pathlib import Path

path_os = os.getcwd()
path_Path = Path.cwd()

# print(type(path_os))
# print(type(path_Path))

print(path_Path)
print(path_Path.name)

path = Path('test/expenses.txt')
print(path)
print(path.parts)
print(path.name)
print(path.stem)
print(path.suffix)
