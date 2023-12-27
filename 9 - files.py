with open("file.txt", "r") as file:
    print(file.read())

with open("output.txt", "w") as file:
    file.write("This has been written to a file")

with open("file.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())

# File paths

import os
full_path = os.path.join("my_package", "some_random_file.txt")
print(full_path)

from pathlib import Path
path = Path("my_package") / "some_random_file.txt"
print(path)

try:
    with open("non-existent-file.txt", "r") as file:
        file.read()
except FileNotFoundError:
    print("File not found")
except Exception as e:
    print(f"Something went wrong: {e}")