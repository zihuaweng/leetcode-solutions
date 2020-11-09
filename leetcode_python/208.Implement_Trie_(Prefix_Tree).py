# https://leetcode.com/problems/implement-trie-prefix-tree/
# 主要是要知道TrieNode要怎么实现，用什么数据结构


class TrieNode(object):

    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        root = self.root
        for i in word:
            if i not in root.children:
                root.children[i] = TrieNode()
            root = root.children[i]
        root.is_word = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        root = self.root
        for i in word:
            if i not in root.children:
                return False
            root = root.children[i]
        if root.is_word:
            return True
        else:
            return False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        root = self.root
        for i in prefix:
            if i not in root.children:
                return False
            root = root.children[i]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)