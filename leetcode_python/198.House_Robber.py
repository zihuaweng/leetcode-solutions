# https://leetcode.com/problems/house-robber/
# 这道题和走楼梯一样，也是斐波那契数列改变题目
# 每个值取决于他前面第二个，和前面第三个值的大小，反正不能是前面第一个，会报警，且不能是前第四个，因为中间肯定还有一个值可以加


# https://www.youtube.com/watch?v=-i2BFAU25Zk
class Solution:
    def rob(self, nums: List[int]) -> int:
        rob = 0
        not_rob = 0
        for num in nums:
            pre = max(not_rob, rob)
            rob = not_rob + num
            not_rob = pre
        return max(rob, not_rob)



class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) < 3:
            return max(nums)
        if len(nums) == 3:
            return max(nums[0] + nums[2], nums[1])

        res_list = [0] * 3
        res_list[0] = nums[0]
        res_list[1] = max(nums[0], nums[1])
        res_list[2] = max(nums[0] + nums[2], nums[1])

        for i in range(3, len(nums)):
            index = i % 3
            last_1 = (i - 2) % 3
            last_2 = (i - 3) % 3
            res_list[index] = nums[i] + max(res_list[last_1], res_list[last_2])

        return max(res_list)


# 更加清晰的dp思路：
# 子任务就是: dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
# 就是dp记录了目前为止最大结果，当前要不要算进去，取决于加上i-2的结果有没有大于 i-1的结果，如果i-1更大，证明这个空格可以不用算进去
class Solution2:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])

        return dp[-1]


# 稍微改变了一下存储方式
class Solution3:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        dp = [0] * 3
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            index = i % 3
            last_1 = (i - 1) % 3
            last_2 = (i - 2) % 3
            dp[index] = max(nums[i] + dp[last_2], dp[last_1])

        return max(dp)
