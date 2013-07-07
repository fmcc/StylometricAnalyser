from ngram import *
from settings import NGRAM_LENGTHS

def generate_ngrams(text):
    ngrams = NGram(text, NGRAM_LENGTHS['MIN'], NGRAM_LENGTHS['MAX'])
    return ngrams.ngram_counts()

def generate_profile(ngrams, vector_space):
    profile = [ngrams.get(ngram,0) for ngram in vector_space]
    return profile

def generate_vector_space(ngrams, vector_space):
    vector_space.update(ngrams.keys())
    return vector_space
    
