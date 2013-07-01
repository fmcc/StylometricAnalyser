from bs4 import BeautifulSoup as BS
import os
from shutil import copy
import sys

# Directory to traverse looking for files. 
source = sys.argv[1]
# Directory which the files will be copied to. 

existing_authors = ['Aeschines', 'Aeschylus', 'Andocides', 'Anonymous', 'Apollodorus', 'Apollonius Rhodius', 'Appian', 'Aretaeus', 'Aristides, Aelius', 'Aristides, Aelius\n\t', 'Aristophanes', 'Aristotle', 'Arrian', 'Athenaeus', 'Bacchylides', 'Colluthus', 'Demades', 'Demosthenes', 'Dinarchus', 'Dio, Chrysostom', 'Diodorus Siculus', 'Diogenes Laertius', 'Dionysius of Halicarnassus', 'Epictetus', 'Euclid', 'Euripides', 'Flavius Josephus', 'Galen', 'Herodotus', 'Hesiod', 'Hippocrates', 'Homer', 'Hyperides', 'Lucian', 'Lycurgus', 'Lysias', 'Pausanias', 'Pindar', 'Plato', 'Plutarch', 'Polybius', 'Pseudo-Plutarch', 'Sophocles', 'Strabo', 'Theocritus', 'Theophrastus', 'Xenophon']
output = ""

for root, dirs, files in os.walk(source):
    for f in files: 
        path = root + "/" + f
        f_xml = BS(open(path))
        if 'kai\\'in f_xml.text:
            if f_xml.author and f_xml.author.text not in existing_authors:
            #output += f_xml.title.text + " - " + f_xml.author.text + "\n"
                output += f_xml.author.text + " - " + path + "\n"      

with open('other_auths.txt','w+') as oot:
    oot.write(output)
