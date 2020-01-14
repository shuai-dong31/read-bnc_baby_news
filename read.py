import xml.etree.ElementTree as ET

import os.path

import fnmatch

def get_content(filename):

    content = open(filename,"w")

    tree = ET.parse(filename)

    root = tree.getroot()

    for w in root.iter('w'):

        content.write(w.text)

    filename.close()

for file in os.listdir(os.getcwd()):

    if fnmatch.fnmatch(file, '*.xml'):

        get_content(file)
        
print('works are done,sucker')
    
