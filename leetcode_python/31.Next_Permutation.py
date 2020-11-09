# https://leetcode.com/problems/next-permutation/
# 从后面往前面找， 后面序列需要是递减的，所以找到第一个前面比后面小的值a。
# 接着从a往后找，找到第一个比a小的值b，替换
# 最后翻转b（原来a的位置）后面的值


class Solution:
    def nextPermutation(self, nums: list) -> None:
        class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        15245  -> 15254
        
        12642  -> 14[622]. -> 14[226] 
         | 2 is the first smaller 
        
        1. from the end of nums, keep looking for the first num that is < next
            start from len(nums)-2 (cur | next)
        2. if found smaller num: 
                swap the cur num with the first bigger number after cur
                since the last part is decreasing, we need to reverse it to get the smallest num
            not found, idx == -1:
                return nums[::-1]
        
        corner case:
            len(nums) <= 1 
        """
        idx = len(nums) - 2
        while idx >= 0 and nums[idx] >= nums[idx+1]:
            idx -= 1

        if idx >= 0:
            i = len(nums) - 1
            while i >= 0 and nums[i] <= nums[idx]:
                i -= 1
            nums[i], nums[idx] = nums[idx], nums[i]
        
        l = idx+1
        r = len(nums)-1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
            