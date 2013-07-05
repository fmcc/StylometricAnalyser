from structures.trie import Trie

class NGram():

    def __init__(self, text, smallest_size, largest_size=None):
        self.ngram_trie = Trie()
        self.text = text
        length = len(self.text)

        def add_ngrams(ngram_length):
            for start in range(0,length):
                out = ""
                if start + ngram_length > length:
                    break
                else:
                    end = start + ngram_length
                for to_gram in range(start,end):
                    out += self.text[to_gram]
                self.ngram_trie.add(out)

        if largest_size:
            for i in range(smallest_size,largest_size):
                add_ngrams(i)
        else:
            add_ngrams(smallest_size) 
    
    def get_vals(self):
        return self.ngram_trie.counts() 

    def get_ngrams(self):
        return self.ngram_trie.keys()

    def ngram_counts(self):
        ngrams = self.ngram_trie.items()
        return {n[0]:n[1] for n in ngrams}
