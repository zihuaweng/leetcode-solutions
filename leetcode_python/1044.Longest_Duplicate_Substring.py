#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://www.youtube.com/watch?v=FQ8hcOOzQMU

class Solution:
    def longestDupSubstring(self, S: str) -> str:
        A = [ord(c) - ord('a') for c in S]
        mod = 2 ** 31 - 1

        def test(L):
            cur = 0
            for i in range(L):
                cur = (cur + 26 ** (L - i - 1) * A[i]) % mod
            seen = {cur}
            for i in range(L, len(S)):
                cur = ((cur - 26 ** (L - 1) * A[i - L]) * 26 + A[i]) % mod
                if cur in seen:
                    return i - L + 1
                seen.add(cur)

        # def test(L):
        #     p = pow(26, L, mod)
        #     cur = reduce(lambda x, y: (x * 26 + y) % mod, A[:L], 0)
        #     seen = {cur}
        #     for i in range(L, len(S)):
        #         cur = (cur * 26 + A[i] - A[i - L] * p) % mod
        #         if cur in seen: return i - L + 1
        #         seen.add(cur)

        res = 0
        i = 0
        j = len(S)
        while i < j:
            mid = (i + j + 1) // 2
            pos = test(mid)
            if pos:
                i = mid
                res = pos
            else:
                j = mid - 1
        return S[res: res + i]