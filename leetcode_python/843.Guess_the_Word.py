#!/usr/bin/env python3
# coding: utf-8

# https://leetcode.com/problems/guess-the-word/
# https://leetcode.com/problems/guess-the-word/discuss/160945/Python-O(n)-with-maximum-overlap-heuristic
# 还没有更改答案

# Time complexity: O()
# Space complexity: O()


# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
         """
        10 guess
        each word has 6 char
        each time we guess on num get k matches
        
        1. choose a random word from wordlist, guess it, get k matches
        2. the secret should have that k matches, we can eliminate other words that do not have k same matches with gusss word
            1. for all other words, we need to find words share k matches with guessed word       
        """
        n = 0
        while n < 6:
            word = random.choice(wordlist)
            n = master.guess(word)
            wordlist = [w for w in wordlist if sum(g == w for g, w in zip(word, w)) == n]