from os import path, walk, listdir
import shutil


root_dir = 'my_project'



for root, dirs, files in walk(root_dir):
    if 'templates' in dirs and root != root_dir:
        for f in listdir(path.join(root, 'templates')):
            shutil.copytree(path.join(root, 'templates', f), path.join(root_dir, 'templates', f))
