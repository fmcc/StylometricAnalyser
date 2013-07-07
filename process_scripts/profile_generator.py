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
        if f.endswith('ngrams.pkl'):
            file_path = root + '/' + f
            ngrams = pickle.load(open(file_path, 'rb'))
            print("creating profile of : " + file_path)
            profile = profile_text(ngrams, all_ngrams)
            pickle_path = file_path + "_profile.pkl"
            pickle.dump(profile,open(pickle_path,'wb'))



