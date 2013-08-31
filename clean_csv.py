import os
import sys
import re

for f in os.listdir(sys.argv[1]):
    os.rename(f, re.sub('^\d+_','',f))
