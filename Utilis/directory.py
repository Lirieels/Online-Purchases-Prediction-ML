import os


def make_directory(path):
    directory_exists = os.path.exists(path)
    if not directory_exists:
        os.makedirs(path)


def list_files(path):
    files = os.listdir(path)
    files = [f for f in files if os.path.isfile(path+'/'+f)]
    return files


def directory_exists(path):
    directory_exists = os.path.exists(path)
    return directory_exists
