#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        """
        as same as the 33. Search in Rotated Sorted Array
        but we need to consider duplicated cases
        
        [1,3,1,1,1]
           | M |
         | M |
        
        """
        if not nums:
            return False
        
        if not nums:
            return -1
        
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left+right) // 2
            
            if nums[mid] == target:
                return True
            
             # only need to add this part on top of No.33, 
             # just need to skip the duplicated one untial 
             # we have nums[mid] != nums[left]
            elif nums[mid] == nums[left]:  
                left += 1
                
            elif nums[mid] < nums[left]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
                    
            else:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
                    
        return False