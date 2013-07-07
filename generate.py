from ngram import *

def generate_ngrams(text):
    ngrams = NGram(text, 1, 11)
    return ngrams.ngram_counts()

def generate_profile(ngrams, vector_space):
    profile = [ngrams.get(ngram,0) for ngram in vector_space]
    return profile

