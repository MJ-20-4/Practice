import os
from pathlib import Path

# Check if a file exists
if os.path.exists("data.txt"):
    print("File found!")

# Modern way using pathlib
p = Path("data.txt")
if p.exists():
    print("Found it!")
    p.unlink()  # Deletes the file
