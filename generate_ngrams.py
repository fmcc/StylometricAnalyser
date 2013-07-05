import sys
import os
from NGramTrie.NGram import *

"""
This function will generate NGrams from all the files in a directory.
"""

def all_ngrams(top_dir):
    ngrams = set()

    for root, dirs, files in os.walk(top_dir):
        for f in files:
            with open(root + '/' + f) as file_in:
                n = NGram(3, file_in.read())
                ngrams.update(n.get_ngrams())

    return ngrams
