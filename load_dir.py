import os
import sys
from load import load

for root, dirs, files in os.walk(sys.argv[1]):
    for f in files:
        load(root + '/' + f)
