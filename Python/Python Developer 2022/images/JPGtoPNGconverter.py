"""
Mod! Source Folder, Destination Folder
"""

import sys
import os
from PIL import Image

folders = sys.argv[1:]
if len(folders) == 0:
    folders = ['pokedex/', 'new/']


def checkFolders(folders):
    result = []
    for n in range(2):
        result.append(os.path.isdir(os.path.join(os.getcwd(), folders[n])))

    if result[0] == False:
        print('Source folder not found, good bye!')
        exit()

    if result[1] == True:
        print('Destination folder found, using it!')

    if result[1] == False:
        print('Destination folder not found, creating it')
        os.mkdir(os.path.join(os.getcwd(), folders[1]))
        # create destination folder
    return


def createPNG(folders):
    for imageName in os.listdir(folders[0]):
        name, extension = getExtension(imageName)
        img = Image.open(os.path.join(folders[0], name + extension))
        img.save(os.path.join(folders[1], name + ".png"))
    return


def getExtension(imageName):
    dot = imageName.find(".")
    name = imageName[:dot]
    extension = imageName[dot:]
    return name, extension


checkFolders(folders)
createPNG(folders)

print('done!')
