import os
import sys
from bs4 import BeautifulSoup as BS

for root, dirs, files in os.walk(sys.argv[1]):
    for f in files:
        source = root + '/' + f
        parsed_file = BS(open(source))

        if parsed_file.l and parsed_file.p:
            os.rename(source, root + '/mix/' + f)
            continue
        if parsed_file.l:
            os.rename(source, root + '/verse/' + f)
            continue
        if parsed_file.p:
            os.rename(source, root + '/prose/' + f)
            continue

