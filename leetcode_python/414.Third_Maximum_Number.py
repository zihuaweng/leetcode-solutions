# https://leetcode.com/problems/third-maximum-number/

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        res = [float('-inf')] * 3
        
        for num in nums:
            if num not in res:
                if num > res[0]:
                    res = [num, res[0], res[1]]
                elif num > res[1]:
                    res = [res[0], num, res[1]]
                elif num > res[2]:
                    res = [res[0], res[1], num]

        print(res)
        if res[2] == float('-inf'):
            return max(res)
        return res[2]