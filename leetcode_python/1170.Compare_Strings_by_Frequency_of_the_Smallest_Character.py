#!/usr/bin/env python3
# coding: utf-8

# https://leetcode.com/problems/compare-strings-by-frequency-of-the-smallest-character/

# Time complexity: O(nlogn)
# Space complexity: O()


class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        res = []
        n = len(words)
        sort_w = sorted(w.count(min(w)) for w in words)
        for q in queries:
            cur = q.count(min(q))
            # 只要知道二分搜索cur可以放在哪个位置就好了。
            idx = bisect.bisect(sort_w, cur)
            res.append(n-idx)
        return res