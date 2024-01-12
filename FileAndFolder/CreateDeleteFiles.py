from pathlib import Path
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Create files .txt
for i in numbers:
    with open(f"test{i}.txt", "w") as file:
        file.write("Hello World")

# Delete files .txt
for path in Path(".").glob("*.txt"):
    path.unlink()

# Delete files .txt except test9.txt
for path in Path(".").glob("test[1-8].txt"):
    path.unlink()