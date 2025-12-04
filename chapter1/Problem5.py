import os

def list_directory_contents(path="/"):
    # """
    # Print all files and directories in the given path.
    # :param path: Directory path (defaults to current directory)
    # """
    try:
        entries = os.listdir(path)
    except (FileNotFoundError, NotADirectoryError, PermissionError) as e:
        print(f"Error accessing directory '{path}': {e}")
        return

    print(f"Contents of directory '{path}':")
    for name in entries:
        print(name)

if __name__ == "__main__":
    # You can change the path to the directory you want
    dir_path = input("Enter directory path (or press Enter for current directory): ").strip() or "."
    list_directory_contents(dir_path)