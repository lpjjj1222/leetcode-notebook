class TrieNode:
    def __init__(self):
        self.children = {}
        self.words = [] #拥有从根节点顺到该节点的前缀的单词
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, product): #将每个product插入Trie
        node = self.root
        for letter in product:
            if letter not in node.children:
                node.children[letter] = TrieNode()
            node = node.children[letter]
            node.words.append(product)
            #不用排序直接pop是因为将products里面的每一个product插入Trie前先对所有product排序
            while len(node.words) > 3:
                node.words.pop()
    def search(self, prefix): #查找拥有某个prefix的单词
        node = self.root
        for letter in prefix:
            if letter not in node.children:
                return []
            node = node.children[letter]
        return node.words

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        trie = Trie()
        for product in products:
            trie.insert(product)
        
        res = []
        for i in range(len(searchWord)):
            prefix_word_list = trie.search(searchWord[:i+1])
            res.append(prefix_word_list)

        return res
        