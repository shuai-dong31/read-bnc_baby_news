import xml.etree.ElementTree as ET

import os.path

import fnmatch


def get_content(filename):

    file_w = "{}.txt".format(filename)

    content = open(file_w, "w")

    tree = ET.parse(filename)

    root = tree.getroot()
    for sent in root.iter('s'):
        for item in sent.itertext():
            content.write(item)
        content.write(" ")


for file in os.listdir(os.getcwd()):

    if fnmatch.fnmatch(file, '*.xml'):
        get_content(file)


print('run this line instead')
