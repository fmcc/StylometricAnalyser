import os
import sys
import pickle
from scipy.spatial import distance

from text_profile import *
from NGramTrie.NGram import *

all_ngrams = pickle.load(open('ngram_store/all_ngrams.pkl','rb'))

file_profiles = []

for root, dirs, files in os.walk(sys.argv[1]):
    for f in files:
        file_path = root + '/' + f
        with open(file_path) as text:
            print("Ngramming: " + file_path)
            ngrams = NGram(text.read(),1,11)
            pickle_path = file_path + "_ngrams.pkl"
            pickle.dump(ngrams,open(pickle_path,'wb'))



