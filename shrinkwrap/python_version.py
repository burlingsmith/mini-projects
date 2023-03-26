import os
import subprocess

TARGET_SIZE = 1000000   # Specify the target size in bytes
DIRECTORY = "/path/to/starting/directory"   # Specify the starting directory

def choose_directory(dir_path, size):
    """
    Recurse through subdirectories until finding a directory smaller than TARGET_SIZE,
    then choose either that directory or its parent directory, depending on which is
    closer to TARGET_SIZE.

    Args:
        dir_path (str): The path to the directory to start the search from.
        size (int): The size of the directory in bytes.

    Returns:
        str: The path to the chosen directory.
    """
    parent_size = os.path.getsize(os.path.dirname(dir_path))
    if size <= TARGET_SIZE:
        if size >= parent_size - size:
            return os.path.dirname(dir_path)
        else:
            return dir_path
    chosen_dir = ""
    chosen_size = 0
    for sub_dir in os.listdir(dir_path):
        sub_dir_path = os.path.join(dir_path, sub_dir)
        if os.path.isdir(sub_dir_path):
            sub_size = os.path.getsize(sub_dir_path)
            if sub_size < size:
                if not chosen_dir or size - sub_size < size - chosen_size:
                    chosen_dir = sub_dir_path
                    chosen_size = sub_size
    if not chosen_dir:
        return os.path.dirname(dir_path)
    else:
        return choose_directory(chosen_dir, chosen_size)

def compress_and_remove(dir_path):
    """
    Compress a directory to .7z format and remove the original directory.

    Args:
        dir_path (str): The path to the directory to compress.
    """
    print(f"Compressing directory: {dir_path}")
    subprocess.run(["7z", "a", f"{dir_path}.7z", dir_path], check=True)
    subprocess.run(["rm", "-rf", dir_path], check=True)

def process_directory(dir_path):
    """
    Recurse through subdirectories of a directory, choose a directory to compress,
    and then compress it and remove the original directory.

    Args:
        dir_path (str): The path to the directory to process.
    """
    size = os.path.getsize(dir_path)
    chosen_dir = choose_directory(dir_path, size)
    compress_and_remove(chosen_dir)

for dir_path, _, _ in os.walk(DIRECTORY):
    process_directory(dir_path)
    