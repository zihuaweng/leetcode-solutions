## https://leetcode.com/problems/3sum/
## 这道题重点在于2sum怎么计算。
## 首先排序，设置两个指针，向中间移动
## 3sum/4sum就是前面加一个循环，遍历前面一个+2sum 或者遍历前面两个+2sum


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        
        res = []
        nums.sort()
        l = len(nums)
        
        for i in range(l-2):
            # pruning : because the list is sort, if one > 0 then we can return res.
            if nums[i] > 0:   
                return res
            # pruning : skip the duplicated num
            if i > 0 and nums[i] == nums[i-1]:
                continue
            self.two_sum(nums[i+1:], -nums[i], res)
                
        return res
                
                
    def two_sum(self, nums, target, res):
        l = 0
        r = len(nums) - 1
        while l < r:
            if nums[l] + nums[r] == target:
                res.append([-target, nums[l], nums[r]])
                while l < r and nums[l] == nums[l+1]:
                    l += 1
                while l < r and nums[r] == nums[r-1]:
                    r -= 1
            if nums[l] + nums[r] < target:
                l += 1
            else:
                r -= 1
            