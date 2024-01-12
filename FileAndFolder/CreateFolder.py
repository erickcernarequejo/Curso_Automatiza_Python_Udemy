from pathlib import Path
import re

# Path('new_dir').mkdir()
# Path('new_dir').mkdir(exist_ok=True)

# Path('new_dir/new_sub_dir/new_dir').mkdir(parents=True, exist_ok=True)

# Rename folder name
# path = Path('new_dir')
# path.rename('new_test')

# Rename file within a folder
# path = Path('new_test/sales.csv.txt')
# newNameFile = path.with_name('purchase.txt')
# path.rename(newNameFile)
# print(newNameFile)

# Get paths from subdirectories
folder = Path('2024')
# for path in list(folder.iterdir()):
#     print(path)

# Get paths from all subdirectories
paths = folder.glob('**/*')
# for path in paths:
#     print(path)

# Get paths from all subdirectories with file
# for path in paths:
#     if path.is_file():
#         print(path)

# Get paths from all subdirectories with file .py
# folder = Path('.')
# for path in folder.glob('**/*.py'):
#     print(path)

# Rename sales.csv.csv to format
folder = Path('2024')
paths = folder.glob('**/*.csv')

for path in paths:
    print(path.parts)
    year = path.parts[0]
    month = path.parts[1]
    day = path.parts[2]
    day_number = int(re.findall(r'\d+', day)[0])
    month_number = int(re.findall(r'(\d+).', month)[0])

    newFolder = path.with_name(f'sales{year}{month_number:02d}{day_number:02d}.csv')
    path.rename(newFolder)
