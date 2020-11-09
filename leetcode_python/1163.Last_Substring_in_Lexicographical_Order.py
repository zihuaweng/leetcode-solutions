#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O(n)
# Space complexity: O()

# https://leetcode.com/problems/last-substring-in-lexicographical-order/

# i, j 为需要比较的两个序列的开头index，k为长度
# 每次只看序列s[i:i+k]与s[j:j+k]
# 如果s[i+k] == s[j+k]， k+1继续看后面的数。如果s[i+k] < s[j+k]，i指针跳到最后，s[i+k] > s[j+k]，j指针跳到最后，其中如果i==j
# 需要把j后移，所以i一定是前面的更长的substring，直接返回s[i:]

class Solution:
    def lastSubstring(self, s: str) -> str:
        i = 0
        j = 1
        k = 0
        n = len(s)
        while j + k < n:
            if s[i+k] == s[j+k]:
                k += 1
                continue
            elif s[i+k] < s[j+k]:
                i = i + k + 1
            else:
                j = j + k + 1
            if j == i:
                j += 1
            k = 0
        return s[i:]