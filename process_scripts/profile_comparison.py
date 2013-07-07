import os
import sys
import pickle
import numpy

from text_profile import *
from NGramTrie.NGram import *

all_ngrams = pickle.load(open('ngram_store/all_ngrams.pkl','rb'))

file_profiles = []

for root, dirs, files in os.walk(sys.argv[1]):
    for f in files:
        if f.endswith('profile.pkl'):
            file_path = root + '/' + f
            print("adding :" + file_path)
            profile = pickle.load(open(file_path, 'rb'))
            file_profiles.append(profile) 

for f1 in file_profiles:
    out = ""
    for f2 in file_profiles:
        out = out + str(round(cosine_distance(f1,f2), 5)) + "\t|\t"
    print(out)


