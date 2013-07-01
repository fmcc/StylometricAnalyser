class Trie():

    def __init__(self):
        self.root = dict()

    def __iter__(self):
        for i in self.__traverse():
            yield i

    def __contains__(self, key):
        return self.find(key)

    def __getitem__(self, key):
        if self.find(key):
            return self.find(key)
        else:
            raise KeyError
        
    
    def __traverse(self,sub_dict=None, k=""):
        if not sub_dict:
            sub_dict = self.root
        key = k
        nodes = []
        if sub_dict.get(True):
            node = sub_dict.get(True)
            return [(key, node['count'], node['value'])]
        else:
            for item in sorted(sub_dict.keys()):
                nodes = nodes + self.__traverse(sub_dict[item], k+item)
        return nodes
    
    def find(self, key):
        trie_dict = self.root
        for item in key:
            if item in trie_dict.keys():
                trie_dict = trie_dict[item]
            else:
                return False
        if True in trie_dict:
            return trie_dict[True]
        else:
            return False

    def add(self, key, value=None):
        trie_dict = self.root
        for char in key:
            trie_dict = trie_dict.setdefault(char, {})
        c = trie_dict.setdefault(True, {'count':0,'value':value})['count']
        trie_dict[True]['count'] = c + 1

    def keys(self):
        return [a[0] for a in self.__traverse()]

    def counts(self):
        return [a[1] for a in self.__traverse()]

    def values(self):
        return [a[2] for a in self.__traverse()]

    def items(self):
        return self.__traverse()


