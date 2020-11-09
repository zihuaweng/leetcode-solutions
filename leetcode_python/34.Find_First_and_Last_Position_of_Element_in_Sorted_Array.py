# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# 二分法

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        #         [5,      7,      7,      8,     8,   10]
        #         i               mid                  j
        #                                 i              j

        if not nums:
            return [-1, -1]

        i = 0
        j = len(nums) - 1

        while i <= j:
            # print(i, j, nums[i], nums[j])
            mid = (i + j) // 2
            if nums[mid] < target:
                i = mid + 1
            elif nums[mid] > target:
                j = mid - 1
            else:
                k = mid
                while k >= 0 and nums[k] == target:
                    k -= 1
                l = mid
                while l < len(nums) and nums[l] == target:
                    l += 1
                return [k + 1, l - 1]

        return [-1, -1]


