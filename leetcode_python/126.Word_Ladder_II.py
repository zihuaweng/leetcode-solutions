#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        """
        - build the graph: bfs
            - for each word, generate new word
                h. i. t
                25 25 25
            - check if the new word in word_set
                - add path to the graph
            - get the shortest path [step]
                
        - build the paths: dfs
            - start from beginWord
            - stop at endWord and step == 0
        
        """
        word_set = set(wordList)
        
        if endWord not in word_set:
            return []
        
        graph = collections.defaultdict(set)
        queue = set()
        queue.add(beginWord)
        seen = set()
        found = False
        steps = 1
        res = []
        
        while queue:
            next_words = set()
            for word in queue:
                for i in range(len(word)):
                    for j in range(26):
                        char = chr(ord('a')+j)
                        new_word = word[:i] + char + word[i+1:]
                        if new_word == endWord:
                            found = True
                        if new_word not in seen and new_word in word_set:
                            next_words.add(new_word)
                            graph[word].add(new_word)
                            
            if found:
                break
            steps += 1
            queue = next_words
            seen |= next_words
            
        
        def dfs(word, endWord, temp, steps):
            if steps < 0:
                return
            
            if word == endWord:
                res.append(temp)
                return
            
            for next_word in graph[word]:
                dfs(next_word, endWord, temp+[next_word], steps-1)
                
        dfs(beginWord, endWord, [beginWord], steps)
        
        return res
            
        
# 另一种实现
class Solution:
    # def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
    #     class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        res = []
        words = set(wordList)
        if endWord not in words:
            return res

        layer = {}
        layer[beginWord] = [[beginWord]]
        while layer:
            new_layer = collections.defaultdict(list)
            for key, path in layer.items():
                if key == endWord:
                    res.extend(path)
                else:
                    for i in range(len(key)):
                        for e in 'qwertyuiopasdfghjklzxcvbnm':
                            new = key[:i] + e + key[i + 1:]
                            if new in words:
                                new_layer[new] += [lst + [new] for lst in path]
            words -= set(new_layer.keys())
            layer = new_layer

        return res