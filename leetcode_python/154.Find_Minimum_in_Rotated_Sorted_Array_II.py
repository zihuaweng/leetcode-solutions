#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/



class Solution:
    def findMin(self, nums: List[int]) -> int:
        i = 0
        j = len(nums) - 1
        while i < j:
            mid = (i+j) // 2
            if nums[mid] > nums[j]:
                i = mid + 1
            elif nums[mid] < nums[j]:
                j = mid
            else:
                if nums[j-1] > nums[j]:  # 这一步看注解
                    i = j
                    break
                j -= 1
        return nums[i]


# This code is correct to return the minimum value of the array. But in terms of "find the minimum value index" it is not right.
# Consider this case: 1 1 1 1 1 1 1 1 2 1 1
# the min index returned is 0, while actually it should be 9.
# For this case: 2 2 2 2 2 2 2 2 1 2 2
# it will return the correct index, which is 8.
#
# The reason is, the pivot index will be passed by at hi--. To avoid this, we can add the following judgement:
#
# else {
#
# if (nums[hi - 1] > nums[hi]) {
#     lo = hi;
#     break;
# }
# hi--;
# }