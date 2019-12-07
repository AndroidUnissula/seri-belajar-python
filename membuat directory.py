import os

def buatFolder(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)

buatFolder("nama_directory/")