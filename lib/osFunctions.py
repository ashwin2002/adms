from os import makedirs


def create_dir(dir_path):
    if type(dir_path) is str:
        makedirs(dir_path, exist_ok=True)
    elif type(dir_path) is list:
        for dirName in dir_path:
            makedirs(dirName, exist_ok=True)
