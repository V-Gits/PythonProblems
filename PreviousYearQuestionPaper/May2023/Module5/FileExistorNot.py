"""
Write a Python code that checks to see, if a file with the given pathname exists
on the disk, before attempting to open a file for input.
"""

import os

file_path = "example.txt"

if os.path.exists(file_path):
    with open(file_path, "r") as file:
        content = file.read()
        print("File Content:\n", content)
else:
    print("Error: File does not exist.")
