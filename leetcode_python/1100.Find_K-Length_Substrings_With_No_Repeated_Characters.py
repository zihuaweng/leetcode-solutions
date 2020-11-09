#!/usr/bin/env python3
# coding: utf-8

# https://leetcode.com/problems/find-k-length-substrings-with-no-repeated-characters/

# Time complexity: O(n)
# Space complexity: O(n)


class Solution:
    def numKLenSubstrNoRepeats(self, S: str, K: int) -> int:
        if len(S) < K or len(set(S)) < K:
            return 0
        queue = collections.deque([])
        res = []
        for idx in range(len(S)):
            while S[idx] in queue:
                queue.popleft()

            queue.append(S[idx])
            if len(queue) == K:
                res.append(''.join(queue))
                queue.popleft()

        return len(res)


