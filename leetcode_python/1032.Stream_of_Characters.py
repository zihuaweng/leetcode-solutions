#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()


class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.word = False


class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = TrieNode()
        self.waitlist = []
        # create a trie
        for word in words:
            root = self.trie
            for char in word[::-1]:
                root = root.children[char]
            root.word = True

    def query(self, letter: str) -> bool:
        self.waitlist.append(letter)
        # print(self.waitlist)
        i = len(self.waitlist) - 1
        
        root = self.trie
        while i >= 0:
            val = self.waitlist[i]
            if val not in root.children:
                return False
            root = root.children[val]
            if root.word:
                return True
            i -= 1
            
        return False
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
