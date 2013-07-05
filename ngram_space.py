from NGramTrie.NGram import *
import os
import sys
import pickle

all_ngrams = set()

for root, dirs, files in os.walk(sys.argv[1]):
    for f in files:
        f_name = root + '/' + f
        with open(f_name) as text:
            ngrams = NGram(text.read(),1,11)
            all_ngrams.update(ngrams.get_ngrams())

with open('./ngram_store/all_ngrams.pkl', 'wb') as output:
    pickle.dump(all_ngrams, output)

print(len(all_ngrams))
