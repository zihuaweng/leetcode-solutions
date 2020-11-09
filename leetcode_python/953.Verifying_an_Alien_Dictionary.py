#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O(nlogn) [排序 + heap]
# Space complexity: O()


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if len(words) <= 1:
            return True

        dictionary = {}
        for i, j in enumerate(order):
            dictionary[j] = i

        for i in range(1, len(words)):
            a = words[i - 1]
            b = words[i]
            idx = 0
            while idx < len(a) and idx < len(b):
                if dictionary[a[idx]] > dictionary[b[idx]]:
                    return False
                if dictionary[a[idx]] < dictionary[b[idx]]:
                    break
                idx += 1
            else:
                if len(a) > len(b):
                    return False

        return True


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if len(words) <= 1:
            return True

        dictionary = {j: i for i, j in enumerate(order)}
        word_num = [[dictionary[c] for c in w] for w in words]
        for a, b in zip(word_num, word_num[1:]):
            if a > b:
                return False

        return True
