import os
import sys
from bs4 import BeautifulSoup as BS
import re

all_tags = set()

for root, dirs, files in os.walk(sys.argv[1]):
    for f in files:
        xml_text = BS(open(root+'/'+f))
        text = xml_text.body
        all_tags.update(re.findall('</[^>]+>',str(text)))

print(sorted(all_tags))
