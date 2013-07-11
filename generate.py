from ngram import *
from settings import NGRAM_LENGTHS, NGRAM_WORDS

def generate_ngrams(text):
    if NGRAM_WORDS:
        text = text.split()
    ngrams = NGram(text, NGRAM_LENGTHS['MIN'], NGRAM_LENGTHS['MAX'])
    return ngrams.ngram_counts()

def generate_profile(ngrams, vector_space):
    profile = [ngrams.get(ngram,0) for ngram in vector_space]
    return profile
