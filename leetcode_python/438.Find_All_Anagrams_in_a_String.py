#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/find-all-anagrams-in-a-string/
# 很好的总结   438,340,76,1004
# https://leetcode.com/problems/find-all-anagrams-in-a-string/discuss/92007/Sliding-Window-algorithm-template-to-solve-all-the-Leetcode-substring-search-problem

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        # a:0
        # b:0
        # c:0
        # count = 0
        # i = 0,  (count == 0  i += 1)
        # res = [0, ]
        # j not match :  while:  match
        # c b a e b a b a c d
        #           i
        #                   j

        res = []

        if not s or len(p) > len(s):
            return res

        counter = collections.Counter(p)
        length = len(counter)

        i = 0
        for j, char in enumerate(s):
            if char in counter:
                counter[char] -= 1
                if counter[char] == 0:
                    length -= 1

            while length == 0:
                if j - i + 1 == len(p):
                    res.append(i)

                if s[i] in counter:
                    if counter[s[i]] == 0:
                        length += 1
                    counter[s[i]] += 1

                i += 1

        return res





