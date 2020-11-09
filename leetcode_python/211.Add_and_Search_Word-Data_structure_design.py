#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/add-and-search-word-data-structure-design/


class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.end = False


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = TrieNode()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.trie
        for w in word:
            node = node.children[w]
        node.end = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        node = self.trie
        return self.dfs(word, node)

    def dfs(self, w, node):
        if not w:
            if node.end:
                return True
            return False

        if w[0] == '.':
            for n in node.children.values():
                if self.dfs(w[1:], n):
                    return True
        else:
            node = node.children.get(w[0])
            if not node:
                return False
            if self.dfs(w[1:], node):
                return True
        
        return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)