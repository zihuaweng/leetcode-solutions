# https://leetcode.com/problems/search-in-rotated-sorted-array/
# 使用二分法找到位置。
# 首先确定每次中间的值的位置，与前面是顺序的还是与后面是顺序的
# 然后判断中间值是否在顺序的内容里，确定下一步的界限，接下来重复这两个判断，剩下两个值，如果两个值都没有则返回-1


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        56 [1] 234
        
        if nums[mid] < nums[left]:
            left is rotated
            right is sorted: if target in this range, left = mid+1
        
        56 [7] 812
        
        if nums[mid] >= nums[right]:
            left is sorted: if target in this range, right = mid
            right is rotated  
            
        """
        if not nums:
            return -1
        
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left+right) // 2
            
            if nums[mid] == target:
                return mid
            
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
                    
        return -1