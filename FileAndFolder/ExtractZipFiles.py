from pathlib import Path
import zipfile

source_directory = Path(".")
target_directory = Path("temp")

for path in source_directory.glob("*.zip"):
    print(path)
    with zipfile.ZipFile(path, "r") as zip_obj:
        zip_obj.extractall(path=target_directory)