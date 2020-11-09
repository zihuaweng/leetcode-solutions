#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        """
        - get the avg of arr for each subarry
            sum(arr) // m
            the result should be very close to the avg, bigger than avg
        
        we need to search between avg to sum(arr), find one value that could split arr into m
        - binary search left: avg, right: sum(arr)
        
        - range avg (3) to 15
        - 9
        split arr with sum(subarray) <= 9
        [1,2,3,4,5]
        
        1,2,3 | 4,5 => count = 2 == m, which means if we want even smaller, we need to decrease target, move left, mid
        result = 9  
        
        - range 3, 9
        - target 6
        [1,2,3,4,5]
        
        1,2,3 | 4 | 5 => count = 3 > m, increase target, move right, mid+1
        
        - range 6, 9
        - target 7
        [1,2,3,4,5]
        
        1,2,3 | 4 | 5 => count = 3 > m, increase target, move right, mid+1
        
        valid: count <= m : move left
        invalid: count > m or could not split: move right
        
        time O(logk)   k is the (sum) of nums
        space O(1)
        
        """
        hi = sum(nums)
        low = max(sum(nums) // m, max(nums))
        
        while low < hi:
            mid = (low+hi) // 2
            splits = self.get_splits(nums, mid)
            if splits > m:
                low = mid + 1
            else:
                hi = mid
        return low
            
            
    def get_splits(self, nums, target):
        count = 0
        cur_sum = 0
        for val in nums:
            if cur_sum + val <= target:
                cur_sum += val
            else:
                count += 1
                cur_sum = val
        count += 1
        return count
        

# https://leetcode.com/problems/split-array-largest-sum/discuss/141497/AC-Java-DFS-%2B-memorization
# dp 做法
# https://leetcode.com/problems/split-array-largest-sum/discuss/89821/Python-solution-dp-and-binary-search