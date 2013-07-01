from NGramTrie.Trie import *

class NGram():

    def __init__(self, size, text):
        self.ngram_trie = Trie()
        self.ngram_set = set()
        self.text = text
        length = len(self.text)
        for start in range(0,length):
            out = ""
            if start + size > length:
                break
            else:
                end = start + size
            for to_gram in range(start,end):
                out += self.text[to_gram]
            self.ngram_trie.add(out)
    
    def get_vals(self):
        return self.ngram_trie.counts() 

    def get_ngrams(self):
        return self.ngram_trie.keys()

    def ngram_counts(self):
        ngrams = self.ngram_trie.items()
        return {n[0]:n[1] for n in ngrams}

