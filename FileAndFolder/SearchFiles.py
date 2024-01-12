from pathlib import Path

folder = Path("2024")
search_text = "202401"

for path in folder.glob("**/*.csv"):
    if search_text in path.name:
        print(path)
        print(path.absolute())
