#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O(n+m)

# https://leetcode.com/problems/number-of-matching-subsequences/

# https://leetcode.com/problems/number-of-matching-subsequences/discuss/117634/Efficient-and-simple-go-through-words-in-parallel-with-explanation

class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        d = collections.defaultdict(list)
        res = 0
        for w in words:
            d[w[0]].append(w)

        for char in S:
            lst = d[char]
            del d[char]
            for w in lst:
                if len(w) == 1:
                    res += 1
                else:
                    d[w[1]].append(w[1:])

        return res