# Change txt extension to csv
from pathlib import Path

folder = Path('change-extension')
folder.mkdir(parents=True, exist_ok=True)

for i in range(1, 11):
    nameFile = folder/f'file{i}.txt'
    nameFile.touch()

# 1. txt -> csv
for path in list(folder.iterdir()):
    if path.suffix == ".txt":
        newExtension = path.with_suffix(".csv")
        path.rename(newExtension)

# 1. csv -> txt
for path in folder.glob("**/*.csv"):
    newExtensionCSV = path.with_suffix(".txt")
    path.rename(newExtensionCSV)
