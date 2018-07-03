from os import makedirs

def createDir (dirPath):
    if type(dirPath) is str:
        makedirs (dirPath, exist_ok=True)
    elif type(dirPath) is list:
        for dirName in dirPath:
            makedirs (dirName, exist_ok=True)
    return
