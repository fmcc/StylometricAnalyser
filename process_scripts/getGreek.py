import os
from shutil import copy
import sys

# Directory to traverse looking for files. 
#source = sys.argv[1]
# Directory which the files will be copied to. 
destination = sys.argv[1]
with open('other_auths.txt') as f:
    for i in f:
        copy(i.strip(),destination)
"""
for root, dirs, files in os.walk(source):
    for f in files: 
        path = root + "/" + f
        if f.endswith('gk.xml'):
            copy(path,destination)
"""

