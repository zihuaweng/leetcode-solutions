#!/usr/bin/env python3
# coding: utf-8

# https://leetcode.com/problems/count-of-smaller-numbers-after-self/
#
# Time complexity: O(nlogn)
# Space complexity: O()

# 使用merge sort的方式，计算
# https://www.youtube.com/watch?v=AeyUmjk4HGQ

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:

        if not nums:
            return []

        res = [0] * len(nums)

        def merge_sort(items):
            if len(items) == 1:
                return items
            mid = len(items) // 2
            left = merge_sort(items[:mid])
            right = merge_sort(items[mid:])
            return merge(left, right)

        def merge(left, right):
            sort_res = []
            i = j = 0
            right_count = 0
            while i < len(left) and j < len(right):
                if left[i][0] > right[j][0]:
                    sort_res.append(right[j])
                    right_count += 1
                    j += 1
                else:
                    sort_res.append(left[i])
                    res[left[i][1]] += right_count
                    i += 1

            while i < len(left):
                res[left[i][1]] += right_count
                sort_res.append(left[i])
                i += 1

            while j < len(right):
                sort_res.append(right[j])
                j += 1

            return sort_res

        items = [(n, i) for i, n in enumerate(nums)]
        merge_sort(items)
        return res


# bit binary serach 方法
# https://leetcode.com/problems/count-of-smaller-numbers-after-self/discuss/76657/3-ways-(Segment-Tree-Binary-Indexed-Tree-Binary-Search-Tree)-clean-python-code
# https://leetcode.com/problems/count-of-smaller-numbers-after-self/discuss/76731/Nlogn-Python-solution-binary-indexed-tree-160-ms
