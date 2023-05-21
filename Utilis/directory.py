import os


def make_directory(path):
    directory_exists = os.path.exists(path)
    if not directory_exists:
        os.makedirs(path)
