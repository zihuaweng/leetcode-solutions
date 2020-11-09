#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/design-search-autocomplete-system/

class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.rank = 0
        self.data = None


class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.root = TrieNode()
        self.keyword = ""
        for i, sentence in enumerate(sentences):
            self.add_record(sentence, times[i])

    def add_record(self, sentence, time):
        p = self.root
        for c in sentence:
            p = p.children[c]
        p.data = sentence
        p.rank -= time

    def search(self, word):
        p = self.root
        for w in word:
            if w not in p.children:
                return []
            p = p.children[w]
        return self.dfs(p)

    def dfs(self, root):
        if not root:
            return []
        res = []
        if root.data:
            res.append((root.rank, root.data))
        for child in root.children:
            res.extend(self.dfs(root.children[child]))
        return res

    def input(self, c: str) -> List[str]:
        res = []
        if c != '#':
            self.keyword += c
            res = self.search(self.keyword)
        else:
            self.add_record(self.keyword, 1)
            self.keyword = ""

        return [ele[1] for ele in sorted(res)[:3]]

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)