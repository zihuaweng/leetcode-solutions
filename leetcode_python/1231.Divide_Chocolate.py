#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/divide-chocolate/

class Solution:
    def maximizeSweetness(self, sweetness: List[int], K: int) -> int:

        def valid(mid):
            count = 1
            total = 0
            for s in sweetness:
                total += s
                if total > mid:
                    total = 0  # 这里和410不一样，本题目是想得到最低的值，所以超过了mid没关系，410需要所有都在mid里面。
                    count += 1
                    if count > K + 1:
                        return False
            return True

        i = min(sweetness)
        j = sum(sweetness) // (K + 1)
        while i <= j:
            mid = (i + j) // 2
            if valid(mid):
                j = mid - 1
            else:
                i = mid + 1

        return i


    def maximizeSweetness(self, sweetness: List[int], K: int) -> int:
        """
        [1,2,3,4,5,6,7,8,9]


        [1,2,3,4,5,6,7,8,9]

        8 gpa -> 5

        [1,2,3,| 4,5, | 6,| 7 | ,8|,9]

        brute force:
        1. split the arr into k+1 chunk, get the min chunk.  O(n^2)
            (n-1)*...*(n-k) situations
        2. get the max chunk from the min chunk from all splits.

        time O(n^2)
        space O(n)


        binary search
        max of min chunk -> split chunck with as max sum as possible
        max of min chunk we can get is sum(sweetness) // (K+1)  -> target     [binary search]
            if we can't split it to targe sum, reduce the target
            if we can split it to target sum, increase the target

        MIN_CHUNK_SUM = min(sweetness)    l 
        MAX_CHUNK_SUM = sum(sweetness) // (K+1)    r

        time O(nlogn)?
        space O()
        """
        def split_doable(bar):
            num = 0
            cur_sum = 0
            for s in sweetness:
                cur_sum += s
                if cur_sum >= bar:
                    cur_sum = 0
                    num += 1
            return num >= K+1
        
        l = min(sweetness)
        r = sum(sweetness) // (K+1)
        while l < r:
            mid = (l+r+1) // 2
            if split_doable(mid):
                l = mid
            else:
                r = mid - 1
                
        return l
    
