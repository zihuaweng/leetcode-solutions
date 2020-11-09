#!/usr/bin/env python3
# coding: utf-8

# https://leetcode.com/problems/search-in-a-sorted-array-of-unknown-size/
# BS主要需要确定界限，要用logn找界限可以每次右边界限右移一倍。确定好了左右界限，就可以做BS了。

# Time complexity: O(logT), where T is an index of target value.
# Space complexity: O(1)

class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        if reader.get(0) == target:
            return 0

        l, r = 0, 1
        while reader.get(r) < target:
            l = r
            r <<= 1

        while l <= r:
            mid = (l + r) // 2
            if reader.get(mid) < target:
                l = mid + 1
            elif reader.get(mid) > target:
                r = mid - 1
            else:
                return mid
        return -1


