import os

path = os.path.join("..", "03_file_writer", "another_file_to_remove.txt")


try:
    os.remove(path)
except FileNotFoundError:
    print("File already deleted.")

